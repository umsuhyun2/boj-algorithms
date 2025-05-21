import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(v, depth):
    if depth == 5:
        print(1)
        sys.exit(0)
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, depth + 1)
    visited[v] = False  # 백트래킹: 방문 해제

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
for i in range(N):
    dfs(i, 1)

print(0)
