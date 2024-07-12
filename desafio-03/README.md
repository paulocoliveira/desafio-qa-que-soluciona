# Desafio 03: Dias Belos

## Desafio
Lily gosta de jogar com números. Ela criou um novo jogo onde determina a diferença entre um número e seu inverso. Por exemplo, dado o número 123, seu inverso é 321. A diferença entre eles é 198. O número 120 revertido é 21, e sua diferença é 99.

Ela decidiu aplicar seu jogo para tomar decisões. Ela olhará para um intervalo numerado de dias e só irá ao cinema em um "dia belo".

Dado um intervalo de dias numerados, i e j, e um número k, determine o número de dias no intervalo que são belos. Números belos são definidos como números onde a diferença entre o número e seu inverso é divisível por k. Se o valor de um dia é um número belo, então é um dia belo. Retorne o número de dias belos no intervalo.

## Detalhamento do Desafio:
1. Crie uma função chamada beautifulDays que tem os seguintes parâmetros:
    int i: o número do dia inicial
    int j: o número do dia final
    int k: o divisor
2. Retorne o número de dias belos no intervalo entre i e j.

## Exemplo
Dado i = 20, j = 23 e k = 6, a saída seria 2, pois existem apenas 2 dias belos entre os dias 20 e 23.

Exmplicação:
- Dia 20 é belo porque a seguinte avaliação resulta em um número inteiro: (20 - 2) / 6 = 3
- Dia 21 não é belo porque a seguinte avaliação não resulta em um número inteiro: (21 - 12) / 6 = 1.5
- Dia 22 é belo porque a seguinte avaliação resulta em um número inteiro: (22 - 22) / 6 = 0
- Dia 23 não é belo porque a seguinte avaliação não resulta em um número inteiro: (23 - 32) / 6 = -1.5

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Manipulação de Strings e Números: Aprenda a converter números em strings e vice-versa para poder inverter os números.
- Divisibilidade e Operações Matemáticas: Aprenda a usar operações matemáticas básicas e entender o conceito de divisibilidade.
- Loops: Aprenda a iterar sobre uma sequência de números, o que é crucial para verificar cada dia no intervalo dado.

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1: 
- Entrada: i=20, j=23, k=6
- Saída Esperada: 2

### Teste 2: 
- Entrada: i=13, j=45, k=3
- Saída Esperada: 33

### Teste 3: 
- Entrada: i=1, j=2000000, k=2000000
Saída Esperada: 2998

### Teste 4: 
- Entrada: i=1, j=2000000, k=23047885
Saída Esperada: 2998

## Dicas Extras:
- Considere escrever uma função auxiliar para reverter o número e calcular a diferença.
- Lembre-se de verificar cada dia no intervalo usando um loop e incrementar sua contagem de dias belos conforme necessário.