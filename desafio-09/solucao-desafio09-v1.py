def similarity(s):
    # Inicializa a variável que irá armazenar a soma total das similaridades
    total_similarity = 0
    # Obtém o comprimento da string
    n = len(s)
    
    # Itera sobre cada sufixo da string
    for i in range(n):
        # Obtém o sufixo que começa no índice 'i'
        suffix = s[i:]
        # Inicializa o comprimento do prefixo comum
        common_length = 0
        # Compara a string original com o sufixo atual
        for j in range(len(suffix)):
            # Se os caracteres na mesma posição de ambas as strings são iguais
            if s[j] == suffix[j]:
                # Incrementa o comprimento do prefixo comum
                common_length += 1
            else:
                # Se encontrar um caractere diferente, interrompe a comparação
                break
        # Adiciona o comprimento do prefixo comum ao total de similaridades
        total_similarity += common_length
    
    # Retorna a soma total das similaridades
    return total_similarity

# Testes com assert para verificar se os resultados estão corretos

# Teste 1:
assert similarity("ababaa") == 11, "Teste 1 falhou"

# Teste 2:
assert similarity("aa") == 3, "Teste 2 falhou"

# Teste 3:
assert similarity("abcabccba") == 13, "Teste 3 falhou"

# Teste 4:
assert similarity("eabdcbbeeedbdaebdedbcbdcdeeaebbdbedbdbccbaaeababba") == 63, "Teste 4 falhou"

# Teste 5:
assert similarity("bcdedeccaabdaebdddaeedabedccdddccbbaaadcbbabccbaadbbbeddecacddbababbabadcbbbacecdaee") == 105, "Teste 5 falhou"

# Teste 6:
assert similarity("aeccbdaadbcebddbadbaedeceedbcdaaadcbdebecaddedebccdbadaeed") == 70, "Teste 6 falhou"