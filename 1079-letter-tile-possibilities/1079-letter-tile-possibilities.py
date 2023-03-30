class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        visited = [False]*len(tiles)

        def dfs(seq,depth):
            if seq:
                ans.add(seq)
            if depth==len(tiles)-1:
                return 
            for i in range(len(tiles)):
                if not visited[i]:
                    visited[i] = True
                    dfs(seq+tiles[i], depth+1)
                    visited[i]=False
        dfs('',-1)
        return len(ans)
