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

"""
For undirected graphs the neighbours fall in three categories during DFS
1. visited[neighbour] = T and neighbour != parent
        THIS IS CYCLIC CONDITION
2. visited[neighbour] = T and neighbour == parent
        DO NOTHING
3. visited[neighbour] = F
        DO DFS
"""

def isCycleUndirected(graph, visited, curr, parent):
    visited.add(curr)

    for neighbour in graph[curr]:
        # order matters, dont run this if after below's if
        # in case it is done, there are chances that isCycleUndirected will return false
        # but will make visited true. Then checking this condition will be True and it
        # will return True
        if neighbour.dest in visited and neighbour.dest != parent:
            return True
    
        if neighbour.dest not in visited:
            if isCycleUndirected(graph, visited, neighbour.dest, curr):
                return True
            
    return False


"""
A way of sorting graph nodes such that the nodes traversed first
during traversal are placed before than its neighbour
"""

def topSort(graph, visited, curr, stack):

    # We can use list for keeping visited array instead of set
    visited[curr] = True
    for neighbour in graph[curr]:
        if not visited[neighbour.dest]:
            topSort(graph, visited, neighbour.dest, stack)
    stack.append(curr)

"""
Dijkstra's Algorithm: A way to find shortest distance from source to target

Relaxation rule:
    u -> source node
    v -> destination/target node
    dt[u] + w < dt[v]
    dt[v] = dt[u] + w

    Priority Queues are used in Dijkstra's Algorithm
"""

import sys
from queue import PriorityQueue

def dijkstra(graph, src, V):

    visited = set()
    dt = [sys.maxsize] * V
    dt[src] = 0
    pq = PriorityQueue()
    # Priority queue in python has weight as first argument
    # and key as second
    pq.put((0,0))

    while not pq.empty():
        _, u = pq.get()

        if u not in visited:
            visited.add(u)
            
            for neighbour in graph[u]:
                v = neighbour.dest
                wt = neighbour.weight
                if dt[u] + wt < dt[v]:
                    dt[v] = dt[u] + wt
                    pq.put((dt[v], v))
    return dt

"""
BELLMAN FORD ALGORITHM

Limitation of Dijkstra:
    - Cannot executed on negative weights

Limitation of Bellman Ford:
    - Cannot work on graphs having negative weight cycles
    i.e for graph
        Edge(A,B,a)
        Edge(B,C,b)
        Edge(C,A,c)
    now -ve weight cycle exists if (a+b+c < 0)
"""

def bellman(graph, src, V):

    dt = [sys.maxsize] * V
    dt[src] = 0

    for i in range(V-1):  #O(V)
        for u in range(V): # O(E)
            for neighbour in graph[u]:
                v = neighbour.dest
                wt = neighbour.weight
                if dt[u] != sys.maxsize and dt[u] + wt < dt[v]:
                    dt[v] = dt[u] + wt
    
    ## For detecting -ve weight cycle
    ## Incase distance matrix gets updated then
    ## Negative weight cycle exists 
    for u in range(V): # O(E)
        for neighbour in graph[u]:
            v = neighbour.dest
            wt = neighbour.weight
            if dt[u] != sys.maxsize and dt[u] + wt < dt[v]:
                print("Negative weight cycle exists")                                                                                                          
    return dt
    