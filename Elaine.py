numeros_pares = []
for numero in range(1, 11):
    # Verifica se o número é par
    if numero % 2 == 0:
        numeros_pares.append(numero)

print("Números pares de 0 até 10 (excluindo o zero):", numeros_pares)
