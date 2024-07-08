# Desario 04: Notificações de Atividades Suspeitas

## Desafio
O Banco Nacional de HackerLand tem uma política simples para alertar clientes sobre possíveis atividades fraudulentas nas contas. Se o valor gasto por um cliente em um dia específico for maior ou igual ao dobro da mediana dos gastos do cliente para um número de dias anteriores, eles enviam uma notificação ao cliente sobre a possível fraude. O banco não envia nenhuma notificação até que tenham pelo menos esse número de dias de dados de transações anteriores.

Dado o número de dias anteriores e os gastos diários totais de um cliente durante um período de dias, determine quantas vezes o cliente receberá uma notificação durante todos os dias.

## Detalhamento do Desafio:
1. Crie uma função chamada activityNotifications que tem os seguintes parâmetros:
    - int expenditure[n]: despesas diárias
    - int d: os dias de retrospectiva para os gastos médios
2. Retorne o número de notificações enviadas.

## Exemplo
Para os dados de transação de 9 dias e uma retrospectiva de 5 dias com despesas diárias de [2, 3, 4, 2, 3, 6, 8, 4, 5], a saída seria 2. Isso porque:
- Como a retrospectiva deve ser de 5 dias, nada é calculado para os 5 primeiros dias, iniciando apenas no sexto dia
- No sexto dia, as despesas anteriores são [2, 3, 4, 2, 3] com uma mediana de 3. A despesa do dia é 6, que é maior ou igual que 2 * 3, resultando em uma notificação.
- No sétimo dia, as despesas anteriores são [3, 4, 2, 3, 6] com uma mediana de 3. A despesa do dia é 8, que é maior ou igual que 2 * 3, resultando em uma notificação.
- No oitavo dia, as despesas anteriores são [4, 2, 3, 6, 8] com uma mediana de 4. A despesa do dia é 4, que NÃO é maior ou igual que 2 * 4, NÃO resultando em uma notificação.
- No nono dia, as despesas anteriores são [2, 3, 6, 8, 4] com uma mediana de 4. A despesa do dia é 5, que NÃO é maior ou igual que 2 * 4, NÃO resultando em uma notificação.

## Quais conhecimentos eu preciso adquirir para resolver este desafio?
- Loops: Aprenda a iterar sobre uma sequência de números, o que é crucial para verificar os dados da lista.
- Estruturas de Dados: Entenda como trabalhar com listas ou arrays para armazenar dados.
- Algoritmos de Ordenação: Aprenda como ordenar dados para calcular medianas eficientemente.
- Mediana: Entenda o conceito de mediana e como calculá-la em uma lista de números.
- Condições: Aprenda a implementar verificações condicionais (if/else) em sua lógica de programação.

## Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

```
python nome-do-seu-script.py
```

Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

### Teste 1: 
- Entrada: expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5], d = 5
- Saída Esperada: 2

### Teste 2: 
- Entrada: expenditure = [1, 2, 3, 4, 4], d = 4
- Saída Esperada: 0

### Teste 3: 
- Entrada: expenditure = [10, 20, 30, 40, 50, 60, 70, 80, 90], d = 5
- Saída Esperada: 1

### Teste 4: 
- Entrada: expenditure = [1, 2, 100, 2, 2, 2, 2, 2], d = 4
- Saída Esperada: 0

## Dicas Extras:
- Mediana não é a média dos números, procure entender o conceito da mediana e como calculá-la. É bastante simples.
- Existe diferença no calculo da mediana para um conjunto de dados com número par de elementos e para um com número ímpar de elementos.
