class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total_sum = int(a, 2) + int(b, 2)
        if total_sum == 0:
            return "0"
        result = ""
        return self.helper(total_sum, result)
    
    def helper(self, total_sum, result):
        if total_sum == 0:
            return result[::-1] 
        rem = total_sum % 2  
        result += str(rem) 
        return self.helper(total_sum // 2, result)