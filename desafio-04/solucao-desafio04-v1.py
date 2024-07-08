# Define a função activityNotifications que recebe uma lista de despesas e um número inteiro 'dias'.
def activityNotifications(despesas, dias):
    # Inicializa o contador de notificações.
    notificacoes = 0

    # Inicia o loop no primeiro dia após ter acumulado 'dias' suficientes para começar a análise.
    for i in range(dias, len(despesas)):
        # Obter os dados das despesas dos últimos 'dias' dias até o dia atual (não incluído).
        dados_antigos = despesas[i-dias:i]
        
        # Ordena os dados para facilitar o cálculo da mediana.
        dados_antigos.sort()
        # Calcula o tamanho da lista ordenada.
        n = len(dados_antigos)
        # Encontra o índice do meio na lista ordenada.
        meio = n // 2
        # Se o tamanho da lista for ímpar, a mediana é o elemento do meio.
        if n % 2 == 1:
            mediana = dados_antigos[meio]
        # Se o tamanho da lista for par, a mediana é a média dos dois elementos do meio.
        else:
            mediana = (dados_antigos[meio - 1] + dados_antigos[meio]) / 2

        # Verifica se a despesa atual é pelo menos o dobro da mediana calculada.
        if despesas[i] >= 2 * mediana:
            # Incrementa o contador de notificações se a condição for verdadeira.
            notificacoes += 1
    
    # Retorna o número total de notificações calculado.
    return notificacoes

# Exemplos de uso da função para verificar a saída e entender seu funcionamento.
print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))  # Saída: 2
print(activityNotifications([1, 2, 3, 4, 4], 4))  # Saída: 0
print(activityNotifications([10, 20, 30, 40, 50, 60, 70, 80, 90], 5))  # Saída: 1
print(activityNotifications([1, 2, 100, 2, 2, 2, 2, 2], 4))  # Saída: 0