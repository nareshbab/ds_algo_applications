"""
Graphs
- Non weighted
- Weighted
Ways for creating graphs
- adjacency list
    ex 
    {
        "1" : [],
        "2" : [],
        "3" : [],
        "<vertex>": []
    }
- adjacency matrix
    ex 
    [[0,1,0,1], [0,0,1,1], [0,1,0,1], [0,0,0,1]]
- Edge List
    ex
    [[1,2], [1,3], [1,4], [2,1]]
- Implicit Graph

Graph Traversals
    * Breadth First Search (BFS)
        Each node and its neighbours are traversed first before moving to 
        next node
    * Depth First Search (DFS)
"""

from collections import deque

class Edge:
    def __init__(self, s, d, w=None) -> None:
        self.src = s
        self.dest = d
        self.weight = w

def bfs(graph, root, visited, start):
    """
    Time Complexity O(V+E)
    """

    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex, "----")
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour.dest not in visited:
                visited.add(neighbour.dest)
                queue.append(neighbour.dest)


graph = {}
n_vertex = 7

"""
  1-----3
 /      |\ 
0       | 5-6
 \      |/
  2-----4
"""

for i in range(n_vertex):
    graph.update({i:list()})

graph[0].append(Edge(0,1))
graph[0].append(Edge(0,2))

graph[1].append(Edge(1,0))
graph[1].append(Edge(1,3))

graph[2].append(Edge(2,0))
graph[2].append(Edge(2,4))

graph[3].append(Edge(3,1))
graph[3].append(Edge(3,4))
graph[3].append(Edge(3,5))

graph[4].append(Edge(4,2))
graph[4].append(Edge(4,3))
graph[4].append(Edge(4,5))

graph[5].append(Edge(5,3))
graph[5].append(Edge(5,4))
graph[5].append(Edge(5,6))

graph[6].append(Edge(6,5))

visited = set()
for i in range(n_vertex):
    if i not in visited:
        bfs(graph, Edge(i,0), visited, i)


