import numpy as np


class Morfologia:
    def __init__(self, imagem):
        self.imagem = np.array(imagem)
        self.height, self.width = self.imagem.shape
        print(self.width, self.height)
        self.estruturante = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def _aplicar_estruturante(self, imagem, x, y):
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if imagem[i][j] == 255:
                    return False
        return True

    def _erosao(self, imagem):
        PRETO = 0
        BRANCO = 255
        # print(self._get_frequencias())
        matriz_erodida = [[j for j in imagem[i]] for i in range(len(imagem))]
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if imagem[i][j] == PRETO:
                    if self._aplicar_estruturante(imagem, i, j):
                        matriz_erodida[i][j] = PRETO
                        continue
                matriz_erodida[i][j] = BRANCO

        return matriz_erodida

    def _dilatacao(self, imagem):
        matriz_erodida = [[j for j in imagem[i]] for i in range(len(imagem))]
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if imagem[i][j] == 0:
                    matriz_erodida[i][j - 1] = self.estruturante[1][0]
                    matriz_erodida[i][j] = self.estruturante[1][1]
                    matriz_erodida[i][j + 1] = self.estruturante[1][2]
                    matriz_erodida[i - 1][j - 1] = self.estruturante[0][0]
                    matriz_erodida[i - 1][j] = self.estruturante[0][1]
                    matriz_erodida[i - 1][j + 1] = self.estruturante[0][2]
                    matriz_erodida[i + 1][j - 1] = self.estruturante[2][0]
                    matriz_erodida[i + 1][j] = self.estruturante[2][1]
                    matriz_erodida[i + 1][j + 1] = self.estruturante[2][2]

        return matriz_erodida


class Fechamento(Morfologia):
    def run(self):
        imagem = self._erosao(self.imagem)
        imagem = self._dilatacao(imagem)
        return np.matrix(imagem).astype(np.uint8)


class Abertura(Morfologia):
    def run(self):
        imagem = self._dilatacao(self.imagem)
        imagem = self._erosao(imagem)
        return np.matrix(imagem).astype(np.uint8)
