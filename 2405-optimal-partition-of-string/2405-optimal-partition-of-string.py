class Solution:
    def partitionString(self, s: str) -> int:
        visits = set()
        count = 0
        i = 0
        while i < len(s):
            count += 1
            while i<len(s) and s[i] not in visits:
                visits.add(s[i])
                i += 1
            visits.clear()
        return count
                