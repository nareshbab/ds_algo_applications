from graphs import *


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

    ### BREADTH FIRST SEARCH
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

    ### DEPTH FIRST SEARCH
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


    # PATHS TO TARGET FROM SOURCE
    # all_paths_visited = set()
    # pathSourceToTarget(graph2, 0, all_paths_visited, "0", 5)

    ### CYCLE DETECTION FOR DIRECTED GRAPHS
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

    ### CYCLE DETECTION FOR UNDIRECTED GRAPHS
    graph4 = {
        0: [Edge(0,1), Edge(0,4)],
        1: [Edge(1,0), Edge(1,2), Edge(1,4)],
        2: [Edge(2,1), Edge(2,3)],
        3: [Edge(3,2)],
        4: [Edge(4,0), Edge(4,1), Edge(4,5)],
        5: [Edge(5,4)]
    }

    n_vertex_cycle_undirected = 6
    cycle_undirected_visited = set()
    # for i in range(n_vertex_cycle_undirected):
    #     if i not in cycle_undirected_visited:
    print(isCycleUndirected(graph4, cycle_undirected_visited, 0, -1))
            # if isCycle:
            #     print(isCycle)
            #     break


    ### TOPOLOGICAL SORTING
    graph5 = {
        0: [],
        1: [],
        2: [Edge(2,3)],
        3: [Edge(3,1)],
        4: [Edge(4,0), Edge(4,1)],
        5: [Edge(5,0), Edge(5,2)]
    }
    
    n_vertex_topsort = 6
    topsort_visited = [False]*n_vertex
    topsort_stack = []
    
    # loop through all nodes incase of broken graphs
    for i in range(n_vertex_topsort):
        if not topsort_visited[i]:
            topSort(graph5, topsort_visited, i, topsort_stack)
    
    for i in range(len(topsort_stack)):
        print(topsort_stack.pop())

    
    ### DIJKSTRA'S ALGORITHM
    graph6 = {
        0: [Edge(0,1,2), Edge(0,2,4)],
        1: [Edge(1,3,7), Edge(1,2,1)],
        2: [Edge(2,4,3)],
        3: [Edge(3,5,1)],
        4: [Edge(4,3,2),  Edge(4,5,5)],
        5:[]
    }

    print("Dijkstra's shortest distance algo :: ", dijkstra(graph6, 0, 6))

    ### BELLMAN FORD ALGORITHM
    graph7 = {
        0: [Edge(0,1,2), Edge(0,2,4)],
        1: [Edge(1,2,-4)],
        2: [Edge(2,3,2)],
        3: [Edge(3,4,4)],
        4: [Edge(4,1,-1)] # Change -1 to -10 for creating negative weight cycle
    }

    print("Bellman ford algorithm distance matrix :: ", bellman(graph7, 0, 5))