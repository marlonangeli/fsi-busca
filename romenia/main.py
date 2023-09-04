from profundidade_limitada import dls
from aprofundamento_iterativo import ids
from datetime import datetime


def main():
    romenia_mapa = {
        'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
        'Sibiu': ['Arad', 'Fagaras', 'Oradea', 'Rimnicu Vilcea'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Zerind': ['Arad', 'Oradea'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Oradea': ['Sibiu', 'Zerind'],
        'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
        'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
        'Bucharest': ['Fagaras', 'Pitesti']
    }

    inicio = 'Arad'
    objetivo = 'Bucharest'

    for limite in [2, 4, 7]:
        inicio_tempo_dls = datetime.now()
        resultado_dls = dls(romenia_mapa, inicio, objetivo, limite)
        fim_tempo_dls = datetime.now()
        tempo_execucao_dls = fim_tempo_dls - inicio_tempo_dls
        print(f"Tempo de execução do DLS ({limite}):", tempo_execucao_dls.microseconds)
        if resultado_dls:
            print(f'DLS com limite {limite}:', ' -> '.join(resultado_dls))
        else:
            print(f'DLS com limite {limite}: Não encontrado')

    profundidade_maxima = 7

    inicio_tempo_ids = datetime.now()
    resultado_ids = ids(romenia_mapa, inicio, objetivo, profundidade_maxima)
    fim_tempo_ids = datetime.now()
    tempo_execucao_ids = fim_tempo_ids - inicio_tempo_ids
    print(f"Tempo de execução do IDS:", tempo_execucao_ids.microseconds)

    if resultado_ids:
        print('IDS:', ' -> '.join(resultado_ids))
    else:
        print('IDS: Não encontrado')


if __name__ == '__main__':
    main()
