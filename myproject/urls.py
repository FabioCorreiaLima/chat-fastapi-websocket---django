from django.contrib import admin
from django.urls import path, include
from users.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('users.urls')), # Substitua 'users.urls' pelo caminho correto para suas URLs
]
