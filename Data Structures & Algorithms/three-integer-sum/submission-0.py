class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            sub_arr = nums[i + 1:]
            leftPointer = 0
            rightPointer = len(sub_arr) - 1
            while leftPointer < rightPointer:
                curr = sub_arr[leftPointer] + sub_arr[rightPointer]
                if curr < target:
                    leftPointer += 1
                elif curr > target:
                    rightPointer -= 1

                else:
                    res.append([nums[i], sub_arr[leftPointer], sub_arr[rightPointer]])
                    while leftPointer < rightPointer and sub_arr[leftPointer] == sub_arr[leftPointer + 1]:
                        leftPointer += 1
                    while leftPointer < rightPointer and sub_arr[rightPointer] == sub_arr[rightPointer - 1]:
                        rightPointer -= 1
                    leftPointer += 1
                    rightPointer -= 1
        return res

