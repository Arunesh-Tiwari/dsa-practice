class Solution:
    def sortTheStudents(self, a: List[List[int]], k: int) -> List[List[int]]:
        v=[]
        
        for i in range(len(a)):
            v+=[[a[i][k],a[i]]]
        print(v)
        def cmp(a):
            return a[0]
        v=sorted(v,key=cmp)[::-1]
        print(v)
        ans=[]
        for i in range(len(v)):
            a[i]=v[i][1]
        return a