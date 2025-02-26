class Solution(object):
    def convert(self, s, numRows):
        result = ""
        arr = []
        for i in range(numRows):
            arr.append(["" for _ in range(len(s))])
        n, m = 0, 0
        idx = 0
        while idx < len(s):
            if n < numRows:
                arr[n][m] = s[idx]
                n += 1
                idx += 1
            else:
                n -= 1
                for i in range(numRows):
                    if i == 0 or i == numRows - 1:
                        continue
                    else:
                        n -= 1
                        m += 1
                        arr[n][m] = s[idx]
                        idx += 1
                        if idx >= len(s):
                            break
                n = 0
                m += 1

        for i in range(numRows):
            result += "".join(val for val in arr[i])
                    

        return result
