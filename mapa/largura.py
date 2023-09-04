from collections import deque
from time import sleep


def bfs(mapa, inicio, objetivo):
    fila = deque()
    fila.append(inicio)
    visitados = set()

    while fila:
        no = fila.popleft()
        visitados.add(no)
        print(no)  # Substitua por sua lógica de processamento
        sleep(0.1)

        if no == objetivo:
            return True

        for vizinho in mapa[no]:
            if vizinho not in visitados and vizinho not in fila:
                fila.append(vizinho)

    return False