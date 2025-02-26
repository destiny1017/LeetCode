class Solution(object):
    def reverseWords(self, s):
        s += " "
        str_arr = []
        word = ""
        for i in range(len(s)):
            if s[i] == " ":
                if word.isalnum():
                    str_arr.append(word)
                word = ""
            else:
                word += s[i]
        
        while str_arr:
            word += str_arr.pop() + " "
        
        return word[0:-1]