import time
from count_vertices import count_vertices
from get_vertices import get_vertices
from wave_algorithm import wave_algorithm

def main():
    # Test data
    edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
    start = 1
    end = 5

    # Perform timing analysis for 1000 iterations
    iterations = 1000
    for _ in range(iterations):
        vertices_count, count_time = count_vertices(edges)
        vertices_list, list_time = get_vertices(edges)
        path, visited, traverse_time, path_time = wave_algorithm(edges, start, end)

        # Print results for each iteration
        print(f"Количество вершин: {vertices_count}, Время подсчета: {count_time:.6f} секунд")
        print(f"Список вершин: {vertices_list}, Время получения списка: {list_time:.6f} секунд")
        print(f"Путь от {start} до {end}: {path}, Время обхода: {traverse_time:.6f} секунд, Время восстановления пути: {path_time:.6f} секунд")

if __name__ == "__main__":
    main()