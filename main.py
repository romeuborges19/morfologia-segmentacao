from PIL import Image
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    main()
