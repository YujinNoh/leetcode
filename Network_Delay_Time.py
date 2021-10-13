class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        
        graph = [[] for i in range(n + 1)]
        distance = [1e9] * (n + 1)
        
        for node1, node2, dist in times:
            graph[node1].append((node2, dist))
            
        def dijkstra(start):
            q = []
            heapq.heappush(q, (0, start))
            distance[start] = 0
            
            while q:
                dist, now = heapq.heappop(q)
                if distance[now] < dist:
                    continue
                for i in graph[now]:
                    cost = dist + i[1]
                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q,(cost, i[0]))
            
        
        dijkstra(k)
        
        max_distance = 0
        for d in distance:
            if d != 1e9:
                max_distance = max(max_distance, d)
            
        
        return max_distance if (max_distance < 1e9 and distance.count(1e9) <= 1)  else -1
