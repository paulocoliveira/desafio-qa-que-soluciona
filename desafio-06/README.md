# Desafio 06: Números Quadrados

## Desafio
Watson gosta de desafiar a habilidade matemática de Sherlock. Ele fornecerá um valor inicial e final que descrevem um intervalo de inteiros, inclusive nos limites. Sherlock deve determinar o número de inteiros quadrados dentro desse intervalo.

Nota: Um inteiro quadrado é um inteiro que é o quadrado de um inteiro, por exemplo, 1 (1²), 4 (2²), 9 (3²), etc.

## Detalhamento do Desafio:
1. Complete a função squares que conta e retorna o número de inteiros quadrados no intervalo inclusivo de a a b. A função possui os seguintes parâmetros:
- int a: o limite inferior do intervalo.
- int b: o limite superior do intervalo.
2. Retorne o número de inteiros quadrados no intervalo

## Exemplo
Entrada: 
- a: 3
- b: 9
Saída:
- 2
Explicação:
No intervalo de 3 a 9, 4 (2²) e 9 (3²) são os dois inteiros quadrados.

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Raiz Quadrada e Potenciação: Aprenda a calcular raízes quadradas e potências de números para identificar inteiros quadrados.
- Laços e Condições: Utilize laços para iterar através de um intervalo e condições para verificar se um número é um quadrado perfeito.
- Matemática Básica: Entenda conceitos de arredondamento e intervalos numéricos.

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1: 
- Entrada: a = 3, b = 9
- Saída Esperada: 2

### Teste 2: 
- Entrada: a = 24, b = 49
- Saída Esperada: 3

### Teste 3: 
- Entrada: a = 17, b = 24
- Saída Esperada: 0

### Teste 4: 
- Entrada: a = 35, b = 70
- Saída Esperada: 3

### Teste 5: 
- Entrada: a = 100, b = 1000
- Saída Esperada: 22

### Teste 6: 
- Entrada: a = 59, b = 999999922
- Saída Esperada: 31615

### Teste 7: 
- Entrada: a = 9, b = 999999966
- Saída Esperada: 31620

### Teste 8: 
- Entrada: a = 12, b = 999999988
- Saída Esperada: 31619

## Dicas Extras:
- Considere usar a função de raiz quadrada e arredondar para baixo para encontrar o primeiro inteiro quadrado possível no intervalo.
- Para otimizar, comece a verificar a partir do quadrado do menor inteiro maior ou igual à raiz quadrada de a até b.