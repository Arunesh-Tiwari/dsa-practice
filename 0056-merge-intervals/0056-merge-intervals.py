class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        for i in range(len(intervals)):
            if(ans==[]):
                ans.append(intervals[i])

            else:
                prev_end = ans[-1][1]
                cur_start = intervals[i][0]
                cur_end = intervals[i][1]

                if(prev_end >= cur_start):
                    ans[-1][1]= max(prev_end, cur_end)
                else:
                    ans.append(intervals[i])
        return ans 
        