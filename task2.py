from collections import deque

def reconstruct_path(parent, start, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()

        if node == goal:
            return reconstruct_path(parent, start, goal)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

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

    print("BFS Path:", bfs(graph, 'A', 'F'))  