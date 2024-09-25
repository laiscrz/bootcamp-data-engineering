# Sintaxe - FOR
''' 
    for variável in sequência:
        # código a ser executado para cada item na sequência
'''

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print("Fruta:", fruta)


#  Iterando com range()
for i in range(5):  # Gera números de 0 a 4
    print("Número:", i)


# Usando for em Strings
texto = "Python"

for letra in texto:
    print("Letra:", letra)


# Iterando sobre Dicionários
dados = {"nome": "Alice", "idade": 30}

# Iterando sobre chaves
for chave in dados:
    print("Chave:", chave)

# Iterando sobre valores
for valor in dados.values():
    print("Valor:", valor)

# Iterando sobre itens
for chave, valor in dados.items():
    print(f"{chave}: {valor}")


# List Comprehensions
quadrados = [x**2 for x in range(10)]
print("Quadrados:", quadrados)


# Usando break e continue no for

for i in range(10):
    if i == 5:
        break  # Sai do loop quando i é igual a 5
    print("Número:", i)


for i in range(5):
    if i % 2 == 0:
        continue  # Pula os números pares
    print("Número ímpar:", i)
