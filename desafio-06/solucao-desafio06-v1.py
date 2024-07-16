import math

def squares(a, b):
    # Inicia o contador de quadrados perfeitos
    count = 0

    # Inicia com o menor número inteiro (1)
    i = 1

    # Continua enquanto o quadrado de i for menor ou igual a b
    while i * i <= b:
        # Se o quadrado de i for maior ou igual a 'a' e menor ou igual a 'b', é um quadrado perfeito no intervalo
        if i * i >= a:
            count += 1
        # Incrementa i para verificar o próximo número
        i += 1
    
    return count

print(squares(3, 9)) # 2
print(squares(24, 49)) # 3
print(squares(17, 24))# 0
print(squares(35, 70)) # 3
print(squares(100, 1000)) # 22
print(squares(59, 999999922)) # 31615
print(squares(9, 999999966)) # 31620
print(squares(12, 999999988)) # 31619