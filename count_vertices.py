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