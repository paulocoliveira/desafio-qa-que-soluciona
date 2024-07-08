# Importa o módulo bisect, que fornece suporte para manter listas em ordem enquanto insere elementos.
import bisect

# Define a função calcular_mediana que recebe uma lista ordenada e o tamanho n da lista.
def calcular_mediana(lista_ordenada, n):
    meio = n // 2  # Calcula a posição do meio na lista.
    if n % 2 == 1:  # Se o tamanho da lista é ímpar, retorna o elemento central diretamente.
        return lista_ordenada[meio]
    else:  # Se o tamanho é par, retorna a média dos dois elementos centrais.
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2

# Define a função activityNotifications que recebe uma lista de despesas e um número de dias para análise.
def activityNotifications(despesas, dias):
    notificacoes = 0  # Inicializa o contador de notificações.
    lista_ordenada = sorted(despesas[:dias])  # Cria uma lista ordenada das primeiras 'dias' despesas.

    for i in range(dias, len(despesas)):  # Inicia um loop a partir do índice 'dias' até o final da lista de despesas.
        # Calcula a mediana da lista ordenada atual.
        mediana = calcular_mediana(lista_ordenada, dias)

        # Verifica se a despesa atual é pelo menos o dobro da mediana e incrementa as notificações se verdadeiro.
        if despesas[i] >= 2 * mediana:
            notificacoes += 1

        # Continua a atualização da lista ordenada se ainda não estamos no último elemento.
        if i < len(despesas) - 1:
            # Insere a nova despesa de forma ordenada na lista.
            bisect.insort(lista_ordenada, despesas[i])
            # Encontra e remove o elemento mais antigo da janela da mediana na lista ordenada.
            elemento_a_remover = despesas[i - dias]
            del lista_ordenada[bisect.bisect_left(lista_ordenada, elemento_a_remover)]

    # Retorna o total de notificações geradas.
    return notificacoes

# Exemplos de uso da função para demonstrar sua funcionalidade.
print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))  # Saída: 2
print(activityNotifications([1, 2, 3, 4, 4], 4))  # Saída: 0
print(activityNotifications([10, 20, 30, 40, 50, 60, 70, 80, 90], 5))  # Saída: 1
print(activityNotifications([1, 2, 100, 2, 2, 2, 2, 2], 4))  # Saída: 0