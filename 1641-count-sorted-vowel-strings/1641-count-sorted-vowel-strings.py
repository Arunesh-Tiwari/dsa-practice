class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0]*5 for i in range(n)]
        dp[0] = [1]*5

        for i in range(1,len(dp)):
            dp[i][0]= dp[i-1][0]+dp[i-1][1]+dp[i-1][2]+dp[i-1][3]+dp[i-1][4]
            dp[i][1]= dp[i-1][1]+dp[i-1][2]+dp[i-1][3]+dp[i-1][4]
            dp[i][2]= dp[i-1][2]+dp[i-1][3]+dp[i-1][4]
            dp[i][3]= dp[i-1][3]+dp[i-1][4]
            dp[i][4]= dp[i-1][4]
        return sum(dp[-1])        