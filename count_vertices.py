import time 

def count_vertices(edges):
    """Подсчет количества вершин в графе."""
    start_time = time.perf_counter()
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    end_time = time.perf_counter()
    return len(vertices), (end_time - start_time)

if __name__ == "__main__":
    # Входные данные
    edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
    
    # Измерение времени
    vertices_count, exec_time = count_vertices(edges)
    
    # Вывод результатов
    print(f"Количество вершин: {vertices_count}")
    print(f"Время выполнения: {exec_time:.6f} секунд")