import sys
input = sys.stdin.readline

def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
