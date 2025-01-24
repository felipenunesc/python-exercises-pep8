# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#  - O produto do dobro do primeiro com metade do segundo .
#  - A soma do triplo do primeiro com o terceiro.
#  - O terceiro elevado ao cubo.

num_1_int = int(input("Digite o primeiro número inteiro: "))
num_2_int = int(input("Digite o segundo número inteiro: "))
num_3_real = float(input("Digite um número real: "))

produto_dobro_metade = (num_1_int * 2) * (num_2_int / 2)
soma_triplo_terceiro = (num_1_int * 3) + num_3_real
cubo_terceiro = num_3_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {produto_dobro_metade:.2f}")
print(f"A soma do triplo do primeiro com o terceiro: {soma_triplo_terceiro:.2f}")
print(f"O terceiro elevado ao cubo: {cubo_terceiro:.2f}")
