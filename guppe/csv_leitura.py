# Reader

"""from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #Pular 1 linha
    for linha in leitor_csv:
        print(f'{linha[0]} asdasd {linha[1]} asdas {linha[2]}')
"""
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']}")
