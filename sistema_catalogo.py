from PySimpleGUI import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkTeal3')
dados = pd.read_csv('dataset_brinquedo.csv')
print(dados.head())

# funções
def calculo_forca(dict):
    result = 30
    if dict['sexo'] == 'M':
        result += 30

    if dict['esporte'] == 'Vôlei' or dict['esporte'] == 'Luta':
        result += 20
    elif dict['esporte'] == 'Nada':
        result -= 20

    if dict['altura'] > 180:
        result += 20
    
    if dict['idade'] > 65:
        result -= 15
    
    if result > 100:
        result = 100

    return result
        

def calculo_veloc(dict):
    result = 30
    if dict['sexo'] == 'F':
        result += 15

    if dict['esporte'] == 'Futebol' or dict['esporte'] == 'Atletismo':
        result += 30
    elif dict['esporte'] == 'Nada' or dict['esporte'] == 'eSports':
        result -= 20

    if dict['peso'] > 150:
        result -= 20

    if dict['altura'] <= 160:
        result += 20
    if dict['idade'] > 65:
        result -= 20

    if dict['gosto_musical'] == 'Funk' or dict['gosto_musical'] == 'Eletrônica':
        result += 15

    if result > 100:
        result = 100

    return result

def calculo_int(dict):
    result = 30
    if dict['sexo'] == 'F':
        result += 25
    if dict['esporte'] == 'Basquete' or dict['esporte'] == 'eSports':
        result += 20
    if dict['jogo_favorito'] == 'Dota' or dict['jogo_favorito'] == 'League of Legends':
        result += 15
    
    if result > 100:
        result = 100
    return result

def definir_categoria(dict):
    forca = dict['forca']
    velocidade = dict['velocidade']
    inteligencia = dict['inteligencia']

    if forca >= 60 and velocidade >= 60 and inteligencia >= 60:
            return 'Mutante especial'
    elif forca >= 65 and velocidade <= 50:
        return 'Tanque'
    elif velocidade >= 40 and inteligencia >= 65:
        return 'Estrategista'
    elif forca <= 40 and velocidade >= 65:
        return 'Corredor'
    else:
        return 'Comum'


def adicionar_zumbi():
    idade = valores['idade']
    peso = valores['peso']
    tipo_sangue = valores['tipo_sangue']
    esporte = valores['esporte']
    sexo = valores['sexo']
    altura = valores['altura']
    gosto_musical = valores['gosto_musical']
    jogo_favorito = valores['jogo_favorito']

    novo_zumbi = {
        'idade': int(idade),
        'sexo': sexo,
        'peso': float(peso),
        'altura': int(altura),
        'tipo_sanguineo': tipo_sangue,
        'gosto_musical': gosto_musical,
        'esporte': esporte,
        'jogo_favorito':jogo_favorito
    }

    novo_zumbi['forca'] = calculo_forca(novo_zumbi)
    novo_zumbi['velocidade'] = calculo_veloc(novo_zumbi)
    novo_zumbi['inteligencia'] = calculo_int(novo_zumbi)
    novo_zumbi['categoria'] = definir_categoria(novo_zumbi)

    dados.loc[len(dados)] = novo_zumbi


# tela inicio

tamanho_botao = (15,2)
layout_inicio = [
    [
        sg.Column(
            [
                [sg.Text('CatalogaZ', font=('Helvetica', 25))],
                [sg.Text(' ')],
                [sg.Button('Adicionar zumbi', font=('Helvetica', 15), size = tamanho_botao, enable_events=True)],
                [sg.Text(' ')],
                [sg.Button('Deletar zumbi', font=('Helvetica', 15), size = tamanho_botao, enable_events=True)],
                [sg.Text(' ')],
                [sg.Button('Visualizar zumbi', font=('Helvetica', 15), size = tamanho_botao, enable_events=True)],
            ], element_justification='l'
        ),
        sg.Column(
            [
                [sg.Image('menina.png', size = (300,300))],
            ], element_justification='r'
        )
    ]
]

# tela adicionar
opcoes = {
            'sexo': ['Masculino', 'Feminino'],
            'tipo_sanguineo': ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
            'gosto_musical': ['Pop', 'Rock', 'Pagode', 'Sertanejo', 'Hip-Hop/Rap', 'Eletrônica', 'Funk', 'Metal'],
            'esporte': ['Futebol', 'Basquete', 'Vôlei', 'Luta', 'Atletismo', 'eSports', 'Nada'],
            'jogo_favorito': ['Counter-Strike', 'Minecraft', 'Fortnite', 'The Witcher', 'Valorant', 'Assassins Creed',
                              'World of Warcraft', 'FIFA', 'League of Legends', 'Dota', 'Rocket League', 'Outro']
        }

fonte = ('Helvetica', 15)
tamanho = (25,1)
layout_adicionar = [
    [
        sg.Column(
            [
                [sg.Text('Idade', font=fonte, size=tamanho)],
                [sg.Input(key = 'idade', size=tamanho)],
                [sg.Text('Peso', font=fonte, size=tamanho)],
                [sg.Input(key = 'peso', size=tamanho)],
                [sg.Text('Tipo sanguíneo', font=fonte, size=tamanho)],
                [sg.Combo(opcoes['tipo_sanguineo'],default_value=opcoes['tipo_sanguineo'][0],size=tamanho,key = 'tipo_sangue')],
                [sg.Text('Esporte', font=fonte, size=tamanho)],
                [sg.Combo(opcoes['esporte'],default_value=opcoes['esporte'][0],size=tamanho,key = 'esporte')],
                [sg.Text('   ')],
                [sg.Button('Adicionar zumbi', font=fonte, size=tamanho, enable_events=True, key = 'adc_zumbi')]
            ], element_justification='l'
        ),
        sg.Column(
            [
                [sg.Text('Sexo biológico', font=fonte, size=tamanho)],
                [sg.Combo(opcoes['sexo'], default_value=opcoes['sexo'][0], size=tamanho ,key = 'sexo')],

                [sg.Text('Altura (cm)', font=fonte, size=tamanho)],
                [sg.Input(key = 'altura', size=tamanho)],

                [sg.Text('Gosto musical', font=fonte, size=tamanho)],
                [sg.Combo(opcoes['gosto_musical'],default_value=opcoes['gosto_musical'][0],size=tamanho,key = 'gosto_musical')],

                [sg.Text('Jogo favorito', font=fonte, size=tamanho)],
                [sg.Combo(opcoes['jogo_favorito'],default_value=opcoes['jogo_favorito'][0],size=tamanho,key = 'jogo_favorito')],

                [sg.Text('   ')],
                [sg.Button('Voltar', font=fonte, size=tamanho, enable_events=True)],
            ], element_justification='l'
        )
    ]
]

#dados
interface_dados = dados.values.tolist()

# telas deletar

layout_deletar = [
    [
        sg.Column(
            [
                [sg.Text('Deletar zumbi', font=('Helvetica', 25))],
                [sg.Text('Qual o número do zumbi a ser deletado?', font=('Helvetica', 15))],
                [sg.Input(key = '-INDEX-', size = (35,1)), sg.Button('OK')],
                [sg.Table(values=interface_dados, headings=['Idade','Sexo','Peso','Altura','Tipo Sanguíneo','Gosto musical','Esporte','Jogo Favorito', 'Força', 'Velocidade', 'Inteligência', 'Categoria'],
                          auto_size_columns=True, justification='center', key='-TABLE-', num_rows = 1)],
                [sg.Button('Deletar', key = 'delete', size = (5,1), enable_events=True)],
                [sg.Button('Voltar', font=fonte, size=tamanho, enable_events=True)],
            ], element_justification='l'
        ),
    ]
]

# tela visualizar
layout_visualizar = [
    [
        sg.Column(
            [
                [sg.Text('Visualizar zumbi', font=('Helvetica', 25))],
                [sg.Text('Qual o número do zumbi?', font=('Helvetica', 15))],
                [sg.Text('Digite o número e aperte OK, para voltar para a tabela digite qualquer letra e aperte OK', font=('Helvetica', 10))],
                [sg.Input(key = '-INDEX-', size = (35,1)), sg.Button('OK')],
                [sg.Table(values=interface_dados, headings=['Idade','Sexo','Peso','Altura','Tipo Sanguíneo','Gosto musical','Esporte','Jogo Favorito', 'Força', 'Velocidade', 'Inteligência', 'Categoria'],
                          auto_size_columns=True, justification='center', key='-TABLE-', num_rows = 24)],
                [sg.Button('Voltar', font=fonte, size=tamanho, enable_events=True)],
            ], element_justification='l'
        ),
    ]
]


# criando janelas
janela_inicio = sg.Window('Início', layout_inicio, size = (600,350))
janela_adicionar = sg.Window('Adicionar', layout_adicionar, size = (600,350))
janela_deletar = sg.Window('Deletar', layout_deletar, size = (1400,300))
janela_visualizar = sg.Window('Visualizar', layout_visualizar, size = (1400,600))

#selecionando janela
janela_atual = janela_inicio

# loop principal
while True:
    evento, valores = janela_atual.read(timeout=0)
    janela_atual.un_hide()
    if evento == sg.WINDOW_CLOSED:
        break
    

    if janela_atual == janela_inicio:
        if evento == 'Adicionar zumbi':
            janela_atual.Hide()
            janela_atual = janela_adicionar
        elif evento == 'Deletar zumbi':
            janela_atual.Hide()
            janela_atual = janela_deletar
        elif evento == 'Visualizar zumbi':
            janela_atual.Hide()
            janela_atual = janela_visualizar

    if janela_atual in [janela_adicionar, janela_deletar, janela_visualizar]:
            if evento == 'Voltar':
                janela_atual.Hide()
                janela_atual = janela_inicio

    if janela_atual == janela_adicionar:
        if evento == 'adc_zumbi':
            adicionar_zumbi()
            sg.popup_ok('Zumbi adicionado com sucesso!')
            # salvando banco de dados novo
            dados.to_csv('dataset_brinquedo.csv', index=False, mode='w')
    
    if janela_atual == janela_visualizar:
        if evento == 'OK':
            try:
                indice = int(valores['-INDEX-'])

                info = dados.iloc[indice].values.tolist()

                janela_atual['-TABLE-'].update(values=[info])

            except ValueError:
                janela_atual['-TABLE-'].update(values=interface_dados)
            except IndexError:
                pass
    
    if janela_atual == janela_deletar:
        if evento == 'OK':
            try:
                indice = int(valores['-INDEX-'])

                info = dados.iloc[indice].values.tolist()

                janela_atual['-TABLE-'].update(values=[info])

            except ValueError:
                janela_atual['-TABLE-'].update(values=interface_dados)
            except IndexError:
                pass
            ok = True
        if evento == 'delete' and ok == True:
            dados = dados.drop(indice)
            dados = dados.reset_index(drop=True)
            dados.to_csv('dataset_brinquedo.csv', index=False, mode='w')
            sg.popup_ok('Zumbi deletado com sucesso!')
            janela_atual['-TABLE-'].update(values=interface_dados)
# fechando janelas
janela_inicio.close()
janela_adicionar.close()
janela_deletar.close()
janela_visualizar.close()    

