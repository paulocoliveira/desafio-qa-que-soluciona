import math

def encryption(s):
    # Calcula a raiz quadrada do tamanho da string e determina os inteiros ao redor dela
    size = len(s)
    sqrt_size = math.sqrt(size)
    row = math.floor(sqrt_size)
    column = math.ceil(sqrt_size)

    # Verifica se a multiplicação de row e column é suficiente, senão ajusta
    if row * column < size:
        row += 1

    # Divide a string em partes de tamanho column
    parts = []
    for i in range(0, len(s), column):
        parts.append(s[i:i + column])

    # Constrói a string final pegando caracteres de cada coluna
    encrypted = []
    for col in range(column):
        col_chars = ''
        for row in range(len(parts)):
            if col < len(parts[row]):
                col_chars += parts[row][col]
        encrypted.append(col_chars)

    return ' '.join(encrypted)

# Testes
assert encryption("haveaniceday") == "hae and via ecy", "Teste falhou para 'haveaniceday'"
assert encryption("feedthedog") == "fto ehg ee dd", "Teste falhou para 'feedthedog'"
assert encryption("chillout") == "clu hlt io", "Teste falhou para 'chillout'"
assert encryption("iuo") == "io u", "Teste falhou para 'iuo'"
assert encryption("wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny") == \
       "wmgjpnull cyjqlejgi lyhhdzbui wctlsqsbm fxeoxmsvv ovxjeirfm zadysxbhn nxkkbffpn bawobphfy", \
       "Teste falhou para a string longa"