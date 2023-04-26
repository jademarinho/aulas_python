print("Qual é o seu nome?")
nome = input()

#print('Seja bem vindo %s' % nome)
print('Seja bem vindo {0}'.format(nome))

print('Qual a sua idade?')
idade = input()
#>>> idade = int(imput('Qual a sua idade? '))

##print('A %s tem %s anos' % (nome, idade))
print('A {0} tem {1} anos'.format(nome, idade))

##print moderno.
print(f'Seja bem vindo(a)  {nome}')

print({2022 - int(idade) + 100})
