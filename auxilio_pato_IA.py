'''
Descrição: o sistema de auxílio ao pato de combate irá identificar a classe do ser e a partir disso irá sugerir ações
IA será treinada com imagens geradas pelo Dall-e  ->  

classes: 
   - humano
   - Z mutante
   - Z tanque
   - Z estrategista
   - Z comum

pontos fracos (de acordo com a classe):
   - Z mutante
   - Z tanque
   - Z estrategista
   - Z comum

Simulador:
imagens aleatórias aparecerão, botão para trocar imagem
irá aparecer -> imagem, pato, ataque, defesa, botão para trocar imagem

Irá disparar um 'sinal' para o pato

'''


from PySimpleGUI import PySimpleGUI as sg
import numpy as np
import re
import os
import glob

sg.theme('DarkPurple5')


# pegando as imagens de zumbis para simulação
caminho_img = []
caminho_pasta = 'assets'
imagens = glob.glob(os.path.join(caminho_pasta, '*.png'))
for imagem in imagens:
    nome_imagem = os.path.basename(imagem)
    print(nome_imagem)
    caminho_img.append(nome_imagem)


# armazenamento das características: [[perigo], [defesa], [ataque], [pontos fracos], [pontos fortes]]
dicio = {
    'comum': [['baixo'], ['correr', 'bomba de fumaça'], ['bomba incendiária', 'braço robô atirar']
              , ['lento, não inteligente, pouca força física'], ['possibilidade de formação de horda']],
              
    'estrategista': [['alto'], ['bomba de fumaça' , 'escudo de energia'], ['bomba incendiária', 'braço robô atirar'], 
                     ['pouca força física, lento'], ['desperta zumbis próximos para ajudar no ataque']],

    'tanque': [['médio'], ['correr / fugir'], ['bomba incendiária', 'braço robô atirar'], 
               ['fogo, não muito inteligente, não muito ágil'], ['alta resistência física, muita força física']],

    'corredor': [['alto'], ['bomba de choque', 'voar', 'escudo de energia'], ['despejar óleo no chão + lança-chamas'], 
                 ['pouca força física, pouca inteligência'], ['muito ágil e atlético, se aproxima facilmente']],

    'mutante': [['ALTÍSSIMO - PRIORIZAR A FUGA!!'], ['fumaça + voar', 'bomba de choque + correr'],
                ['bomba incendiária', 'braço robô atirar', 'despejar óleo no chão + lança-chamas'], 
                ['esse tipo de espécime não possui pontos fracos'], ['raro espécime, possui todos os atributos acima da média']],
}

def info_classe(img):
    classes = ['comum', 'tanque', 'estrategista', 'mutante', 'corredor']
    for _, classe in enumerate(classes):
        if classe in img:
            return classe
def info_num(img):
    numero = re.findall(r'\d+', img)
    return numero[0]



img = 'assets/' + np.random.choice(caminho_img)
classe = info_classe(img)
qnt = info_num(img)
perigo = dicio[classe][0][0]
fraco = dicio[classe][3][0]
forte = dicio[classe][4][0]

def_ = np.random.choice(dicio[classe][1])
atk = np.random.choice(dicio[classe][2])

fonte_txt = ('Helvetica', 13)
layout = [
    [
        sg.Column(
            [
                [sg.Image(filename='mallard.png', key='-DUCK-', size=(260, 260))],
                [sg.Text(' ')],
                [sg.Text(' ')],
                [sg.Image(filename='shield.png', size=(33,39)), sg.Text('Defesa', font = ('Helvetica', 20))],
                [sg.Text(def_, font = fonte_txt, key = '-defesa-')],
                [sg.Image(filename='sword.png', size=(39,33)), sg.Text('Ataque', font = ('Helvetica', 20))],
                [sg.Text(atk, font = fonte_txt, key = '-ataque-')],
            ], element_justification='l'
        ),
        sg.Column(
            [
                [sg.Text('Visão real do pato', font = ('Helvetica', 25))],
                [sg.Image(filename=img, key='-IMAGE-', size=(300, 300))],
                [sg.Button('trocar imagem', font = ('Helvetica', 10))],
                [sg.Text('Contagem: ', font = ('Helvetica', 15)), sg.Text(qnt, font = fonte_txt, key='-quantidade-')],
                [sg.Text('Periculosidade: ', font = ('Helvetica', 15)), sg.Text(perigo, font = fonte_txt, key='-perigo-')],
                [sg.Text('Pontos fracos: ', font = ('Helvetica', 15)), sg.Text(fraco, font = fonte_txt, key='-pnt fracos-')],
                [sg.Text('Pontos fortes: ', font = ('Helvetica', 15)), sg.Text(forte, font = fonte_txt, key='-pnt fortes-')],
            ], element_justification='l'
        )
        
    ]
]





janela = sg.Window('Pato de combate', layout, size = (900,550))




while True:
    evento, valores = janela.read(timeout=0)

    if evento == sg.WIN_CLOSED:
        break

    if evento == 'trocar imagem':
        # Atualizando o texto
        img = 'assets/' + np.random.choice(caminho_img)
        classe = info_classe(img)
        qnt = info_num(img)
        perigo = dicio[classe][0][0]
        fraco = dicio[classe][3][0]
        forte = dicio[classe][4][0]

        def_ = np.random.choice(dicio[classe][1])
        atk = np.random.choice(dicio[classe][2])
        
        print('-------')
        print(img)
        print(classe)
        print(fraco)
        print(forte)

        janela['-defesa-'].update(def_)
        janela['-ataque-'].update(atk)

        janela['-IMAGE-'].update(filename= img)
        janela['-quantidade-'].update(qnt)
        janela['-perigo-'].update(perigo)
        janela['-pnt fracos-'].update(fraco)
        janela['-pnt fortes-'].update(forte)

# Fechando a janela
janela.close()