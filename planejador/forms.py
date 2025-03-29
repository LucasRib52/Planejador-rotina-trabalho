from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = [
            'titulo',
            'descricao',
            'data',
            'hora',
            'realizado',
            'descricao_execucao'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título da tarefa'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva a tarefa (opcional)'
            }),
            'data': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'hora': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'realizado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'descricao_execucao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Descreva o que foi feito'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adiciona classe aos campos não incluídos via widgets
        for field_name, field in self.fields.items():
            if field.widget.__class__ not in [
                forms.CheckboxInput,
                forms.DateInput,
                forms.TimeInput,
                forms.Textarea,
                forms.TextInput
            ]:
                field.widget.attrs['class'] = 'form-control'
