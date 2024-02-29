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
from typing import Set

class Edge:
    def __init__(self, s, d, w=None) -> None:
        self.src = s
        self.dest = d
        self.weight = w

def bfs(graph, visited, start):
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

def dfs(graph, curr, visited):
    print(curr.src, "----")
    visited.add(curr.src)
    for neighbour in graph[curr.src]:
        if neighbour.dest not in visited:
            dfs(graph, Edge(neighbour.dest,0), visited)


def pathSourceToTarget(graph, curr, visited: Set, path, target):

    if curr == target:
        print(path)
        return

    for neighbour in graph[curr]:
        if neighbour not in visited:
            visited.add(curr)
            pathSourceToTarget(graph, neighbour, visited, path+str(neighbour), target)
            visited.remove(curr)

"""
Cycle Detection in Graphs:
* directed graphs
    Condition for cycle is:
        If during traversal the next node is present in recursion stack
        recursion_stack: List[bool]
* undirected graphs
    Condition for cycle is:
        If during traversal the next node is already visited
        and is not parent of current node
"""

def isCycleDirected(graph, curr, visited, recursion_stack):

    visited.add(curr)
    recursion_stack[curr]= True

    for neighbour in graph[curr]:

        #condition for cycle
        if recursion_stack[neighbour]:
            return True
        if neighbour not in visited:
            if isCycleDirected(graph, neighbour, visited, recursion_stack):
                return True
    recursion_stack[curr] =False
    return False


if __name__ == "__main__":

    graph1 = {}
    n_vertex = 7

    """
    1-----3
    /      |\\ 
    0       | 5-6
    \\      |/
    2-----4
    """

    for i in range(n_vertex):
        graph1.update({i:list()})

    graph1[0].append(Edge(0,1))
    graph1[0].append(Edge(0,2))

    graph1[1].append(Edge(1,0))
    graph1[1].append(Edge(1,3))

    graph1[2].append(Edge(2,0))
    graph1[2].append(Edge(2,4))

    graph1[3].append(Edge(3,1))
    graph1[3].append(Edge(3,4))
    graph1[3].append(Edge(3,5))

    graph1[4].append(Edge(4,2))
    graph1[4].append(Edge(4,3))
    graph1[4].append(Edge(4,5))

    graph1[5].append(Edge(5,3))
    graph1[5].append(Edge(5,4))
    graph1[5].append(Edge(5,6))

    graph1[6].append(Edge(6,5))

    # bfs_visited = set()
    # for i in range(n_vertex):
    #     if i not in bfs_visited:
    #         bfs(graph, bfs_visited, i)

    """
          1-----3
         /      |\\ 
        0       | 5-6
        \\      |/
          2-----4
    """

    # Another way of representing graph
    graph2 = {
        0 : [1,2],
        1 : [0,3],
        2 : [0,4],
        3 : [1,4,5],
        4 : [2,3,5],
        5 : [3,4,6],
        6 : [5]
    }

    # dfs_visited = set()
    # for i in range(n_vertex):
    #     if i not in dfs_visited:
    #         dfs(graph1, Edge(i, 0), dfs_visited)

    # all_paths_visited = set()
    # pathSourceToTarget(graph2, 0, all_paths_visited, "0", 5)

    # Cycle detection
    graph3 = {
        0: [2],
        1: [0],
        2: [3],
        3: [0]
    }

    cycle_visited = set()
    recursion_stack = [False] * 4
    for i in range(4):
        if i not in cycle_visited:
            isCycle = isCycleDirected(graph3, i, cycle_visited, recursion_stack)
            if isCycle:
                print(isCycle)
                break


