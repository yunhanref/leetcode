
import math

class Solution:

    def native_reader(self, num: int):
        front_e_var = len(str(num)) - 1
        front_list = []
        if num == 0:
            print("num is 0")
            front_list = [0]
            return front_list
        else:
            while front_e_var >= 0:
                front_remainder = num // 10**front_e_var
                front_list.append(front_remainder)
                num = num - (front_remainder * 10**front_e_var)
                front_e_var -= 1

            print(front_list)
            return front_list

    def reverse_reader(self, num):
        reverse_list = []
        if num == 0:
            print("num is 0")
            reverse_list = [0]
            return reverse_list
        else:
            while num >= 1:
                back_remainder = num % 10
                reverse_list.append(back_remainder)
                num = num // 10

            print(reverse_list)
            return reverse_list

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = self.reverse_reader(x)
        nat = self.native_reader(x)
        if rev == nat:
            print("yes")
            return True
        else:
            print("no")
            return False


read = Solution()
print(read.isPalindrome(10))