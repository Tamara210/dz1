import time

def find_second_min(arr):
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
    return second_min if second_min is not None else None

def measure_execution_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    return result, end_time - start_time

# Тестовые данные
test_array = [5, 2, 8, 1, 9]


result, exec_time = measure_execution_time(find_second_min, test_array)
print(f"Массив: {test_array}")
print(f"Второй минимум: {result}")
print(f"Время выполнения: {exec_time:.6f} сек\n")
