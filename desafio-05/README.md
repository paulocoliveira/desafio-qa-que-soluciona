# Desafio 05: Horas em Palavras

## Desafio
Dado um horário em numerais, podemos convertê-lo em palavras, como mostrado nos exemplos abaixo. Este programa visa converter um horário dado no formato de horas e minutos para a sua representação em palavras:

5:00 → five o' clock
5:01 → one minute past five
5:10 → ten minutes past five
5:15 → quarter past five
5:30 → half past five
5:40 → twenty minutes to six
5:45 → quarter to six
5:47 → thirteen minutes to six
5:28 → twenty eight minutes past five

## Detalhamento do Desafio:
1. Complete a função timeInWords que converte a hora dada em palavras seguindo as convenções de tempo acima descritas. A função possui os seguintes parâmetros:
    - int h: a hora do dia.
    - int m: os minutos após a hora.
2. Retorne o as horas em texto.

## Exemplo
Entrada: 
- Hora: 5
- Minutos: 47
Saída:
- thirteen minutes to six
Explicação:
47 minutos são traduzidos como "thirteen minutes to six" porque 60 - 47 = 13, e usamos "to" para indicar que está se aproximando da próxima hora.

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Estruturas Condicionais: Use estruturas de decisão para aplicar diferentes regras baseadas no valor dos minutos.
- Manipulação de Strings: Construa strings dinâmicas baseadas nas condições dadas.
- Conversão de Números para Palavras: Converta números inteiros em suas representações textuais por extenso.

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1: 
- Entrada: h = 5, m = 0
- Saída Esperada: five o' clock

### Teste 2: 
- Entrada: h = 5, m = 1
- Saída Esperada: one minute past five

### Teste 3: 
- Entrada: h = 5, m = 10
- Saída Esperada: ten minutes past five

### Teste 4: 
- Entrada: h = 5, m = 15
- Saída Esperada: quarter past five

### Teste 5: 
- Entrada: h = 5, m = 28
- Saída Esperada: twenty eight minutes past five

### Teste 6: 
- Entrada: h = 5, m = 30
- Saída Esperada: half past five

### Teste 7: 
- Entrada: h = 5, m = 40
- Saída Esperada: twenty minutes to six

### Teste 8: 
- Entrada: h = 5, m = 45
- Saída Esperada: quarter to six

### Teste 9: 
- Entrada: h = 5, m = 47
- Saída Esperada: thirteen minutes to six

## Dicas Extras:
- Considere criar um dicionário para mapear todos os números até 59 para suas respectivas palavras, incluindo termos especiais como "quarter" e "half".
- Ajuste a hora para a próxima se os minutos forem superiores a 30, e considere o caso especial de transição de "12" para "1".