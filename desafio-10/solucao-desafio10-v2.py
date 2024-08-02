import heapq

def shortestReach(n, edges, s):
    # Inicializa o grafo como um dicionário onde cada nó tem uma lista de adjacências vazia
    graph = {i: [] for i in range(1, n + 1)}
    
    # Popula o grafo com as arestas fornecidas
    for u, v, w in edges:
        graph[u].append((v, w))  # Adiciona a aresta do nó u ao nó v com peso w
        graph[v].append((u, w))  # Adiciona a aresta do nó v ao nó u com peso w (grafo não direcionado)

    # Inicializa as distâncias como infinito para todos os nós, exceto para o nó inicial s
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[s] = 0  # A distância do nó inicial para ele mesmo é 0
    
    # Inicializa a fila de prioridade com o nó inicial
    pq = [(0, s)]  # (distância, nó)

    # Processa os nós na fila de prioridade
    while pq:
        # Remove o nó com a menor distância da fila
        current_distance, u = heapq.heappop(pq)

        # Se a distância atual for maior que a distância registrada, continue (nó já processado)
        if current_distance > distances[u]:
            continue

        # Atualiza as distâncias para os vizinhos do nó atual
        for neighbor, weight in graph[u]:
            distance = current_distance + weight  # Calcula a nova distância

            # Se a nova distância for menor, atualiza a distância e adiciona o vizinho à fila
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # Prepara a saída formatada
    output = []
    for i in range(1, n + 1):
        if i != s:
            # Adiciona a distância ao nó na saída, ou -1 se o nó não for alcançável
            output.append(str(distances[i] if distances[i] != float('inf') else -1))

    # Retorna a saída como uma string de distâncias separadas por espaço
    return ' '.join(output)

def test_1():
    n = 4
    edges = [
        (1, 2, 24),
        (1, 4, 20),
        (3, 1, 3),
        (4, 3, 12)
    ]
    s = 1
    expected_output = "24 3 15"
    
    output = shortestReach(n, edges, s)
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

def test_2():
    n = 5
    edges = [
        (1, 2, 10),
        (1, 3, 6),
        (2, 4, 8)
    ]
    s = 2
    expected_output = "10 16 8 -1"
    
    output = shortestReach(n, edges, s)
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

def test_3():
    n = 6
    edges = [
        (1, 2, 7),
        (1, 3, 9),
        (1, 6, 14),
        (2, 3, 10),
        (2, 4, 15),
        (3, 4, 11),
        (3, 6, 2),
        (4, 5, 6),
        (5, 6, 9)
    ]
    s = 1
    expected_output = "7 9 20 20 11"
    
    output = shortestReach(n, edges, s)
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

def test_4():
    n = 3
    edges = [
        (1, 2, 1),
        (2, 3, 1)
    ]
    s = 1
    expected_output = "1 2"
    
    output = shortestReach(n, edges, s)
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

def test_5():
    n = 4
    edges = [
        (1, 2, 1),
        (2, 3, 2),
        (3, 4, 3)
    ]
    s = 2
    expected_output = "1 2 5"
    
    output = shortestReach(n, edges, s)
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

# Executar os testes
test_1()
test_2()
test_3()
test_4()
test_5()