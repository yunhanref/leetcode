from math import acos, degrees


class Solution:

    def quick_sort(self,nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        border = len(nums) - 1
        pivot = nums[border]
        small_ptr_ind = -1
        
        for big_ptr_ind in range(border): 
            if nums[big_ptr_ind] >= pivot:
                pass 
            else:
                small_ptr_ind += 1
                nums[small_ptr_ind], nums[big_ptr_ind] = nums[big_ptr_ind], nums[small_ptr_ind]

        small_ptr_ind += 1
        nums[small_ptr_ind], nums[border] = nums[border], nums[small_ptr_ind]
        
        left_side = nums[:small_ptr_ind]
        right_side = nums[small_ptr_ind + 1:]
        
        return self.quick_sort(left_side) + [nums[small_ptr_ind]] + self.quick_sort(right_side)
    
    def internalAngles(self, sides: list[int]) -> list[float]:
        is_triangle = False
        if (sides[0] + sides[1] > sides[2])and(sides[0] + sides[2] > sides[1])and(sides[1] + sides[2] > sides[0]):
            print("is triangle")
            is_triangle = True
        if not is_triangle:
            print("not a triangle")
            return []
        if is_triangle:
            angle_a = degrees(acos(float((sides[1]**2 + sides[2]**2 - sides[0]**2)/ (2*sides[1]*sides[2]))))
            angle_b = degrees(acos(float((sides[0]**2 + sides[2]**2 - sides[1]**2)/ (2*sides[0]*sides[2]))))
            angle_c = degrees(acos(float((sides[0]**2 + sides[1]**2 - sides[2]**2)/ (2*sides[0]*sides[1]))))

        return self.quick_sort([angle_a,angle_b,angle_c])
sol = Solution()
print(sol.internalAngles([3,4,5]))
