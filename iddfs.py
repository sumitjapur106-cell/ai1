def dls(graph, node, goal, depth):
    if depth == 0 and node == goal:
        return True
    if depth > 0:
        for neighbor in graph.get(node, []):
            if dls(graph, neighbor, goal, depth - 1):
                return True
    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        if dls(graph, start, goal, depth):
            return True
    return False


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start = 'A'
goal = 'F'
max_depth = 3

if iddfs(graph, start, goal, max_depth):
    print("Goal found!")
else:
    print("Goal not found.")