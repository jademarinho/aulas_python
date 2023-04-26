
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

cliente1 = Cliente('Angelina', 'Jolie', '654654', 5000)
funcionario1 = Funcionario('Jade', 'Marinho', '6546464', 54564)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
print (cliente1.__dict__)
print(funcionario1.__dict__)