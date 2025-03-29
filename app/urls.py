from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('planejador/', include('planejador.urls')),  # Aqui você inclui as rotas do app planejador
]
