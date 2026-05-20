from auxiliar.operacoes import dobro, triplo, quadrado
# def dobro(n):
#     d = n * 2
#     return d


# def triplo(n):
#     t = n * 3
#     return t


# def quadrado(n):
#     q = n ** 2
#     return q


# início
num = int(input('Informe o número: '))

print('\n ##### MENU DE OPÇÕES #####')
print(30 * '=')

print('[1] - Dobro\n[2] - Triplo\n[3] - Quadrado')
opcao = int(input('\nInforme a sua opção: '))

match opcao:
    case 1:
        resultado = dobro(num)
    case 2:
        resultado = triplo(num)
    case 3:
        resultado = quadrado(num)
    case _:
        print('Opção Inválida')


print(f'Resultado: {resultado}')



