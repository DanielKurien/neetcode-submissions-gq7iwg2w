class Solution:
    def trap(self, height: List[int]) -> int: 
        leftMax = []
        rightMax = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                leftMax.append(height[i])
            else:
                leftMax.append(max(height[i], leftMax[i - 1]))

        for j in range(len(height) -1, -1, -1):
            if j == len(height) - 1:
                rightMax[j] = height[j]
            else:
                rightMax[j] = max(height[j], rightMax[j + 1])
        
        water = 0
        
        for i in range(len(height)):
            water += max(min(leftMax[i], rightMax[i]) - height[i], 0)
        
        return water