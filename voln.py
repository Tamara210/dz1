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

def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    start_time = time.perf_counter()
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    end_time = time.perf_counter()
    return list(vertices), (end_time - start_time)

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

# Тестовые данные
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
start = 1
end = 5

# Измерения
vertices_count, count_time = count_vertices(edges)
vertices_list, list_time = get_vertices(edges)
path, visited, traverse_time, path_time = wave_algorithm(edges, start, end)
print(f"Количество вершин: {vertices_count}, Время подсчета: {count_time:.6f} секунд")
print(f"Список вершин: {vertices_list}, Время получения списка: {list_time:.6f} секунд")
print(f"Путь от {start} до {end}: {path}, Время обхода: {traverse_time:.6f} секунд, Время восстановления пути: {path_time:.6f} секунд")
