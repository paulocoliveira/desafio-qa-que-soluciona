def staircase(n):
    i = 1
    while i <= n:
        # Calcula quantos espaços e '#' são necessários
        spaces = ' ' * (n - i)
        hashes = '#' * i
        # Combina espaços e '#' em uma linha e imprime
        print(spaces + hashes)
        i += 1

# Teste da função
staircase(2)
staircase(7)
staircase(20)
