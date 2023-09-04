from time import sleep


def dfs(mapa, no, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    print(no)  # Substitua por sua lógica de processamento
    sleep(0.1)

    if no == objetivo:
        return True

    visitados.add(no)

    for vizinho in mapa[no]:
        if vizinho not in visitados:
            if dfs(mapa, vizinho, objetivo, visitados):
                return True

    return False
