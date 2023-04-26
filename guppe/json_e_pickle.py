"""
ret = json.dumps(['produto', {'PS4': ('2TB', 'Novo', '220v', 2340)}])

print(type(ret))

print(ret)

no final do cod

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)
"""
import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Amarelo')

ret = jsonpickle.encode(felix)
print(ret)