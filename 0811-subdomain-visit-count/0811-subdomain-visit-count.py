class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        visits = {}

        for i in cpdomains:
            l = i.split(' ')
            value = l[0]
            domain = l[1]
            subdomains = domain.split(".")
            for i in range(len(subdomains)):
                sub = '.'.join(subdomains[i:])
                if sub not in visits:
                    visits[sub] = value
                else:
                    visits[sub] = str(int(visits[sub]) + int(value))
                
        for i, j in visits.items():
            ans.append(j+' '+i)

        return ans
        