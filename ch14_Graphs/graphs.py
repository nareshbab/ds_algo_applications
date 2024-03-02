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

"""
MINIMUM SPANNING TREE

A minimum spanning tree or minimum weight tree is a subset of the edges of a CONNECTED, 
EDGE_WEIGHTED UNDIRECTED graph that connects all the vertices together,
without any cycles and with the minimum possible total edge weight

Properties of MST:
- Subgraph of Graph
- All vertices present
- Connected Graph
- No cyles
- Edge weight is minimum

Algorithms to find MSTs:
- Prim's Algorithm
"""

def prims(graph): ## O(ElogE)

    visited = set()
    pq = PriorityQueue()
    ## Priority Queue (weight, key)
    pq.put((0,0))

    mst_cost = 0
    while not pq.empty():
        cost, u = pq.get()

        if u not in visited:
            visited.add(u)
            mst_cost += cost

            for neighbour in graph[u]:
                v = neighbour.dest
                wt = neighbour.weight
                if neighbour.dest not in visited:
                    pq.put((wt, v))
    return mst_cost

"""
STRONGLY CONNECTED COMPONENTS

SCC is a component in which we can reach every vertex of the
component from every other vertex in that component

KOSARAJU's ALGORITHM O(V+E)
Steps:
    - Get nodes in stack (topological order) O(V+E)
    - transpose the graph O(V+E)
    - Do DFS according to stack nodes on the transposed graph (reverse DFS) O(V+E)
"""

def kosaraju_scc(graph, visited, curr, stack, V):

    # STEP 1 (TopSort): O(E+V)
    for i in range(V):
        if not visited[i]:
            topSort(graph, visited, curr, stack)

    dfs_visited = set()

    # STEP 2 (TRANSPOSE GRAPH): O(E+V)
    transposed_graph= {}
    
    for i in range(V):
        for neighbour in graph[i]:
            if transposed_graph.get(neighbour.dest):
                transposed_graph[neighbour.dest].append(Edge(neighbour.dest, neighbour.src))
            else:
                transposed_graph.update({neighbour.dest: [Edge(neighbour.dest,neighbour.src)]})
    
    # STEP 3 DFS OF TOPSORT STACK: O(E+V)
    while len(stack) > 0:
        curr = stack.pop()
        if curr not in dfs_visited:
            dfs(transposed_graph, Edge(curr, 0), dfs_visited)
            print()

"""
BRIDGE IN GRAPHS:
Bridge is an edge whose deletion increases 
the graph's number of connected components

TARJAN'S ALGORITHM:
    - perform DFS
    - compare dt[u] < low[v]
"""

def tarjan_dfs(graph, curr, visited, dt, low, time, parent):
    
    visited.add(curr)
    dt[curr] = low[curr] = time + 1
    
    for neighbour in graph[curr]:
        # pass if the neighbour is parent
        if neighbour.dest == parent:
            continue
        
        # if node is not visited do DFS and update the lowest of node
        elif neighbour.dest not in visited:
            tarjan_dfs(graph, neighbour.dest, visited, dt, low, time+1, curr)
            low[curr] = min(low[curr], low[neighbour.dest])

            # now check for bridge condition
            if dt[curr] < low[neighbour.dest]:
                print(curr, "----->", neighbour.dest)
        
        # if node is visited and not its parent then update the lowest of node
        # neighbour.dest !=parent and neighbour.dest in visited:
        else:
            low[curr] = min(low[curr], dt[neighbour.dest])

def tarjan_bridge(graph, curr, parent, V):
    # set intial time to 0
    t = 0
    dt = [sys.maxsize] * V
    low = [sys.maxsize] * V
    visited  = set()
    dt[curr] = low[curr] = t + 1

    for i in range(V):
        if i not in visited:
            tarjan_dfs(graph, i, visited, dt, low, t, -1)            



