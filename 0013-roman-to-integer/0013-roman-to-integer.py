class Solution:
    def romanToInt(self, s: str) -> int:
        intmap = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        
        sum = 0
        for i in range(len(s) - 1):
            if intmap[s[i]] < intmap[s[i+1]]:
                sum -= intmap[s[i]]
            else:
                sum += intmap[s[i]]
            
        sum += intmap[s[-1]]

        return sum