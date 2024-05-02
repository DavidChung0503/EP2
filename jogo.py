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