# Desafio 09: Similaridade de Sufixos

## Desafio
Para duas strings A e B, definimos a similaridade das strings como o comprimento do prefixo mais longo comum a ambas as strings. Por exemplo, a similaridade das strings "abc" e "abd" é 2, enquanto a similaridade das strings "aaa" e "aaab" é 3.

Neste desafio, você deve calcular a soma das similaridades de uma string S com cada um de seus sufixos.

## Detalhamento do Desafio:
1. Crie uma função chamada similarity que tem os seguintes parâmetros:
- string s: uma string para calcular a similaridade com seus sufixos.
2. Retorne a soma das similaridades como um inteiro.
- int: soma das similaridades.

## Exemplo
Entrada: 
- s = "ababaa"
Saída:
- 11

Explicação:
Os sufixos da string "ababaa" são gerados removendo um caractere por vez, começando do início. Aqui estão os sufixos e como suas similaridades com a string original "ababaa" são calculadas:

1. Sufixo: "ababaa"
- Comparação com "ababaa": O sufixo é a string completa.
- Similaridade: 6 (completa), pois todos os caracteres correspondem.

2. Sufixo: "babaa"
- Comparação com "ababaa": Começa com 'b', enquanto "ababaa" começa com 'a'.
- Similaridade: 0, pois não há prefixo comum.

3. Sufixo: "abaa"
- Comparação com "ababaa": Os primeiros três caracteres 'aba' são comuns.
- Similaridade: 3, corresponde a 'aba'.

4. Sufixo: "baa"
- Comparação com "ababaa": Começa com 'b', enquanto "ababaa" começa com 'a'.
- Similaridade: 0, pois não há prefixo comum.

5. Sufixo: "aa"
- Comparação com "ababaa": Os últimos dois caracteres 'aa' são comuns, aparecendo também como o quinto e sexto caracteres de "ababaa".
- Similaridade: 1, corresponde ao último 'a'.

6. Sufixo: "a"
- Comparação com "ababaa": O último caractere 'a' é comum, aparecendo também como o primeiro, terceiro e sexto caracteres de "ababaa".
- Similaridade: 1, corresponde ao último 'a'.

Cálculo da Resposta:
Somando as similaridades dos sufixos, obtemos:

6(ababaa) + 0(babaa) + 3(abaa) + 0(baa) + 1(aa) + 1(a) = 11

Essa soma resulta em uma resposta total de 11 para a similaridade da string "ababaa" com todos os seus sufixos.

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Manipulação de Strings: Aprenda a trabalhar com sufixos de strings e a identificar prefixos comuns.

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1:
- Entrada: "ababaa"
- Saída Esperada: 11

### Teste 2:
- Entrada: "aa"
- Saída Esperada: 3

### Teste 3:
- Entrada: "abcabccba"
- Saída Esperada: 13

### Teste 4:
- Entrada: "eabdcbbeeedbdaebdedbcbdcdeeaebbdbedbdbccbaaeababba"
- Saída Esperada: 63

### Teste 5:
- Entrada: "bcdedeccaabdaebdddaeedabedccdddccbbaaadcbbabccbaadbbbeddecacddbababbabadcbbbacecdaee"
- Saída Esperada: 105

### Teste 6:
- Entrada: "aeccbdaadbcebddbadbaedeceedbcdaaadcbdebecaddedebccdbadaeed"
- Saída Esperada: 70

## Dicas Extras:
- Utilize técnicas de cache para armazenar resultados de cálculos de similaridade para sufixos comuns a fim de evitar recalculações desnecessárias.