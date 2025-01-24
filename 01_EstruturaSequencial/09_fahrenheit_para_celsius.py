# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius

temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
temp_celsius = 5 * ((temp_fahrenheit - 32) / 9)

print(f"A temperatura em °C é igual a {temp_celsius:.2f}°")
