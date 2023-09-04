from time import sleep
from profundidade_limitada import dls


def ids(mapa, inicio, objetivo, profundidade_maxima):
    for limite in range(profundidade_maxima + 1):
        resultado = dls(mapa, inicio, objetivo, limite)
        sleep(0.1)
        if resultado is not None:
            return resultado
