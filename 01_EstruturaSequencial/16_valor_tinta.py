# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.

import math

# Entrada do tamanho da área a ser pintada
area_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Cálculo da quantidade de tinta necessária
litros_necessarios = area_pintada / 3
latas_comprar = math.ceil(litros_necessarios / 18)  # Arredonda para cima, pois não é possível comprar meia lata

# Cálculo do custo total
preco_total = latas_comprar * 80.00

# Exibição dos resultados
print(f"Você precisará de {latas_comprar} lata(s) de tinta.")
print(f"O custo total será de R$ {preco_total:.2f}.")
