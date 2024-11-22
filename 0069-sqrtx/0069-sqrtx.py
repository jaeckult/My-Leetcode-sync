class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        low, high = 1, x
        result = 0  

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:  
                return mid
            elif mid * mid < x:  
                result = mid 
                low = mid + 1
            else:  
                high = mid - 1

        return result
