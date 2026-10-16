class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        index = 0
        for i in nums:
            nums[index] = i**2
            index += 1
        nums.sort()
        return nums