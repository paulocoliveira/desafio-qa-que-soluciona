def staircase(n):
    # Utiliza list comprehension e o método join para criar a escada
    print('\n'.join(' ' * (n - i) + '#' * i for i in range(1, n + 1)))

# Testes da função
staircase(2)
staircase(7)
staircase(20)
