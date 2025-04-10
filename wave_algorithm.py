import time
from get_vertices import get_vertices

def wave_algorithm(edges, start, end):
    """Реализация волнового алгоритма."""
    vertices, _ = get_vertices(edges)

    # Время обхода вершин
    traverse_start = time.perf_counter()
    visited = {v: 0 for v in vertices}
    visited[start] = 1
    parent = {v: None for v in vertices}
    found = False
    step = 1

    while True:
        new_vertices_found = False
        for v in vertices:
            if visited[v] == step:
                for edge in edges:
                    if edge[0] == v and visited[edge[1]] == 0:
                        visited[edge[1]] = step + 1
                        parent[edge[1]] = v
                        new_vertices_found = True
                    if edge[1] == v and visited[edge[0]] == 0:
                        visited[edge[0]] = step + 1
                        parent[edge[0]] = v
                        new_vertices_found = True
        if visited[end] != 0:
            found = True
            break
        if not new_vertices_found:
            break
        step += 1
    traverse_time = time.perf_counter() - traverse_start

    # Время восстановления пути
    path_start = time.perf_counter()
    if found:
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        path_time = time.perf_counter() - path_start
        return path, visited, traverse_time, path_time
    else:
        path_time = time.perf_counter() - path_start
        return None, visited, traverse_time, path_time

if __name__ == "__main__":
    # Входные данные
    edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
    start = 1
    end = 5

    # Измерение времени
    path, visited, traverse_time, path_time = wave_algorithm(edges, start, end)
    
    # Вывод результатов
    print(f"Путь от {start} до {end}: {path}")
    print(f"Время обхода: {traverse_time:.6f} секунд")
    print(f"Время восстановления пути: {path_time:.6f} секунд")