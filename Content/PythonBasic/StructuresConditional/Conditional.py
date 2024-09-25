# Sintaxe - IF
 '''
    if condição:
        # código a ser executado se a condição for verdadeira
'''

# Exemplo
numero = 10

if numero > 5:
    print("O número é maior que 5.")

# Sintaxe - ELIF e ELSE
'''
    if condição1:
        # código se condição1 for verdadeira
    elif condição2:
        # código se condição2 for verdadeira
    else:
        # código se nenhuma das condições anteriores for verdadeira
'''

numero = 0

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Operadores de Comparação
a = 5
b = 10

if a < b:
    print("a é menor que b")


# Combinação de Condições
idade = 18
tem_habilitacao = True

if idade >= 18 and tem_habilitacao:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

# Condições Aninhadas
numero = 15

if numero > 10:
    print("O número é maior que 10.")
    if numero % 2 == 0:
        print("E também é par.")
    else:
        print("Mas é ímpar.")
