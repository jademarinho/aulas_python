with open("actors.csv") as arquivo:
    dados = arquivo.read().replace('"Robert Downey, Jr."',"Robert Downey Jr.").split('\n')

    for linha in dados[1:]:
        ator = (linha.split(",")[0])
        valor =(linha.split(",")[1])

        print(f'{ator} tem {valor}\n')