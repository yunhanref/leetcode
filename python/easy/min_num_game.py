def quick_sort(nums: list[int]) -> list[int]:
    """
    1) Choose pivot and specify ptr_small ptr_big
    2) Let ptr_big iterate over array len(array)-2 times, check if indexval>pivot
    3) Then sort left and right side of the sub-arrays next to newly replaced pivot.
    4) Continue until everything is sorted. 
    """
    # TEMEL DURUM (Base Case): 
    # Eğer liste 1 elemanlıysa veya boşsa zaten sıralıdır, işlemi bitir ve listeyi döndür.
    if len(nums) <= 1:
        return nums

    # * OPTION ONE (Başlangıç Değerleri)
    border = len(nums) - 1
    pivot = nums[border] # pivot her zaman son eleman
    small_ptr_ind = -1
    
    # * OPTION TWO (Bölümleme - Partitioning)
    for big_ptr_ind in range(border): 
        if nums[big_ptr_ind] >= pivot:
            # Eleman pivot'tan büyükse hiçbir şey yapma, aramaya devam et
            pass 
        else:
            # Eleman pivot'tan küçükse small_ptr_ind'i artır ve değerleri takas et (SWAP)
            small_ptr_ind += 1
            nums[small_ptr_ind], nums[big_ptr_ind] = nums[big_ptr_ind], nums[small_ptr_ind]
            
    # Döngü bittiğinde pivot'u gerçek ve nihai yerine koy
    # Nihai yer, küçük olanların bittiği yerin bir fazlasıdır (small_ptr_ind + 1)
    small_ptr_ind += 1
    nums[small_ptr_ind], nums[border] = nums[border], nums[small_ptr_ind]
    
    # * ADIM 3 ve 4: Alt dizileri ayır ve kendini tekrar çağır (Recursion)
    # Pivot artık doğru yerinde. Pivotun solundaki ve sağındaki listeleri alalım:
    left_side = nums[:small_ptr_ind]
    right_side = nums[small_ptr_ind + 1:]
    
    # Sol tarafı sırala + pivotu araya koy + sağ tarafı sırala
    return quick_sort(left_side) + [nums[small_ptr_ind]] + quick_sort(right_side)

class Solution():
    def numberGame(self, nums: list[int]) -> list[int]:
        nums = quick_sort(nums)
        output = []
        iteration = int(len(nums)/2) #6/2= 3 iteration
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
sol = Solution()
print(sol.numberGame([4, 5, 1, 2, 3, 9, 6, 8, 7]))

#! SELF MADE QUICK SORT ALGORITHM
''' 
def semisort(nums:list[int]) -> list[int]:
    
    #1)choose pivot and specify ptr_small ptr_big
    #2)let ptr_big iterate over array len(array)-2 times, check if indexval>pivot
    #    a) if indexval >= pivot continue iterating until the end.
    #    b) else: increment ptr_big by one, swap values of both pointers. Continue
    #    c) if reached end, replace pivot with value next to ptr_big (ptr_big + 1)
    #3) then sort left and right side of the sub-arrays next to newly replaced pivot.
    #4) continue until everything is sorted. 
    
    #* OPTION ONE
    border = len(nums) - 1
    pivot_ind = border
    pivot = nums[pivot_ind] #pivot = last index of pivot
    big_ptr_ind = 0
    small_ptr_ind = -1
    #ptr_small_value = nums[small_ptr_ind]
    #ptr_big_value = nums[big_ptr_ind]
    

    #* OPTION TWO
    if big_ptr_ind < border:
        
        for big_ptr_ind in range(border):
            
            if nums[big_ptr_ind] >= pivot:
                print("(ptr_big) no problem, continuing the search")
                big_ptr_ind += 1
            
            else:
                print("(ptr_big) found a value smaller than the pivot")
                small_ptr_ind += 1
                
                #? SWAP NASIL YAPILIR? INDICES STAY SAME, POINTER VALUES TAKE INDICES VALUE
                #INEFFICIENT WAY
                #nums[small_ptr_ind] = ptr_big_value
                #nums[big_ptr_ind] = ptr_small_value
                #CORRECT WAY
                nums[small_ptr_ind], nums[big_ptr_ind] = nums[big_ptr_ind], nums[small_ptr_ind]
        small_ptr_ind += 1
        nums[small_ptr_ind], nums[border] = nums[border], nums[small_ptr_ind]
    return nums #! return semi-sorted list after reaching border.

print(semisort([4,5,1,2,3]))


def partitionsort():
    #? Take the semisorted output and pivot index.
    #? Sort left and right side of the pivot the same way.
    pass
'''

#! GEMINI CORRECTEDSELF MADE QUICK SORT ALGORITHM
''' 
def quick_sort(nums: list[int]) -> list[int]:
    """
    1) Choose pivot and specify ptr_small ptr_big
    2) Let ptr_big iterate over array len(array)-2 times, check if indexval>pivot
    3) Then sort left and right side of the sub-arrays next to newly replaced pivot.
    4) Continue until everything is sorted. 
    """
    # TEMEL DURUM (Base Case): 
    # Eğer liste 1 elemanlıysa veya boşsa zaten sıralıdır, işlemi bitir ve listeyi döndür.
    if len(nums) <= 1:
        return nums

    # * OPTION ONE (Başlangıç Değerleri)
    border = len(nums) - 1
    pivot = nums[border] # pivot her zaman son eleman
    small_ptr_ind = -1
    
    # * OPTION TWO (Bölümleme - Partitioning)
    for big_ptr_ind in range(border): 
        if nums[big_ptr_ind] >= pivot:
            # Eleman pivot'tan büyükse hiçbir şey yapma, aramaya devam et
            pass 
        else:
            # Eleman pivot'tan küçükse small_ptr_ind'i artır ve değerleri takas et (SWAP)
            small_ptr_ind += 1
            nums[small_ptr_ind], nums[big_ptr_ind] = nums[big_ptr_ind], nums[small_ptr_ind]
            
    # Döngü bittiğinde pivot'u gerçek ve nihai yerine koy
    # Nihai yer, küçük olanların bittiği yerin bir fazlasıdır (small_ptr_ind + 1)
    small_ptr_ind += 1
    nums[small_ptr_ind], nums[border] = nums[border], nums[small_ptr_ind]
    
    # * ADIM 3 ve 4: Alt dizileri ayır ve kendini tekrar çağır (Recursion)
    # Pivot artık doğru yerinde. Pivotun solundaki ve sağındaki listeleri alalım:
    left_side = nums[:small_ptr_ind]
    right_side = nums[small_ptr_ind + 1:]
    
    # Sol tarafı sırala + pivotu araya koy + sağ tarafı sırala
    return quick_sort(left_side) + [nums[small_ptr_ind]] + quick_sort(right_side)


# Test edelim
ornek_liste = [4, 5, 1, 2, 3, 9, 6, 8, 7]
print("Sorted list:", quick_sort(ornek_liste))
''' 