class Solution(object):
    def maxArea(self, height):
        st, ed = 0, len(height)-1
        water = min(height[st], height[ed]) * ed

        while ed > st:
            if height[st] < height[ed]:
                st += 1
            else:
                ed -= 1

            water = max(water, min(height[st], height[ed]) * (ed - st))
            
        return water