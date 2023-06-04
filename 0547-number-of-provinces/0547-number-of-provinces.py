class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        queue = []
        count = 0
        for i in range(len(isConnected)):
            if i not in visited and isConnected[i][i]==1:
                visited.add(i)
                count += 1
                queue.append(i)

                while queue:
                    n = queue.pop(0)
                    for j in range(len(isConnected[n])):
                        if j not in visited and isConnected[n][j]==1:
                            visited.add(j)
                            queue.append(j)
        return count