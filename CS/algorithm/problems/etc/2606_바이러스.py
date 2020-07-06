def DFS(matrix,node):
    visited[node] = 1
    for i in range(n+1):
        if matrix[i][node] == 1 and visited[i] == 0:
            DFS(matrix,i)

cnt = 0
n = int(input())
k = int(input())
matrix = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(k):
    i, j = map(int, input().split())
    matrix[i][j] = 1
    matrix[j][i] = 1

DFS(matrix, 1)
print(sum(visited)-1)