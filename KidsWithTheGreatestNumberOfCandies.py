class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        maxCandies = max(candies)

        for i in range(len(candies)):            
            result.append(candies[i] + extraCandies >= maxCandies)
        return result 