class Solution:
    def sortVowels(self, s: str) -> str:
        c = Counter(s)
        ans = ""
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']        
        hw = defaultdict(bool)
        
        for i in vowels:
            hw[i] = True
        
        h = []
        
        for i in vowels[::-1]:
            if c[i]: h.append([i, c[i]])
        
        for i in s:
            if hw[i]:
                ans += h[-1][0] 
                h[-1][1] -= 1
                
                if not h[-1][1]:
                    h.pop()                    
            else:
                ans += i
                
        return ans
                
                
                