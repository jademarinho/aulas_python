import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2019, 3, 3, 0)

tempo_para_evento = aniversario - data_hoje

print(tempo_para_evento)

#______

data_compra = datetime.datetime.now()

print(data_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_compra + regra_boleto

print(vencimento_boleto)

"""
dias da semana
0 segunda
1 terça
2 quarta
...

"""