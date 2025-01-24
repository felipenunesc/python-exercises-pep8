# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit

temp_celsius = float(input("Digite a temperatura em °C: "))
temp_fahrenheit = temp_celsius * 9 / 5 + 32

print(f"A temperatura em °F é igual a {temp_fahrenheit:.2f}°")
