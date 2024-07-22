import math

def calculate_dimensions(size):
    """Calcula as dimensões ideais para a grade com base no tamanho da entrada."""
    sqrt_size = math.sqrt(size)
    rows = math.floor(sqrt_size)
    cols = math.ceil(sqrt_size)
    if rows * cols < size:
        rows += 1
    return rows, cols

def create_grid(s, cols):
    """Cria uma grade com as strings divididas em número definido de colunas."""
    return [s[i:i + cols] for i in range(0, len(s), cols)]

def encrypt_columns(parts, cols, rows):
    """Lê as colunas da grade criada para formar a string criptografada."""
    encrypted = []
    for col in range(cols):
        col_chars = ''.join(part[col] if col < len(part) else '' for part in parts)
        if col_chars:
            encrypted.append(col_chars)
    return ' '.join(encrypted)

def encryption(s):
    """Função principal que gerencia o processo de criptografia da string."""
    size = len(s)
    rows, cols = calculate_dimensions(size)
    parts = create_grid(s, cols)
    return encrypt_columns(parts, cols, rows)

# Testes
assert encryption("haveaniceday") == "hae and via ecy", "Teste falhou para 'haveaniceday'"
assert encryption("feedthedog") == "fto ehg ee dd", "Teste falhou para 'feedthedog'"
assert encryption("chillout") == "clu hlt io", "Teste falhou para 'chillout'"
assert encryption("iuo") == "io u", "Teste falhou para 'iuo'"
assert encryption("wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny") == \
       "wmgjpnull cyjqlejgi lyhhdzbui wctlsqsbm fxeoxmsvv ovxjeirfm zadysxbhn nxkkbffpn bawobphfy", \
       "Teste falhou para a string longa"