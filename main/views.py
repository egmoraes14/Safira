# views.py
from django.shortcuts import render, redirect
from .forms import EscolhaForm, EscolhaForm2, EscolhaForm3, EscolhaForm4

def trilha_do_conhecimento(request):
    return render(request, 'trilha.html')


def index_view(request):
    return render(request, 'index.html')

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
            request.session['escolhas1'] = escolhas
            return redirect('escolha2')
    else:
        form = EscolhaForm()
    return render(request, 'escolha1.html', {'form': form})

def escolha2_view(request):
    if request.method == 'POST':
        form = EscolhaForm2(request.POST)
        if form.is_valid():
            escolhas = {
                'pergunta6': form.cleaned_data['pergunta6'],
                'pergunta7': form.cleaned_data['pergunta7'],
                'pergunta8': form.cleaned_data['pergunta8'],
                'pergunta9': form.cleaned_data['pergunta9'],
                'pergunta10': form.cleaned_data['pergunta10'],
            }
            request.session['escolhas2'] = escolhas
            return redirect('escolha3')
    else:
        form = EscolhaForm2()
    return render(request, 'escolha2.html', {'form': form})

def escolha3_view(request):
    if request.method == 'POST':
        form = EscolhaForm3(request.POST)
        if form.is_valid():
            escolhas = {
                'pergunta11': form.cleaned_data['pergunta11'],
                'pergunta12': form.cleaned_data['pergunta12'],
                'pergunta13': form.cleaned_data['pergunta13'],
                'pergunta14': form.cleaned_data['pergunta14'],
                'pergunta15': form.cleaned_data['pergunta15'],
            }
            request.session['escolhas3'] = escolhas
            return redirect('escolha4')
    else:
        form = EscolhaForm3()
    return render(request, 'escolha3.html', {'form': form})

def escolha4_view(request):
    if request.method == 'POST':
        form = EscolhaForm4(request.POST)
        if form.is_valid():
            escolhas = {
                'pergunta16': form.cleaned_data['pergunta16'],
                'pergunta17': form.cleaned_data['pergunta17'],
                'pergunta18': form.cleaned_data['pergunta18'],
                'pergunta19': form.cleaned_data['pergunta19'],
                'pergunta20': form.cleaned_data['pergunta20'],
            }
            request.session['escolhas4'] = escolhas
            return redirect('resultado')
    else:
        form = EscolhaForm4()
    return render(request, 'escolha4.html', {'form': form})


def resultado_view(request):
    escolhas = {
        'escolhas1': request.session.get('escolhas1', {}),
        'escolhas2': request.session.get('escolhas2', {}),
        'escolhas3': request.session.get('escolhas3', {}),
        'escolhas4': request.session.get('escolhas4', {}),
        
    }

    # Contar quantas vezes cada alternativa foi escolhida
    contagem = {
        'opcao1': 0,
        'opcao2': 0,
        'opcao3': 0,
        'opcao4': 0,
        'opcao5': 0,
    }
    
    for escolhas_form in escolhas.values():
        for escolha in escolhas_form.values():
            if escolha in contagem:
                contagem[escolha] += 1

    # Calcular os valores ponderados
    opcao1_count = contagem['opcao1']
    opcao2_count = contagem['opcao2'] * 2
    opcao3_count = contagem['opcao3'] * 3
    opcao4_count = contagem['opcao4'] * 4
    opcao5_count = contagem['opcao5'] * 5
    total = opcao1_count + opcao2_count + opcao3_count + opcao4_count + opcao5_count

    return render(request, 'resultado.html', {
        'contagem': contagem,
        'total': total,
    })
