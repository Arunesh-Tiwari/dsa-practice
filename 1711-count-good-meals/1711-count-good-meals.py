class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10 ** 9 + 7
        cnt = collections.Counter(deliciousness)
        res = 0
        for k, v in cnt.items():
            for i in range(22):
                p = (1 << i) - k
                if p >= 0 and p in cnt:
                    if p == k: res += v * (v - 1)
                    else: res += v * cnt[p]
            
        return (res // 2)  % mod