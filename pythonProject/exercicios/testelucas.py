idade = 0
linha_selecionada = []
i = 0
with open("actors.csv", "r+") as arquivo:
    for linha in arquivo:
        if '"Robert Downey, Jr."' in linha:
            linha = linha.replace('"Robert Downey, Jr."','"Robert Downey Jr."')
        if i == 0:
            i += 1
            continue
        l = linha.split(",")
        if int(l[2]) > idade:
            idade = int(l[2])
            linha_selecionada = l

    print(linha_selecionada[0], linha_selecionada[2])