# Dia 02: Picking Numbers

## Desafio
Este é um desafio de programação cujo objetivo é encontrar a maior subarray de um array de inteiros onde a diferença absoluta entre quaisquer dois elementos seja menor ou igual a 1.

## Detalhamento do Desafio:
1. Crie uma função chamada pickingNumbers que recebe um array de inteiros a como parâmetro.
2. Retorne o comprimento da maior subarray que atende ao critério descrito.

## Exemplo
Dado o array a = [4, 6, 5, 3, 3, 1], as subarrays possíveis que atendem ao critério são [3, 3, 1] e [4, 5, 3, 3]. A subarray [3, 3, 1] tem comprimento 3, que é o máximo possível.

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Arrays e Listas: Entenda como trabalhar com arrays ou listas em sua linguagem de programação preferida.
- Algoritmos de Busca: Aprenda a buscar e comparar elementos dentro de um array.
- Estruturas de Loop: Utilize loops para iterar sobre os elementos do array.

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1: 
- Entrada: a = [4, 6, 5, 3, 3, 1]
- Saída Esperada: 3

### Teste 2: 
- Entrada: a = [1, 2, 2, 3, 1, 2]
- Saída Esperada: 5

### Teste 3: 
Entrada: a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
Saída Esperada: 5

## Dicas Extras:
- A função deve ser capaz de tratar arrays de qualquer tamanho dentro do limite especificado nas restrições.
- Considere o uso de estruturas auxiliares para facilitar o cálculo das subarrays.