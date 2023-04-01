class Solution:
    def search(self, n: List[int], t: int) -> int:
    	i, j = 0, len(n)-1
    	while j - i > 1:
    		m = (i+j)//2
    		if t <= n[m]: j = m
    		else: i = m
    	return i if n[i] == t else j if n[j] == t else -1
