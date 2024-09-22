# Operadores de Identidade em Python

# Definindo variáveis
a = [1, 2, 3]
b = a  # b é uma referência ao mesmo objeto que a
c = a[:]  # c é uma cópia de a

# Usando operadores de identidade
print("a:", a)
print("b:", b)
print("c:", c)

# Operador 'is'
print("\nVerificando identidade:")
print(f"a is b: {a is b}")  # True, porque b é o mesmo objeto que a
print(f"a is c: {a is c}")  # False, porque c é uma cópia de a

# Operador 'is not'
print(f"a is not c: {a is not c}")  # True, porque c não é o mesmo objeto que a
print(f"a is not b: {a is not b}")  # False, porque b é o mesmo objeto que a

# Exemplos práticos
x = [1, 2, 3]
y = [1, 2, 3]

print("\nComparando listas:")
print(f"x is y: {x is y}")  # False, porque x e y são objetos diferentes
print(f"x == y: {x == y}")  # True, porque os valores são iguais
