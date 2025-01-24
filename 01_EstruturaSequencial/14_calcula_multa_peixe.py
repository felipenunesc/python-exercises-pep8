# João Papo-de-Pescador comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Se ele trouxer um peso de peixes maior que o permitido pelo regulamento de pesca do estado de São Paulo (50 quilos),
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# O programa deve calcular o excesso e a multa a ser paga, se houver, e imprimir as informações.

peso_peixe = float(input("Digite o peso do peixe (em kg): "))

limite = 50.0
multa_por_quilo = 4.00
excesso = max(0, peso_peixe - limite)
multa = excesso * multa_por_quilo

if excesso > 0:
    print(f"O peso excedente foi de {excesso:.2f} kg.")
    print(f"João terá que pagar uma multa no valor de R$ {multa:.2f}.")
else:
    print("João não excedeu o limite de peso. Não há multa.")
