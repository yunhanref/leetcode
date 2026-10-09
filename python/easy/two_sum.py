class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        C_pointer = 0
        M_pointer = C_pointer + 1
        
        while C_pointer < len(nums) - 1:
            if M_pointer <= len(nums) - 1:
                if nums[C_pointer] + nums[M_pointer] == target:
                    return [C_pointer, M_pointer]
                else:
                    M_pointer += 1
            else:
                C_pointer += 1
                M_pointer = C_pointer + 1

twosum = Solution()
print(twosum.twoSum(nums=[123,123,123,3,23,23,13,21,31,23,12,31,3,123,3,32,3,2,32,32,33,2,3], target=246))