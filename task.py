def dfs(graph, start, goal):
    stack = [(start, [start])]  
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None


if __name__ == "__main__":
    graph = {
 'A': ['B', 'C'],
'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': ['F'],
'F': []
    }

    print("DFS Path:", dfs(graph, 'A', 'F'))
