class Solution:
    def findJudge(self, N, trust):
        for person in range(1, N+1):
            if self.trust_nobody(person, trust) and self.everybody_trusts(person, trust, N):
                return person
        return -1
    
    def trust_nobody(self, person, trust):
        for item in trust:
            if item[0] == person:
                return False
        return True
        
    def everybody_trusts(self, person, trust, N):
        trust_set = set()
        for item in trust:
            if item[1] == person:
                trust_set.add(item[0])
        person_set = set(range(1, N+1))
        trust_missing_list = list(person_set.difference(trust_set))
        if trust_missing_list.count(person) == len(trust_missing_list) and trust_missing_list:
            return person 
        else:
            return False

# Test Code
def stub(N, trust):
    sol_obj = Solution()
    return sol_obj.findJudge(N, trust)
    
