class Solution(object):
    def maxArea(self, height):
        st, ed = [0, height[0]], [len(height)-1, height[-1]]
        water = min(st[1], ed[1]) * (len(height)-1)

        while ed[0] > st[0]:
            if st[1] < ed[1]:
                st[0] += 1
                st[1] = height[st[0]]
            else:
                ed[0] -= 1
                ed[1] = height[ed[0]]

            water = max(water, min(st[1], ed[1]) * (ed[0] - st[0]))
            
        return water