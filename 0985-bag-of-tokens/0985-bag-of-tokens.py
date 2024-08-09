class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        low, high = 0, len(tokens)-1
        tokens = sorted(tokens)
        print (tokens)
        maxscore = 0

        while low <= high:
            if tokens[low] <= power:
                power -= tokens[low]
                low += 1
                score += 1
                maxscore= max(maxscore,score)

            elif tokens[low]>power and score >=1:
                power += tokens[high]
                high -= 1
                score -= 1
            
            else:
                break
        return maxscore
