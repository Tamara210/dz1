# Анализ волнового алгоритма

## Временная сложность и практические измерения

| Часть алгоритма         | Временная сложность | Время выполнения (сек) | Данные                          | Стенд                                                                 |
|--------------------------|---------------------|-------------------------|---------------------------------|----------------------------------------------------------------------|
| Подсчет вершин           | $ O(n) $               | 0.000005                | Список рёбер                   | [count_vertices.py](https://github.com/Tamara210/dz1/blob/main/count_vertices.py) |
| Получение списка вершин  |               | 0.000002                | Список рёбер                   | [get_vertices.py](https://github.com/Tamara210/dz1/blob/main/get_vertices.py)     |
| Обход вершин             |  ![alt text](image.png)          | 0.000015                | Список рёбер, начало, конец              | [wave_algorithm.py](https://github.com/Tamara210/dz1/blob/main/wave_algorithm.py) |
| Восстановление пути      | $$ O(n) $$              | 0.000004                | Список рёбер, начало, конец              | [path_rec.py](https://github.com/Tamara210/dz1/blob/main/path_rec.py)             |
| Поиск второго минимума   | $$ O(n) $$                 | 0.000004                | Список чисел                   | [min_count.py](https://github.com/Tamara210/dz1/blob/main/min_count.py)           |