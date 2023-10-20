import numpy as np
import pandas as pd

# seed para manter a reprodutibilidade
np.random.seed(0)

# geração de idades de acordo com a distribuição brasileira
idades = np.concatenate([np.random.choice(range(1, 45), int(0.64 * 1000)), 
                         np.random.choice(range(45, 61), int(0.36 * 1000))])

# geração de sexos (50% M e 50% F)
sexos = np.random.choice(['M', 'F'], 1000)

# geração dos peso de acordo com a idade
pesos = np.where(idades <= 8, np.round(np.random.normal(20, 5, len(idades)), 2),
                 np.where(idades <= 14, np.round(np.random.normal(45, 7, len(idades)), 2),
                          np.round(np.random.normal(70, 15, len(idades)), 2))
                )

# geração de alturas (distribuição normal)
alturas = np.round(np.random.normal(loc=140, scale=30, size=1000)).astype(int)
alturas = np.where(alturas < 30, 30, alturas)
alturas = np.where(alturas > 250, 250, alturas)

# geração tipos sanguíneos (aleatório)
tipos_sanguineos = np.random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'], 1000)

# geração gostos musicais (aleatório)
gostos_musicais = np.random.choice(['Pop', 'Rock', 'Sertanejo', 'Funk', 'Eletrônica', 'Outro'], 1000)

# geração esportes (aleatório)
esportes = np.random.choice(['Futebol', 'Basquete', 'Vôlei', 'Luta', 'Atletismo', 'eSports', 'Nenhum'], 1000)

# geração jogo favorito (aleatório)
jogos_favoritos = np.random.choice(['Counter-Strike', 'Minecraft', 'Fortnite', 'The Witcher', 'Valorant',
                                    'Assassins Creed', 'World of Warcraft', 'FIFA', 
                                    'League of Legends', 'Dota', 'Rocket League', 'Outro'], 1000)

dados = pd.DataFrame({
    'idade': idades,
    'sexo': sexos,
    'peso': np.round(pesos, 2),
    'altura': alturas,
    'tipo_sanguineo': tipos_sanguineos,
    'gosto_musical': gostos_musicais,
    'esporte': esportes,
    'jogo_favorito': jogos_favoritos
})

# cálculo de atributos (força, velocidade, inteligência)

def calculo_forca(row):
    result = 30
    if row['sexo'] == 'M':
        result += 30

    if row['esporte'] == 'Vôlei' or row['esporte'] == 'Luta':
        result += 20
    elif row['esporte'] == 'Nada':
        result -= 20

    if row['altura'] > 180:
        result += 20
    
    if row['idade'] > 65:
        result -= 15
    
    if result > 100:
        result = 100

    return result
        

def calculo_veloc(row):
    result = 30
    if row['sexo'] == 'F':
        result += 15

    if row['esporte'] == 'Futebol' or row['esporte'] == 'Atletismo':
        result += 30
    elif row['esporte'] == 'Nada' or row['esporte'] == 'eSports':
        result -= 20

    if row['peso'] > 150:
        result -= 20

    if row['altura'] <= 160:
        result += 20
    if row['idade'] > 65:
        result -= 20

    if row['gosto_musical'] == 'Funk' or row['gosto_musical'] == 'Eletrônica':
        result += 15

    if result > 100:
        result = 100

    return result

def calculo_int(row):
    result = 30
    if row['sexo'] == 'F':
        result += 25
    if row['esporte'] == 'Basquete' or row['esporte'] == 'eSports':
        result += 20
    if row['jogo_favorito'] == 'Dota' or row['jogo_favorito'] == 'League of Legends':
        result += 15
    
    if result > 100:
        result = 100
    return result

def definir_categoria(row):
    forca = row['forca']
    velocidade = row['velocidade']
    inteligencia = row['inteligencia']

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

# aplicando as funções de geração de atributos e categoria ao dataframe

dados['forca'] = dados.apply(calculo_forca , axis = 1)
dados['velocidade'] = dados.apply(calculo_veloc , axis = 1)
dados['inteligencia'] = dados.apply(calculo_int , axis = 1)
dados['categoria'] = dados.apply(definir_categoria, axis=1)


# primeiras linhas do dataframe
print(dados.head())

# exportando o dataframe
dados.to_csv('dataset_brinquedo.csv', index=False)