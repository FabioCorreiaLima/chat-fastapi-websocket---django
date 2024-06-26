from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import aioredis

router = APIRouter()

class GerenciadorConexoes:
    def __init__(self):
        self.conexoes_ativas = {}
        self.redis = None

    async def conectar(self, websocket: WebSocket, evento_id: int, username: str):
        await websocket.accept()
        chave_evento = f"chat:{evento_id}"
        if evento_id not in self.conexoes_ativas:
            self.conexoes_ativas[evento_id] = []
        self.conexoes_ativas[evento_id].append((username, websocket))

        if self.redis:
            mensagens = await self.redis.lrange(chave_evento, 0, -1)
            for mensagem in mensagens:
                await websocket.send_text(mensagem.decode())

    def desconectar(self, websocket: WebSocket, evento_id: int):
        if evento_id in self.conexoes_ativas:
            self.conexoes_ativas[evento_id] = [(username, ws) for username, ws in self.conexoes_ativas[evento_id] if ws != websocket]

    async def enviar_mensagem_pessoal(self, mensagem: str, websocket: WebSocket, evento_id: int):
        await websocket.send_text(mensagem)

    async def transmitir(self, evento_id: int, mensagem: str, username: str):
        chave_evento = f"chat:{evento_id}"
        mensagem_enviada = f"{username}: {mensagem}"
        if self.redis:
            await self.redis.lpush(chave_evento, mensagem_enviada)
            for _, conexao in self.conexoes_ativas.get(evento_id, []):
                await conexao.send_text(mensagem_enviada)

    async def startup_event(self):
        self.redis = await aioredis.from_url('redis://localhost')

    async def shutdown_event(self):
        if self.redis:
            await self.redis.close()

gerenciador = GerenciadorConexoes()

@router.get("/chat/{evento_id}/{username}", response_class=HTMLResponse)
async def get_chat(evento_id: int, username: str):
    with open("users/templates/chat.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content.replace("{{ evento_id }}", str(evento_id)).replace("{{ username }}", username))

@router.websocket("/ws/{evento_id}/{username}")
async def websocket_endpoint(websocket: WebSocket, evento_id: int, username: str):
    await gerenciador.conectar(websocket, evento_id, username)
    try:
        while True:
            dados = await websocket.receive_text()
            await gerenciador.transmitir(evento_id, dados, username)
    except WebSocketDisconnect:
        gerenciador.desconectar(websocket, evento_id)
