# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# - Para homens: (72.7 * h) - 58
# - Para mulheres: (62.1 * h) - 44.7

altura = float(input("Digite a sua altura (em metros): "))

peso_ideal_homens = (72.7 * altura) - 58
peso_ideal_mulheres = (62.1 * altura) - 44.7

print(f"Para uma altura de {altura:.2f} m:")
print(f"- O peso ideal para homens é {peso_ideal_homens:.2f} kg.")
print(f"- O peso ideal para mulheres é {peso_ideal_mulheres:.2f} kg.")
