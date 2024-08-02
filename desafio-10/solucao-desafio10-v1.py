
def shortestReach(n, edges, s):
    # Inicializar o grafo como um dicionário de listas
    graph = {i: [] for i in range(1, n + 1)}
    
    # Adicionar cada aresta ao grafo
    for u, v, w in edges:
        graph[u].append((v, w))  # Adicionar a aresta de u para v com peso w
        graph[v].append((u, w))  # Adicionar a aresta de v para u com peso w porque o grafo é não direcionado

    # Inicializar distâncias com infinito e definir a distância do nó inicial como 0
    distances = [float('inf')] * (n + 1)  # Cria uma lista de distâncias com tamanho n + 1, inicializada com infinito
    distances[s] = 0  # Define a distância do nó inicial s como 0
    
    # Inicializar o conjunto de visitados
    visited = [False] * (n + 1)  # Cria uma lista de nós visitados com tamanho n + 1, inicializada com False

    # Para cada nó no grafo
    for _ in range(n):
        # Encontrar o nó não visitado com a menor distância
        min_distance = float('inf')
        min_node = -1
        for i in range(1, n + 1):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_node = i

        # Se não encontrar nenhum nó, sair do loop
        if min_node == -1:
            break

        # Marcar o nó como visitado
        visited[min_node] = True

        # Atualizar as distâncias dos vizinhos do nó atual
        for neighbor, weight in graph[min_node]:
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node] + weight

    # Preparar a saída, excluindo o nó inicial
    result = []
    for i in range(1, n + 1):
        if i != s:
            # Adicionar a distância ao resultado ou -1 se o nó não for alcançável
            result.append(str(distances[i] if distances[i] != float('inf') else -1))

    # Retornar a saída como uma string de distâncias separadas por espaços
    return ' '.join(result)


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