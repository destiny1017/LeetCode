class Solution(object):
    
    def getRoman(self, roman_map, n, unit):
        num = n * unit
        if n == 0:
            return ""
        elif num in roman_map:
            return roman_map[num]
        else:
            result = ""
            if n >= 5:
                result += roman_map[5 * unit]
                num %= (5 * unit)
            result += roman_map[unit] * (num // unit)
            return result
    
    def getLastRoman(self, roman_map, n, unit):
        return roman_map[unit] + roman_map[(n * unit) + unit]

    def intToRoman(self, num):
        roman_map = {
            1: "I", 5: "V", 10: "X", 50: "L",
            100: "C", 500: "D", 1000: "M"
        }

        result = ""
        roman = []
        str_num = str(num)
        unit = 1
        for i in range(len(str_num)-1, -1, -1):
            if str_num[i] == "4" or str_num[i] == "9":
                roman.append(self.getLastRoman(roman_map, int(str_num[i]), unit))
            else:
                roman.append(self.getRoman(roman_map, int(str_num[i]), unit))
            unit *= 10
        
        while roman:
            result += roman.pop()

        return result
        
        
        