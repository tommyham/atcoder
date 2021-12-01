from collections import deque
import math


def bfs():
    h,w,sy,sx,gy,gx=list(map(int,input.split()[:6]))
    maze=list(map(list,input.split()[6:]))
    for y in range(h):
        for x in range(w):
            if maze[y][x]=='.':
                maze[y][x]=math.inf


    maze[sy-1][sx-1]=0
    que=deque([[sy-1,sx-1]])
    while que:
        y,x=que.popleft()
        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            nexty,nextx=y+i,x+j
            dist=maze[nexty][nextx]
            if dist!='#':
                if dist>maze[y][x]+1:
                    maze[nexty][nextx]=maze[y][x]+1
                    que.append([nexty,nextx])
    print(maze[gy-1][gx-1])