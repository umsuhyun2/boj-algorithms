import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    data = list(map(int, input().split()))
    v = data[0]
    for i in range(1, len(data)-1, 2):
        nxt = data[i]
        dist = data[i+1]
        graph[v].append((nxt, dist))

def bfs(start):
    visited = [-1] * (N+1)
    visited[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for nxt, dist in graph[v]:
            if visited[nxt] == -1:
                visited[nxt] = visited[v] + dist
                queue.append(nxt)
    max_dist = max(visited)
    max_node = visited.index(max_dist)
    return max_node, max_dist

node, _ = bfs(1)
_, diameter = bfs(node)
print(diameter)
