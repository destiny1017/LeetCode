class Solution(object):
    def convert(self, s, numRows):
        result = ""
        arr = []
        if numRows == 1 or numRows >= len(s):
            return s
        
        for i in range(numRows):
            arr.append([])
        idx = 0
        d = 1
        for c in s:
            arr[idx].append(c)
            if idx == 0:              
                d = 1
            elif idx == numRows - 1:
                d = -1
            
            idx += d

        for i in range(numRows):
            result += "".join(val for val in arr[i])
                    

        return result
