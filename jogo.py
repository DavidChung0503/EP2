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


