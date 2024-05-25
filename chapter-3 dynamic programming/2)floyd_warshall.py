# FLOYD WARSHALL ALGORITHM

'''
find shortest path in graph
can handle negative nodes
but cant work in a negative cycle
'''

# algorithm
"""
1)intialize the solutoon matrix same as the input graph
2)update solution matrix by considering all vertices as intermediate vertex
3)if we pick k we have considered k-1

*4)for every pair (i,j) of the source and destination vetice
there are 2 possible cases
a)k is not a vertex from shortest path from source to dest
-we keep the value of dist[i][j] as it is
b)k is an intermediate vertex in shortest path from i to j
- dist[i][j] > dist[i][k]+dist[k][j] we update the value of dist[i][j] 
"""

# pseudo code
'''
for k=0 to n-1[intermediate node]
for i = 0 to n-1[source node]
for j = 0 to n-1[destination node]

dist[i,j] = min(distance[i,j],distance[i,k]+distance[k,j])
'''

V = 4
INF = 999999

# code
def floydWarshall(graph):

    dist = graph.copy()
    print('initial graph')
    print(dist)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] =  min(dist[i][j],dist[i][k]+dist[k][j])
    print('final graph')
    print(dist)

graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]

# Function call
floydWarshall(graph)
