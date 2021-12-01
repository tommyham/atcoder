mov=[[0,1],[1,0],[-1.0],[0,-1]]
import networkx as nx
import collections 

def search(m):
    global mov
    

H,W=map(int,input().split())
S=[[0 for i in range(W)] for j in range(H)]
for i in range(H):
    S[i]=list(map(str,input().split()))
s=[0,0]
g=[0,0]
for i in len(S):
    for j in range(len(S[i])):
        if(S[i][j]=="."):
            s=S[i][j]
        else:
            pass
