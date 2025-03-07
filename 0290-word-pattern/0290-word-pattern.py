class Solution(object):
    def wordPattern(self, pattern, s):
        pmap = dict()
        smap = dict()
        arr = s.split(" ")
        result = True
        
        if len(arr) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in pmap:
                if pmap[pattern[i]] != arr[i]:
                    result = False
                    break
            else:
                if arr[i] in smap:
                    result = False
                    break
                pmap[pattern[i]] = arr[i]
                smap[arr[i]] = pattern[i]
        
        return result
        