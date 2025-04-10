import time

def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    start_time = time.perf_counter()
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    end_time = time.perf_counter()
    return list(vertices), (end_time - start_time)

if __name__ == "__main__":
    # Входные данные
    edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
    
    # Измерение времени
    vertices_list, exec_time = get_vertices(edges)
    
    # Вывод результатов
    print(f"Список вершин: {vertices_list}")
    print(f"Время выполнения: {exec_time:.6f} секунд")