"""
Funções com Retorno
.pop = tira o ultimo numero.


"""

numeros = [1, 2, 3, 4]

ret_pop = numeros.pop()

print(f'Retorno de pop:{ret_pop}')

print(numeros)

def quadrado_7():
    print(7 * 7)

quadrado_7()

ret = quadrado_7()
print(f'Retorno {ret}') ##none

##refatorar para retornar:

def qd_7():
    return 7 * 7
ret_7 = qd_7()
print(f'Retorno {ret_7 + 1}')

def diz_oi():
    return 'Oi! '
print (diz_oi())

alguem = 'Pedro'

print (diz_oi() + alguem)

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao())

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

print('------')

from random import random

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())