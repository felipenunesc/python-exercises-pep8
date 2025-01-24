# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Quanto você ganha por hora: "))
horas_mes = float(input("Número de horas trabalhadas no mês: "))

salario_total = valor_hora * horas_mes

print(f"O total do salário no referido mês é igual a {salario_total:.2f}")
