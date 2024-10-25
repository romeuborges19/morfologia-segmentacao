import numpy as np


class SegmentacaoLimiar:
    def __init__(self, imagem):
        self.imagem = np.array(imagem)
        self.width, self.height = self.imagem.shape

    def _get_frequencias(self):
        quantidades = {k: 0 for k in range(256)}
        for i in range(self.width):
            for j in range(self.height):
                nivel = int(self.imagem[i][j])
                quantidades[nivel] += 1

        return quantidades

    def encontrar_vales(self):
        quantidades = self._get_frequencias()
        lista_valores = [int(v) for v in quantidades.values()]

        vales = []
        for i in range(1, len(lista_valores) - 1):
            if lista_valores[i - 1] > lista_valores[i] < lista_valores[i + 1]:
                vales.append(i)

        return vales

    def encontrar_limiar(self, vales: list[int]):
        melhor_limiar = vales[0]
        meio_escala = 255 // 2

        menor_distancia = 255
        for valor in vales:
            if valor > meio_escala:
                distancia_meio = valor - meio_escala
            else:
                distancia_meio = meio_escala - valor

            if distancia_meio < menor_distancia:
                menor_distancia = distancia_meio
                melhor_limiar = valor

        return melhor_limiar

    def run(self):
        vales = self.encontrar_vales()
        limiar = self.encontrar_limiar(vales)

        nova_imagem = [
            [255 if int(self.imagem[i][j]) >= limiar else 0 for j in range(self.width)]
            for i in range(self.height)
        ]

        return np.matrix(nova_imagem).astype(np.uint8)
