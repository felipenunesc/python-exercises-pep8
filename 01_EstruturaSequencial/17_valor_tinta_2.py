# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida:
# - Em latas de 18 litros, que custam R$ 80,00.
# - Em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta e os respectivos preços em 3 situações:
# 1. Comprar apenas latas de 18 litros.
# 2. Comprar apenas galões de 3,6 litros.
# 3. Misturar latas e galões para minimizar o desperdício.

import math

# Entrada do tamanho da área a ser pintada
area_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Adicionar 10% de folga
area_com_folga = area_pintada * 1.10

# Calcular a quantidade total de tinta necessária (em litros)
litros_necessarios = area_com_folga / 6

# Situação 1: Apenas latas de 18 litros
latas_18 = math.ceil(litros_necessarios / 18)
custo_latas_18 = latas_18 * 80.00

# Situação 2: Apenas galões de 3,6 litros
galoes_3_6 = math.ceil(litros_necessarios / 3.6)
custo_galoes_3_6 = galoes_3_6 * 25.00

# Situação 3: Misturar latas e galões
latas_mistura = int(litros_necessarios / 18)  # Latas completas
resto_tinta = litros_necessarios - (latas_mistura * 18)  # Restante em litros
galoes_mistura = math.ceil(resto_tinta / 3.6)  # Galões para o restante
custo_mistura = (latas_mistura * 80.00) + (galoes_mistura * 25.00)

# Exibição dos resultados
print("\nResultados:")
print(f"1. Apenas latas de 18 litros:")
print(f"   - Quantidade: {latas_18} lata(s)")
print(f"   - Custo total: R$ {custo_latas_18:.2f}")

print(f"\n2. Apenas galões de 3,6 litros:")
print(f"   - Quantidade: {galoes_3_6} galão(ões)")
print(f"   - Custo total: R$ {custo_galoes_3_6:.2f}")

print(f"\n3. Mistura de latas e galões:")
print(f"   - Latas de 18 litros: {latas_mistura}")
print(f"   - Galões de 3,6 litros: {galoes_mistura}")
print(f"   - Custo total: R$ {custo_mistura:.2f}")
