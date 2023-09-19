# Array / String
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        m = len(flowerbed)
        count = 0
        i = 0

        while i < m:
            if flowerbed[i] == 0 and (i == 0 or 
            flowerbed[i-1] == 0) and (i == m - 1 or 
            flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
            i += 1
        return count >= n
        