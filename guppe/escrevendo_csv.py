"""from csv import writer

with open('filmes.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração: ')
            escritor_csv.writerow([filme, genero, duracao])"""


# DictWriter
from csv import DictWriter

with open('filmes2.csv', 'w', encoding='utf-8', newline='') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme ou sair: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duracão: ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
