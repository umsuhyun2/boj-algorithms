from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False]*(N+1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)

def bfs(start):
    visited = [False]*(N+1)
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

dfs(V)
print()
bfs(V)
