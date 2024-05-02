# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}
# frotas de cada pais
PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}
# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

import random
def cria_mapa(N):
    matriz = []
    i = 0
    while i < N:
        linha = []
        j = 0
        while j < N:
            linha.append(' ')
            j += 1
        matriz.append(linha)
        i += 1
    return matriz

def posicao_suporta(mapa, blocos, linha, coluna, orientacao):
    tamanho_mapa = len(mapa)
    i = 0
    while i < blocos:
        if linha < 0 or coluna < 0 or (orientacao == 'v' and linha + i >= tamanho_mapa) or (orientacao == 'h' and coluna + i >= tamanho_mapa):
            return False
        if orientacao == 'v':
            if mapa[linha + i][coluna] != ' ':
                return False
        elif orientacao == 'h':
            if mapa[linha][coluna + i] != ' ':
                return False
        i += 1
    return True

def aloca_navios(mapa, blocos):
    n = len(mapa)
    tamanho_navios = len(blocos)
    navio_atual = 0
    while navio_atual < tamanho_navios:
        tamanho_navio = blocos[navio_atual]
        linha = random.randint(0, n-1)
        coluna = random.randint(0, n-1)
        orientacao = random.choice(['h', 'v'])
        if posicao_suporta(mapa, tamanho_navio, linha, coluna, orientacao):
            for i in range(tamanho_navio):
                if orientacao == 'v':
                    mapa[linha + i][coluna] = 'N'
                else:
                    mapa[linha][coluna + i] = 'N'
            navio_atual += 1
    return mapa

def foi_derrotado(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            if matriz[i][j] == 'N':
                return False
            j += 1
        i += 1
    return True

mapa_computador = cria_mapa(10)
mapa_jogador = cria_mapa(10)


lista_paises = ['Brasil', 'França', 'Austrália', 'Rússia', 'Japão']
computador_escolha = random.choice(lista_paises)
print(f"Iniciando o Jogo!\n\nComputador está alocando os navios de guerra do país {computador_escolha}...\nComputador já está em posição de batalha!\n")
print("1: Brasil\n   1 cruzador\n   2 torpedeiro\n   1 destroyer\n   1 couracado\n   1 porta-aviões\n\n2: França\n   3 cruzador\n   1 porta-aviões\n   1 destroyer\n   1 submarino\n   1 couracado\n\n3: Austrália\n   1 couracado\n   3 cruzador\n   1 submarino\n   1 porta-aviões\n   1 torpedeiro\n\n4: Rússia\n   1 cruzador\n   1 porta-aviões\n   2 couracado\n   1 destroyer\n   1 submarino\n\n5: Japão\n   2 torpedeiro\n   1 cruzador\n   2 destroyer\n   1 couracado\n   1 submarino\n")
frota = input('Qual o número da nação da sua frota? ')
numeros = ['1', '2', '3', '4', '5']
while not frota in numeros:
    print('Opção inválida')
    frota = input('Qual o número da nação da sua frota? ')
if frota == numeros[0]:
    nação = 'Brasil'
elif frota == numeros[1]:
    nação = 'França'
elif frota == numeros[2]:
    nação = 'Austrália'
elif frota == numeros[3]:
    nação = 'Rússia'
elif frota == numeros[4]:
    nação = 'Japão'
if frota in numeros:

    print(f'Você escolheu a nação {nação}')
    print('Agora é a sua vez de alocar seus navios de guerra!')

print(f"  COMPUTADOR - {computador_escolha}                   JOGADOR - {nação}                  "
"\n   A  B  C  D  E  F  G  H  I  J            A  B  C  D  E  F  G  H  I  J   ")

for i in range(10):
    linha_c = '  '.join(mapa_computador[i])
    linha_j = '  '.join(mapa_jogador[i])

    n_linha = f"{i+1:2}" 
    print(f"{n_linha} {linha_c} {n_linha}      {n_linha} {linha_j} {n_linha}")

print ("   A  B  C  D  E  F  G  H  I  J            A  B  C  D  E  F  G  H  I  J   ")


