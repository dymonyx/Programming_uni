import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(adjacency_matrix):
    G = nx.Graph()

    # Добавление вершин
    for i in range(len(adjacency_matrix)):
        G.add_node(i + 1)  # Вершины пронумерованы с 1

    # Добавление рёбер на основе таблицы смежности
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] != 0:
                G.add_edge(i + 1, j + 1, weight=adjacency_matrix[i][j])

    # Рисование графа
    pos = nx.spring_layout(G)  # Позиционирование вершин
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', edge_color='gray', linewidths=1, alpha=0.7)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Отображение графа
    plt.show()

# Пример матрицы смежности (adjacency_matrix)
adjacency_matrix = [
    [0, 6, 8, 0, 0, 7, 0],
    [6, 0, 11, 12, 9, 0, 5],
    [8, 11, 0, 7, 8, 0, 9],
    [0, 12, 7, 0, 6, 5, 10],
    [0, 9, 8, 6, 0, 8, 0],
    [7, 0, 0, 5, 8, 0, 7],
    [0, 5, 9, 10, 0, 7, 0]
]

draw_graph(adjacency_matrix)
