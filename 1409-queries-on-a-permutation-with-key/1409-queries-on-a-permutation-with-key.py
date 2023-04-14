class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1,m+1))
        res = []
        for i in queries:
            ind = p.index(i)
            res.append(ind)
            temp = p[ind]
            p.pop(ind)
            p = [temp]+p
            
        return res

