def is_safe(v, graph, color, c, V):
    for u in range(V):
        if graph[v][u] == 1 and color[u] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v, V):
    if v == V:
        return True

    for c in range(1, m + 1):
        if is_safe(v, graph, color, c, V):
            color[v] = c

            if graph_coloring_util(graph, m, color, v + 1, V):
                return True

            color[v] = 0

    return False

def solve_m_coloring(graph, m):
    V = len(graph)
    color = [0] * V

    if not graph_coloring_util(graph, m, color, 0, V):
        print("No valid coloring exists.")
        return False

    print(f"Solution exists with {m} colors:")
    for v in range(V):
        print(f"Vertex {v} -> Color {color[v]}")
    return True


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    M = 3

    solve_m_coloring(graph, M)
