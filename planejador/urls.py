# planejador/urls.py
from django.urls import path
from .views import (
    TarefaListView, TarefaCreateView, TarefaUpdateView, TarefaDeleteView, atualizar_tarefa
)

app_name = 'planejador'

urlpatterns = [
    path('', TarefaListView.as_view(), name='lista'),
    path('nova/', TarefaCreateView.as_view(), name='nova'),
    path('editar/<int:pk>/', TarefaUpdateView.as_view(), name='editar'),
    path('deletar/<int:pk>/', TarefaDeleteView.as_view(), name='deletar'),
    path('atualizar-tarefa/', atualizar_tarefa, name='atualizar-tarefa'),
]
