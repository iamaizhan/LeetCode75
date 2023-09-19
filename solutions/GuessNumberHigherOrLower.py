# Binary Search

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    picked_number = input(int())
    if num < picked_number:
        return 1
    elif num > picked_number:
        return -1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while True:
            middle = (left + right) // 2            
            result = guess(middle)
            if result > 0:
                left = middle + 1
            elif result < 0:
                right = middle - 1
            else:
                return middle
