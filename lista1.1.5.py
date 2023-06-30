"""
Lista 1, parte 1, exercício 5

Descrição: Este programa apresenta a resolução de uma questão da lista 1 da cadeira de Economia Computacional
Autor:Arthur Kafrouni Tomazi
Data: 23/06/2023
Versão: 0.0.1
"""

# Atribuição de variáveis

horas = 0
sal_bruto = 0
sal_liq = 0
descontos_nominal = 0
desconto_per = 0.3
hora_aula = 40

# Entrada de dados

horas = float(input("Número de horas trabalhadas: "))

# Processamento de dados

sal_bruto = horas * hora_aula
descontos_nominal = sal_bruto * desconto_per
sal_liq = sal_bruto - descontos_nominal

# Saída de dados

print(f'O professor recebeu um salário bruto de {sal_bruto}, com descontos de {descontos_nominal} que levaram a um salário líquido de {sal_liq} pelas {horas} horas trabalhadas')