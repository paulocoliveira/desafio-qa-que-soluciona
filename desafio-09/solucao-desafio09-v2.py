def similarity(s):
    n = len(s)
    total_similarity = 0
    memo = {}

    def common_prefix_length(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        length = 0
        while i < n and j < n and s[i] == s[j]:
            length += 1
            i += 1
            j += 1
        memo[(i, j)] = length
        return length

    for i in range(n):
        total_similarity += common_prefix_length(0, i)

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