# Operadores Lógicos em Python

# Definindo variáveis booleanas
a = True
b = False

# Operador lógico AND
resultado_and = a and b
print(f"Operador AND: {a} and {b} => {resultado_and}")

# Operador lógico OR
resultado_or = a or b
print(f"Operador OR: {a} or {b} => {resultado_or}")

# Operador lógico NOT
resultado_not_a = not a
resultado_not_b = not b
print(f"Operador NOT: not {a} => {resultado_not_a}")
print(f"Operador NOT: not {b} => {resultado_not_b}")

# Exemplos práticos
x = 10
y = 5

# Usando operadores lógicos em expressões condicionais
if x > 5 and y < 10:
    print("x é maior que 5 e y é menor que 10")

if x > 5 or y > 10:
    print("x é maior que 5 ou y é maior que 10")

if not (x < 5):
    print("x não é menor que 5")
