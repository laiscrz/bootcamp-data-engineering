# Sintaxe - WHILE
'''while condição:
    # código a ser executado enquanto a condição for verdadeira'''


contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementa o contador

# Condições e Saída do Loop
contador = 10

while contador < 5:
    print("Contador:", contador)  # Este código não será executado
    contador += 1


# Interromper Loop
contador = 0

while True:  # Loop infinito
    print("Contador:", contador)
    contador += 1
    if contador >= 5:
        break  # Sai do loop quando contador é maior ou igual a 5


# Continuando a Próxima Iteração
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue  # Pula a iteração quando contador é igual a 3
    print("Contador:", contador)


# Evite loops infinitos
contador = 0

while contador < 5:
    print("Contador:", contador)
    # Falta o incremento do contador


# Condicionais com while
numero = 0

while numero < 5:
    numero += 1
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é ímpar")
