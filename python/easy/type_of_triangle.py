class Solution:
    def triangleType(self, nums:list[int]) -> str:
        #! is triangle
        is_triangle = False
        if (nums[0] + nums[1] > nums[2])and(nums[0] + nums[2] > nums[1])and(nums[1] + nums[2] > nums[0]):
            print("is triangle")
            is_triangle = True
        else:
            print("not a triangle")
        
        #! TYPE
        while is_triangle:
            #! is equiliteral?
            if nums[0] == nums [1] == nums [2]:
                print("TYPE: EQUILITERAL")
                break
            #! is isosceles?
            elif (nums [0] == nums[1] and nums[0] != nums[2]) or (nums[0] == nums[2] and nums[0] != nums[1]) or (nums[1] == nums[2] and nums[1] != nums[0]):
                print("TYPE: ISOSCELES")
                break
            #! is scalane?
            elif nums[0] != nums[1] and nums[0] != nums[2]:
                print("TYPE: SCALANE")
                break
            else:
                print("TYPE: ERROR")
                break
sol = Solution()
sol.triangleType(nums=[3,4,313131311])