import math

def squares(a, b):
    # Calcula o menor inteiro x tal que x^2 é maior ou igual a 'a'
    start = math.ceil(math.sqrt(a))
    # Calcula o maior inteiro x tal que x^2 é menor ou igual a 'b'
    end = math.floor(math.sqrt(b))

    # O número de inteiros quadrados perfeitos é dado pela diferença entre 'end' e 'start' mais 1
    # Se 'end' for maior ou igual a 'start'
    if start <= end:
        return end - start + 1
    else:
        return 0

print(squares(3, 9)) # 2
print(squares(24, 49)) # 3
print(squares(17, 24))# 0
print(squares(35, 70)) # 3
print(squares(100, 1000)) # 22
print(squares(59, 999999922)) # 31615
print(squares(9, 999999966)) # 31620
print(squares(12, 999999988)) # 31619