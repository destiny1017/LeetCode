from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        items = []
        result = []
        if digits:
            for digit in digits:
                items.append(nums[int(digit)])

            products = list(product(*items))

            result = ["".join(item) for item in products]
        
        return result
            