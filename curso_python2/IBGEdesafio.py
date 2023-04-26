import csv

with open('desafio-ibge.csv', encoding='latin1') as f:
    reader = csv.reader(f)
    header = next(reader)  # lê a primeira linha como o cabeçalho

    for row in reader:
        nome_origem = row[3]
        nome_destino = row[8]
        print('Nome origem: {}'.format(nome_origem), end='\n')
        print('Nome destino: {}'.format(nome_destino), end='\n\n')
