#Creating the 3 functions needed to create a recursive version of Floyd Warshall
def floyd_warshall_recursive(graph, dist, i, j, k):
    if k == -1:
        return dist[i][j]
    elif i == j:
        return 0
    else:
        without_k = floyd_warshall_recursive(graph, dist, i, j, k - 1)
        via_k = floyd_warshall_recursive(graph, dist, i, k, k - 1) + floyd_warshall_recursive(graph, dist, k, j, k - 1)
        return min(without_k, via_k)

def initialize_distance_matrix(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    return dist

def floyd_warshall(graph):
    n = len(graph)
    dist = initialize_distance_matrix(graph)
    for i in range(n):
        for j in range(n):
            dist[i][j] = floyd_warshall_recursive(graph, dist, i, j, n - 1)
    return dist

#Copy/pasting an imperative implementation of Floyd Marshall for testing purposes
#Code is copy/pasted from https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
def floyd_warshall_imperative(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(4):
        for i in range(4):
            for j in range(4):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    return dist