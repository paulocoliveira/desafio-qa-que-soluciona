# Desafio 02: Contador de Vales

## Desafio
Um ávido caminhante mantém registros meticulosos de suas caminhadas. Durante a última caminhada que durou exatamente N passos, foi registrado se cada passo era uma subida (U) ou uma descida (D). As caminhadas sempre começam e terminam ao nível do mar, e cada passo para cima ou para baixo representa uma mudança de uma unidade de altitude. Definimos os seguintes termos:

Uma montanha é uma sequência de passos consecutivos acima do nível do mar, começando com um passo para cima do nível do mar e terminando com um passo para baixo até o nível do mar.
Um vale é uma sequência de passos consecutivos abaixo do nível do mar, começando com um passo para baixo do nível do mar e terminando com um passo para cima até o nível do mar.
Dado a sequência de passos de subida e descida durante uma caminhada, descubra e imprima o número de vales percorridos.

## Detalhamento do Desafio:
1. Crie uma função chamada countingValleys que recebe uma string como parâmetro para representar o caminho percorrido.
2. Retorne o número de vales atravessados.

## Exemplo
Dado a string UDDDUDUU, o número de vales percorridos foi 1.

Se representarmos o nível do mar com _, um passo para cima como / e um passo para baixo como \, a caminhada pode ser desenhada como:

```
_/\      _
   \    /
    \/\/
```

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Strings: Aprenda a manipular strings em Python, pois você precisará iterar sobre cada caractere da string.
- Estruturas de Loop: Utilize loops para iterar sobre os caracteres da string de caminho.

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1: 
- Entrada: path = "DDUUDDUDUUUD"
- Saída Esperada: 2

### Teste 2: 
- Entrada: path = "UDUUUDUDDD"
- Saída Esperada: 0

### Teste 3: 
Entrada: path = 'DUDUDUDUDUDUDU"
Saída Esperada: 7

### Teste 4: 
Entrada: path = 'DDUUUUDDDUUUDDDU"
Saída Esperada: 3

## Dicas Extras:
- Use um contador de altitude
- Marque o início e o fim dos vales