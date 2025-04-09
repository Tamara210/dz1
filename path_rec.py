def reconstruct_path(parent, start, end):
    """Восстановление пути от конечной вершины к начальной."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path