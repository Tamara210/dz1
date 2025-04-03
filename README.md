# Анализ волнового алгоритма

## Временная сложность и практические измерения

| Часть алгоритма | Временная сложность | Время выполнения (сек) | Описание |
|-----------------|---------------------|----------------------|-----------|
| Подсчет вершин | O(E) | 0.000005 | Проход по всем ребрам графа для подсчета уникальных вершин |
| Получение списка вершин | O(E) | 0.000002 | Формирование списка уникальных вершин из ребер |
| Обход вершин | O(V * E) | 0.000015 | Поиск кратчайшего пути волновым алгоритмом |
| Восстановление пути | O(V) | 0.000004 | Восстановление найденного пути от конечной до начальной вершины |

## Исходный код измерений

### Подсчет вершин
```python
def count_vertices(edges):
    start_time = time.perf_counter()
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    end_time = time.perf_counter()
    return len(vertices), (end_time - start_time)
```

### Получение списка вершин
```python
def get_vertices(edges):
    start_time = time.perf_counter()
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    end_time = time.perf_counter()
    return list(vertices), (end_time - start_time)
```

### Обход вершин
```python
def wave_algorithm(edges, start, end):
    vertices, _ = get_vertices(edges)
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
```

### Восстановление пути
```python
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
```

## Тестовые данные
```python
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
start = 1
end = 5
```

# Анализ алгоритма поиска второго минимального элемента

## Временная сложность и практические измерения

| Часть алгоритма | Временная сложность | Время выполнения (сек) | Описание |
|-----------------|---------------------|----------------------|-----------|
| Поиск второго минимума | O(n) | 0.000004 | Однократный проход по массиву для поиска второго минимального элемента |

## Исходный код измерений

### Поиск второго минимума
```python
def find_second_min(arr):
    start_time = time.perf_counter()
    if not arr:
        return None
    first_min = arr[0]
    second_min = None
    for num in arr[1:]:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif num != first_min:
            if second_min is None or num < second_min:
                second_min = num
    end_time = time.perf_counter()
    return second_min, (end_time - start_time)
```

## Тестовые данные
```python
test_array = [5, 2, 8, 1, 9]
```