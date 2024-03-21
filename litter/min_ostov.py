def welsh_powell(graph):
    # Сортируем вершины графа по степеням в невозрастающем порядке
    sorted_nodes = sorted(graph.nodes, key=lambda node: graph.degree(node), reverse=True)
    colors = {}  # Словарь для хранения раскраски вершин

    for node in sorted_nodes:
        # Получаем список цветов смежных вершин
        neighbor_colors = {colors[neighbor] for neighbor in graph.neighbors(node) if neighbor in colors}

        # Находим минимальный доступный цвет
        min_color = 0
        while min_color in neighbor_colors:
            min_color += 1

        colors[node] = min_color

    return colors


# Пример использования
import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

coloring = welsh_powell(G)
print("Раскраска вершин:", coloring)