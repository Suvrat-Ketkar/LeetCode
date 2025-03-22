#2685 Count the Number of Complete Components
# Date: 22/03/2025
#Type: Daily Problem
# Method used: BFS traversal

from collections import deque
from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = [False] * n
        ans = 0
        def bfs(node):
            q = deque([node])
            vis[node] = True
            comp = []
            while q:
                cur = q.popleft()
                comp.append(cur)
                for neighbor in adj[cur]:
                    if not vis[neighbor]:
                        vis[neighbor] = True
                        q.append(neighbor)
            return comp
        for i in range(n):
            if not vis[i]:
                comp = bfs(i)
                if all(len(adj[node]) == len(comp) - 1 for node in comp):
                    ans += 1
        return ans