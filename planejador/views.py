# planejador/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Tarefa
from .forms import TarefaForm
from django.core.serializers.json import DjangoJSONEncoder
import json

class TarefaListView(ListView):
    model = Tarefa
    template_name = 'planejador/listar.html'  

    def get_queryset(self):
        return Tarefa.objects.order_by('data', 'hora')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        tarefas_queryset = self.get_queryset()
        tarefas_dict = list(tarefas_queryset.values(
            'id', 'titulo', 'descricao', 'data', 'hora', 'realizado',
            'descricao_execucao', 'hora_finalizacao', 'motivo_nao_finalizado'
        ))

        # Converte hora_finalizacao para string formatada (HH:MM)
        for tarefa in tarefas_dict:
            if tarefa['hora_finalizacao']:
                tarefa['hora_finalizacao'] = tarefa['hora_finalizacao'].strftime('%H:%M')

        context['tarefas_json'] = json.dumps(tarefas_dict, cls=DjangoJSONEncoder)
        return context


class TarefaCreateView(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'planejador/form.html' 
    success_url = reverse_lazy('planejador:lista')


class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'planejador/form.html' 
    success_url = reverse_lazy('planejador:lista')


class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = 'planejador/confirmar_exclusao.html'
    success_url = reverse_lazy('planejador:lista')


@csrf_exempt
def atualizar_tarefa(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        realizado = request.POST.get('realizado') == 'true'
        descricao_execucao = request.POST.get('descricao_execucao', '')
        hora_finalizacao = request.POST.get('hora_finalizacao') or None
        motivo = request.POST.get('motivo_nao_finalizado') or ''

        tarefa = Tarefa.objects.get(id=id)
        tarefa.realizado = realizado
        tarefa.descricao_execucao = descricao_execucao
        tarefa.hora_finalizacao = hora_finalizacao if realizado else None
        tarefa.motivo_nao_finalizado = motivo if not realizado else ''
        tarefa.save()

        return JsonResponse({'success': True})
