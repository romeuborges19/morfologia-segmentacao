from PIL import Image

from morfologia import Abertura, Fechamento
from segmentacao import SegmentacaoLimiar


def _executar_algoritmo(classe_algoritmo, imagem, nome_resultado):
    instancia_algoritmo = classe_algoritmo(imagem)
    nova_imagem = instancia_algoritmo.run()

    nova_imagem = Image.fromarray(nova_imagem, mode="L")
    nova_imagem.save(f"image/{nome_resultado}.png")


def main():
    image = Image.open("image/teste.jpg")
    image = image.convert("L")

    _executar_algoritmo(SegmentacaoLimiar, image, "resultado-segmentacao")

    image = Image.open("image/teste.png")
    image = image.convert("L")
    _executar_algoritmo(Fechamento, image, "resultado-fechamento")
    _executar_algoritmo(Abertura, image, "resultado-abertura")


if __name__ == "__main__":
    main()
