#Binarização.

# Pode ter arquivos maliciosos, nao tem como ver o que tem antes de executar
""""
felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Gato(Animal):

    def __int__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando...')


class Cachorro(Animal):

    def __int__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo...')

# Fazer leitura

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O Gato chama-se {gato._Animal__nome}')
    gato.mia()
    print(f'O tipo do gato é `{type(gato)}')

    print(f'O Cachorro chama-se {cachorro._Animal__nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')