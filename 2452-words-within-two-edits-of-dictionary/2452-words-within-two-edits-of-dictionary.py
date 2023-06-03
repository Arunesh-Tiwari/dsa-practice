from typing import List

class Solution:
  def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
    def is_valid(query, word):
        count = 0
        for i in range(len(word)):
            if word[i] != query[i]:
                count += 1
                if count > 2:
                    return False
        return count <= 2

    ans = []
    for query in queries:
        for word in dictionary:
            if is_valid(query, word):
                ans.append(query)
                break
    return ans