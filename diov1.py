""" Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato.
O sistema será desenvolvido para um banco que busca monetizar suas operações.
Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias.
Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes. """


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
n_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Informe o valor de depósito: '))

        if valor <= 0:
            print('Valor inválido')

        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = n_saques >= limite_saques

        if excedeu_saldo:
            print('Saldo insuficiente!')

        elif excedeu_limite:
            print('Saque ultrapassou o limite')

        elif excedeu_saques:
            print('Valor excede limite de transações')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            n_saques += 1

        else:
            print("Valor inválido")

    elif opcao == "e":
        print("\n==================Extrato==================")
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("=============================================")

    elif opcao == "q":
        break

    else:
        print("Opção Invalida")