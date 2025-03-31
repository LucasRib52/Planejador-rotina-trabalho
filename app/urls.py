from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # <- importa o redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('planejador/', permanent=False)),  # <- redireciona ao acessar /
    path('planejador/', include('planejador.urls')),
]
