import datetime

hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')

print(hoje_formatado)

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(teste(5))