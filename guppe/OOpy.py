"""
POO Atributos

Voltagem, Atributo, Ligada ou Desligada
Atributos de instancia, de classe e dinamicos
Todo atributo é publico. Quando é privado usa __ no inicio do atributo meramente para ilustração.
Não funciona se chamar no dir.
ex: __cor
__voltagem
__ligada
"""
class Lampada:
    def __init__(self, voltagem, cor): ##construtor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False



class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

l1 = Lampada('220V', 'amarela')

print(l1.voltagem)

