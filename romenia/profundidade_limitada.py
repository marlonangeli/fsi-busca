from time import sleep


def dls(mapa, no, objetivo, profundidade_limite, visitados=None):
    if visitados is None:
        visitados = set()
    sleep(0.1)

    if no == objetivo:
        return [no]

    if profundidade_limite == 0:
        return None

    visitados.add(no)

    for vizinho in mapa.get(no, []):
        if vizinho not in visitados:
            resultado = dls(mapa, vizinho, objetivo, profundidade_limite - 1, visitados)
            if resultado is not None:
                return [no] + resultado

    return None
