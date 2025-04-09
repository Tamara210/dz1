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