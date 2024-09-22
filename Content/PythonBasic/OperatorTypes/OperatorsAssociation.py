# Operadores de Associação em Python

# Definindo uma lista e um dicionário
fruits = ['apple', 'banana', 'cherry']
fruit_dict = {
    'apple': 5,
    'banana': 3,
    'cherry': 7
}

# Usando o operador 'in' para listas
print("Verificando se 'banana' está na lista de frutas:")
if 'banana' in fruits:
    print("'banana' está na lista.")
else:
    print("'banana' não está na lista.")

# Usando o operador 'not in' para listas
print("\nVerificando se 'orange' está na lista de frutas:")
if 'orange' not in fruits:
    print("'orange' não está na lista.")
else:
    print("'orange' está na lista.")

# Usando o operador 'in' para dicionários
print("\nVerificando se 'cherry' é uma chave no dicionário de frutas:")
if 'cherry' in fruit_dict:
    print("'cherry' é uma chave no dicionário.")
else:
    print("'cherry' não é uma chave no dicionário.")

# Usando o operador 'not in' para dicionários
print("\nVerificando se 'grape' é uma chave no dicionário de frutas:")
if 'grape' not in fruit_dict:
    print("'grape' não é uma chave no dicionário.")
else:
    print("'grape' é uma chave no dicionário.")
