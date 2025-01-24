# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

for e in range(4):
    notas.append(float(input(f"Digite a {e+1}° nota: ")))

media = sum(notas) / len(notas)

print(media)