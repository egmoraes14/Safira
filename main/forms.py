# forms.py
from django import forms

class EscolhaForm(forms.Form):
    PERGUNTAS = [
        ('opcao1', 'Opção 1'),
        ('opcao2', 'Opção 2'),
        ('opcao3', 'Opção 3'),
        ('opcao4', 'Opção 4'),
        ('opcao5', 'Opção 5'),
    ]

    pergunta1 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 1')
    pergunta2 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 2')
    pergunta3 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 3')
    pergunta4 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 4')
    pergunta5 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 5')
