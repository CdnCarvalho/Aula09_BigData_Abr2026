import pandas as pd
import numpy as np
import os

os.system('cls')

df_planilha_custos = pd.read_csv('planilha_de_custos.csv')

print('\nDados Obtido')
print(100 * '-')
print(df_planilha_custos.head())


# PREPARANDO OS DADOS
# Criando uma nova coluna
# valor + valor * porcentagem
df_planilha_custos['Custo Total (R$)'] = (
    df_planilha_custos['Preco de Compra (R$)'] + 
    (df_planilha_custos['Preco de Compra (R$)'] * df_planilha_custos['Imposto (%)'] / 100) +
    df_planilha_custos['Frete (R$)'] +
    df_planilha_custos['Taxa Operacional (R$)']
)

print()

print(df_planilha_custos.head())
print()
print(df_planilha_custos[['Produto', 'Custo Total (R$)']].head(10))

# ----------------------------------------------------------------
# Uso da biblioiteca numpy
array_custo_total = np.array(df_planilha_custos['Custo Total (R$)'])
# print(array_custo_total)

print('\nMedidas de Tendência Central')
print(30*"=")
media = np.mean(array_custo_total)
print(f'\nMédia dos Custos: {media:.2f}')

mediana = np.median(array_custo_total)
print(f'\Mediana dos Custos: {mediana}')

# ------------------------------------------------------------------
# quartis
q1 = np.quantile(array_custo_total, 0.25)  # 25%
q2 = np.quantile(array_custo_total, 0.50)  # 50%
q3 = np.quantile(array_custo_total, 0.75)  # 75%

print('\nMedidas de Posição')
print(30*"=")
print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')


# print('\nMenores:')
# print(30*"=")
# print(df_planilha_custos[df_planilha_custos['Custo Total (R$)'] < q1].sort_values(by='Custo Total (R$)', ascending=False))