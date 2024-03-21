import networkx as nx
import matplotlib.pyplot as plt

# Ваша матрица смежности
adjacency_matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
]

# Создайте граф
G = nx.Graph()

# Добавьте ребра и веса из матрицы смежности
for i in range(len(adjacency_matrix)):
    for j in range(i + 1, len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] != 0:
            G.add_edge(i + 1, j + 1, weight=adjacency_matrix[i][j])

# Нарисуйте граф
pos = nx.spring_layout(G)  # Опционально: выберите раскладку для отображения графа
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Найдите минимальное остовное дерево
min_spanning_tree = nx.minimum_spanning_tree(G)

# Нарисуйте минимальное остовное дерево
nx.draw_networkx_edges(min_spanning_tree, pos, edge_color='red', width=2)

plt.show()