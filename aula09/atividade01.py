import random
import os 


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplica(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return 'Operação Inválida'

    return a / b



# início
os.system('cls')

# n1 = float(input('Informe o número: '))
# n2 = float(input('Informe outro número: '))

n1 = random.randint(11, 100)
n2 = random.randint(1, 10)

print(f'Primeiro Número: {n1}')
print(f'Segundo Número: {n2}')

# os.system('cls')
print('\nEscolha uma opção: ')
print('[1] - Somar')
print('[2] - Subtrair')
print('[3] - Multiplicar')
print('[4] - Dividir')

opcao = int(input('Opção escolhida: '))
match opcao:
    case 1:
        print('\nSoma')
        print(f'Resultado: {soma(n1, n2)}')
    case 2:
        print('\nSubtração')
        print(f'Resultado: {subtracao(n1, n2)}')
    case 3:
        print('\nMultiplicação')
        print(f'Resultado: {multiplica(n1, n2)}')
    case 4:
        print('\nDividir')
        print(f'Resultado: {dividir(n1, n2)}')
    case _:
        print('Opção Inválida!')
