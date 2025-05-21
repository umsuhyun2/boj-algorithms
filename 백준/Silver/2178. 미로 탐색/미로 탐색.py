from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*M for _ in range(N)]
distance = [[0]*M for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    distance[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1:
            return distance[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and maze[nx][ny] == 1:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

print(bfs())
