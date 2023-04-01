class Solution:
    def overlap(self, a, b):
        p,q = a
        r,s = b
                
        return (r >= p and r <= q) or (s >= p and s <= q) or (p >= r and p <= s) or (q >= r and q <= s)
    def merge(self, a, b):
        p,q = a
        r,s = b
        
        return (min(p,r), max(q,s))
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        i = [intervals[0]]
        
        for s,e in intervals:
            if self.overlap(i[-1], (s,e)):
                i[-1] = self.merge(i[-1], (s,e))
            else: 
                i.append((s,e))
        
        return i