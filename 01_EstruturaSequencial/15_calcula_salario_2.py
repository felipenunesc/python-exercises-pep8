# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre:
# - Salário bruto.
# - Quanto pagou ao INSS.
# - Quanto pagou ao sindicato.
# - O salário líquido, considerando os descontos de:
#   * 11% para o Imposto de Renda,
#   * 8% para o INSS,
#   * 5% para o sindicato.

valor_hora = float(input("Quanto você ganha por hora: "))
horas_mes = float(input("Número de horas trabalhadas no mês: "))

# Cálculo do salário bruto
salario_bruto = valor_hora * horas_mes

# Descontos
desconto_ir = salario_bruto * 0.11
valor_inss = salario_bruto * 0.08
valor_sindicato = salario_bruto * 0.05

# Salário líquido
salario_liquido = salario_bruto - (desconto_ir + valor_inss + valor_sindicato)

# Exibindo os resultados
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do Imposto de Renda (11%): R$ {desconto_ir:.2f}")
print(f"Valor pago ao INSS (8%): R$ {valor_inss:.2f}")
print(f"Valor pago ao sindicato (5%): R$ {valor_sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
