class Solution:
    def findContentChildren(self, greed: List[int], cookies: List[int]) -> int:
        greed.sort()
        cookies.sort()

        content_children = 0
        i, j = 0, 0

        while i < len(greed) and j < len(cookies):
            if cookies[j] >= greed[i]:
                content_children += 1
                i += 1
            j += 1

        return content_children
        