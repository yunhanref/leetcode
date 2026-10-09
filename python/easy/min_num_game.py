def quick_sort(nums: list[int]) -> list[int]:
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
    
    return quick_sort(left_side) + [nums[small_ptr_ind]] + quick_sort(right_side)

class Solution():
    def numberGame(self, nums: list[int]) -> list[int]:
        nums = quick_sort(nums)
        output = []
        iteration = int(len(nums)/2)
        for i in range(iteration):
            if len(nums) > 0:
                bob_takes = nums[1]
                output.append(bob_takes)
                nums.pop(1)
            else:
                pass
            alice_takes = nums[0]
            output.append(alice_takes)
            nums.pop(0)

        return output
