# Projeto Django com CRUD de Eventos e Chat usando FastAPI WebSocket e Redis

Este projeto Django integra um sistema de gerenciamento de eventos com um chat em tempo real, implementado com FastAPI WebSocket e usando Redis como banco de dados para o chat. O projeto inclui operações básicas de CRUD (Create, Read, Update, Delete) para eventos e funcionalidades de chat que persistem mensagens utilizando Redis.

## Funcionalidades Principais

## CRUD de Eventos

- **Listar Eventos**: Exibe uma lista de todos os eventos cadastrados.
- **Criar Evento**: Permite adicionar um novo evento ao sistema.
- **Editar Evento**: Permite modificar detalhes de um evento existente.
- **Deletar Evento**: Remove um evento do sistema.

## Chat em Tempo Real

- **Chat Utilizando FastAPI WebSocket**: Implementa um chat em tempo real usando FastAPI para WebSocket.
- **Persistência de Mensagens**: Utiliza Redis como banco de dados para armazenar mensagens de chat, permitindo a persistência das conversas.

## Requisitos do Projeto

Para executar este projeto, você precisará instalar as seguintes bibliotecas Python especificadas no arquivo `requirements.txt`:

- fastapi
- uvicorn
- aioredis
- django


## Instalação

1. Clone este repositório:

   git clone https://github.com/FabioCorreiaLima/chat-fastapi-websocket---django.git

2. Instale as dependências usando pip:
    pip install -r requirements.txt


## Configuração

1. Configure as variáveis de ambiente necessárias para o projeto, como as credenciais do Redis e outras configurações específicas.

2. Execute as migrações do Django para criar as tabelas do banco de dados:

    - python manage.py migrate

3. Inicie o servidor Django e o servidor FastAPI para WebSocket:
### Iniciar servidor Django
    python manage.py runserver

## Iniciar servidor FastAPI WebSocket (em outro terminal)
    uvicorn nome_do_arquivo:app --reload

## Video





## Contribuição

https://github.com/FabioCorreiaLima/chat-fastapi-websocket

https://github.com/FabioCorreiaLima/chat-fastapi-websocket---django/assets/118375746/1beedfa6-a1b9-422e-92d6-efa157e388ce



https://github.com/FabioCorreiaLima/chat-fastapi-websocket---django/assets/118375746/1beedfa6-a1b9-422e-92d6-efa157e388ce

---django/assets/118375746/d7e829d2-c322-403c-9b1f-db888d3af48c



https://github.com/FabioCorreiaLima/chat-fastapi-websocket---django/assets/118375746/d7e829d2-c322-403c-9b1f-db888d3af48c



Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas relatando bugs ou para enviar solicitações de alteração com melhorias.

