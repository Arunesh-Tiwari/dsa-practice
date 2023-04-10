class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (a,b) for a,b in connections}
        neighbours = {city:[] for city in range(n)}
        visited = set()
        changes = 0

        for i,j in connections:
            neighbours[i].append(j)
            neighbours[j].append(i)
        
        def dfs(city):
            nonlocal edges, neighbours, visited, changes

            for child in neighbours[city]:
                if child in visited:
                    continue
                
                #check for leading to city 0
                if (child,city) not in edges:
                    changes += 1
                visited.add(child)
                dfs(child)
        visited.add(0)
        dfs(0)
        return changes
