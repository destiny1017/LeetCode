class Solution:
    def romanToInt(self, s: str) -> int:
        intmap = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        comb_words = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        
        sum, i = 0, 0
        while i < len(s):
            if s[i] in comb_words.keys() and i < len(s) - 1:
                if s[i+1] == comb_words[s[i]][0]:
                    sum += intmap[comb_words[s[i]][0]] - intmap[s[i]]
                    i += 2
                    continue
                elif s[i+1] == comb_words[s[i]][1]:
                    sum += intmap[comb_words[s[i]][1]] - intmap[s[i]]
                    i += 2
                    continue

            sum += intmap[s[i]]
            i += 1

        return sum