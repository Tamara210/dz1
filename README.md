# Анализ волнового алгоритма

## Временная сложность и практические измерения

| Часть алгоритма         | Временная сложность | Время выполнения (сек) | Стенд                                                                 |
|--------------------------|---------------------|-------------------------|----------------------------------------------------------------------|
| Подсчет вершин           | O(E)               | 0.000005                | [count_vertices.py](https://github.com/Tamara210/dz1/blob/main/count_vertices.py) |
| Получение списка вершин  | O(E)               | 0.000002                | [get_vertices.py](https://github.com/Tamara210/dz1/blob/main/get_vertices.py)     |
| Обход вершин             | O(V * E)           | 0.000015                | [wave_algorithm.py](https://github.com/Tamara210/dz1/blob/main/wave_algorithm.py) |
| Восстановление пути      | O(V)               | 0.000004                | [path_rec.py](https://github.com/Tamara210/dz1/blob/main/path_rec.py)             |
| Поиск второго минимума   | O(n)               | 0.000004                | [min_count.py](https://github.com/Tamara210/dz1/blob/main/min_count.py)                     |