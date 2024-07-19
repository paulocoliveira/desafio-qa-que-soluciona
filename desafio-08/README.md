# Desafio 08: Criptografia de Texto

## Desafio
Um texto em inglês precisa ser criptografado usando o seguinte esquema de criptografia Primeiro, os espaços são removidos do texto. Seja L o comprimento deste texto. Em seguida, os caracteres são escritos em uma grade, cujas linhas e colunas têm as seguintes restrições:

Se L for o comprimento da string sem espaços, então a grade deve ter floor(L) linhas e ceil(L) colunas, onde o número de linhas deve ser menor ou igual ao número de colunas e a área da grade (linhas x colunas) deve ser mínima, mas ainda capaz de conter L caracteres. A mensagem codificada é obtida exibindo os caracteres de cada coluna, com um espaço entre os textos das colunas.

## Detalhamento do Desafio:
1. Crie uma função chamada encryption que tem os seguintes parâmetros:
- string s: uma string para criptografar.
2. Retorne a string criptografada.
- string: a string criptografada.

## Exemplo
Entrada: 
- s = "haveaniceday"
Saída:
- "hae and via ecy"

Explicação:
- O comprimento L da string após remover espaços é 12.
- Calculamos a raiz quadrada de 12 que é aproximadamente 3.46
- Para determinar as dimensões da grade, buscamos os inteiros mais próximos para as linhas e colunas: Número de linhas (raiz quadrada de L arredondada para baixo), Número de colunas (raiz quadrada de L arredondado para cima).
- Com base nas dimensões calculadas (3 linhas e 4 colunas), a string é dividida da seguinte forma:
```
have
anic
eday
```
Cada linha contém sequencialmente os caracteres da string original até que todos os caracteres sejam alocados na grade.

- A mensagem criptografada é formada lendo os caracteres de cada coluna da grade formada, começando pela primeira coluna e movendo-se para a direita até a última coluna.
Primeira coluna: "h", "a", "e" → "hae"
Segunda coluna: "a", "n", "d" → "and"
Terceira coluna: "v", "i", "a" → "via"
Quarta coluna: "e", "c", "y" → "ecy"
Os grupos de caracteres de cada coluna são então combinados com um espaço entre eles para formar a mensagem criptografada final.


## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Manipulação de Strings: Aprenda a manipular strings, incluindo como remover espaços, acessar caracteres individuais, e dividir strings em substrings. Essas habilidades são cruciais para preparar a string para o processo de criptografia e para ler colunas de caracteres de uma grade.
- Conceitos de Matemática e Raiz Quadrada: Entenda como calcular a raiz quadrada de um número para determinar as dimensões ideais da grade de criptografia. Isso envolve o uso das funções matemáticas floor e ceil para arredondar números para o inteiro mais próximo apropriado, garantindo que o número de linhas e colunas seja otimizado para o comprimento da string.
- Estruturas de Dados para Armazenamento: Familiarize-se com o uso de listas (arrays) para armazenar dados temporariamente. No contexto deste desafio, você precisará criar e manipular uma lista para armazenar os caracteres em um formato de grade.

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1:
- Entrada: "haveaniceday"
- Saída Esperada: "hae and via ecy"

### Teste 2:
- Entrada: "feedthedog"
- Saída Esperada: "fto ehg ee dd"

### Teste 3:
- Entrada: "chillout"
- Saída Esperada: "clu hlt io"
### Teste 4:
- Entrada: "iuo"
- Saída Esperada: "io u"
### Teste 5:
- Entrada: "wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny"
- Saída Esperada: "wmgjpnull cyjqlejgi lyhhdzbui wctlsqsbm fxeoxmsvv ovxjeirfm zadysxbhn nxkkbffpn bawobphfy"

## Dicas Extras:
- Calcule a quantidade de linhas e colunas baseando-se na raiz quadrada do comprimento da string após remover espaços.
- Remova espaços antes de criar a matriz de caracteres.
- Utilize loops para ler os caracteres verticalmente para formar a mensagem codificada.