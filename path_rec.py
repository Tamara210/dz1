import time

def reconstruct_path(parent, start, end):
    """Восстановление пути от конечной вершины к начальной."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

if __name__ == "__main__":
    # Входные данные
    parent = {1: None, 2: 1, 3: 2, 4: 2, 5: 4}
    start = 1
    end = 5
    
    # Измерение времени
    start_time = time.perf_counter()
    path = reconstruct_path(parent, start, end)
    exec_time = time.perf_counter() - start_time
    
    # Вывод результатов
    print(f"Восстановленный путь: {path}")
    print(f"Время выполнения: {exec_time:.6f} секунд")