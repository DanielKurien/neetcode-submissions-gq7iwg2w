class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            if num - 1 not in numSet:
                currLength = 0
                currNum = num

                while currNum in numSet:
                    currLength += 1
                    currNum += 1
                
                maxLength = max(maxLength, currLength)
        return maxLength

