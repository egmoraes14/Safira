# views.py
from django.shortcuts import render, redirect
from .forms import EscolhaForm

def trilha_do_conhecimento(request):
    return render(request, 'trilha.html')

def escolha1_view(request):
    if request.method == 'POST':
        form = EscolhaForm(request.POST)
        if form.is_valid():
            escolhas = {
                'pergunta1': form.cleaned_data['pergunta1'],
                'pergunta2': form.cleaned_data['pergunta2'],
                'pergunta3': form.cleaned_data['pergunta3'],
                'pergunta4': form.cleaned_data['pergunta4'],
                'pergunta5': form.cleaned_data['pergunta5'],
            }
            request.session['escolhas'] = escolhas
            return redirect('escolha2')
    else:
        form = EscolhaForm()
    return render(request, 'escolha1.html', {'form': form})

def proxima_pesquisa_view(request):
    escolhas = request.session.get('escolhas', {})
    
    # Contar quantas vezes cada alternativa foi escolhida
    contagem = {
        'opcao1': 0,
        'opcao2': 0,
        'opcao3': 0,
        'opcao4': 0,
        'opcao5': 0,
    }
    
    for escolha in escolhas.values():
        if escolha in contagem:
            contagem[escolha] += 1
    
    # Armazenar os valores em variáveis
    opcao1_count = contagem['opcao1']
    opcao2_count = contagem['opcao2']
    opcao3_count = contagem['opcao3']
    opcao4_count = contagem['opcao4']
    opcao5_count = contagem['opcao5']
    
    opcao2_count = opcao2_count * 2
    opcao3_count = opcao3_count * 3
    opcao4_count = opcao4_count * 4
    opcao5_count = opcao5_count * 5
    total_part1 = opcao1_count + opcao2_count + opcao3_count + opcao4_count + opcao5_count

    return render(request, 'proxima_pesquisa.html', {
        'escolhas': escolhas,
        'opcao1_count': opcao1_count,
        'opcao2_count': opcao2_count,
        'opcao3_count': opcao3_count,
        'opcao4_count': opcao4_count,
        'opcao5_count': opcao5_count,
        'total_part1': total_part1,

    })

def escolha2(request):
    return render(request, 'escolha2.html')
