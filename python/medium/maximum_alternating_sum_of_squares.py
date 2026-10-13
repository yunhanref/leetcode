from math import floor
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        start = 0
        if not nums:
            return 0
        self.absol_list = []
        
        for i in nums:
            self.absol_list.append(abs(i))

        self.absol_list.sort()
        absol_len = int(len(self.absol_list))
        
        if absol_len % 2 == 0:            
            sub_part_len = absol_len//2
            index = sub_part_len
            min_subpart = self.absol_list[0:index:1]
            max_subpart = self.absol_list[index::1]
            for a,b in zip(min_subpart, reversed(max_subpart)):
                result1 = start + (b**2 - a**2)
                start = result1
            return result1
        else:
            result2 = start
            sub_part_len = int(len(self.absol_list)//2)
            index = floor(sub_part_len) + 1

            min_subpart = self.absol_list[0:index:1]
            max_subpart = self.absol_list[index::1]
            for a,b in zip(min_subpart, reversed(max_subpart)):
                result2 = start + (b**2 - a**2)
                start = result2
            result2 += min_subpart[-1]**2
            return result2
