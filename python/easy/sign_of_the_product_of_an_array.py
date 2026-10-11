class Solution:
    def signFunc(self,x:int) -> int:
        if x < 0:
            return -1
        elif x == 0:
            return 0
        else:
            return 1
        
    def arraySign(self, nums: list[int]) -> int:
        #! multiply all nums return int
        start = 1
        if nums != []:
            for i in nums:
                val = i*start
                start = val

        return self.signFunc(val)