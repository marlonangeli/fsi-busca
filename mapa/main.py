from datetime import datetime
from largura import bfs
from profundidade import dfs

def main():
    mapa = {
        'School': ['Lake', 'Bank', 'Club'],
        'Lake': ['Park', 'Bank'],
        'Bank': ['Park', 'Museum', 'Home'],
        'Club': ['Bank', 'Home'],
        'Museum': [],
        'Home': [],
        'Park': []
    }

    inicio = 'School'
    objetivo = 'Museum'
    inicio_tempo_bfs = datetime.now()
    print("Busca em Largura:")
    resultado_bfs = bfs(mapa, inicio, objetivo)
    fim_tempo_bfs = datetime.now()
    tempo_execucao_bfs = fim_tempo_bfs - inicio_tempo_bfs
    print("Tempo de execução do BFS:", tempo_execucao_bfs.microseconds, resultado_bfs)

    # Medir o tempo de execução do DFS
    inicio_tempo_dfs = datetime.now()
    print("Busca em Profundidade:")
    resultado_dfs = dfs(mapa, inicio, objetivo)
    fim_tempo_dfs = datetime.now()
    tempo_execucao_dfs = fim_tempo_dfs - inicio_tempo_dfs
    print("Tempo de execução do DFS:", tempo_execucao_dfs.microseconds, resultado_dfs)


if __name__ == '__main__':
    main()
