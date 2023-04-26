class Animal():
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('Precisa implementar metodo')

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala au au')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala ik ik ik')

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()