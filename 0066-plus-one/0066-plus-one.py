from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[n - 1] += 1  # Increment the last digit
        
        for i in range(n - 1, -1, -1):  # Start from the last digit and move backwards
            if digits[i] == 10:  # If the current digit is 10, we have a carry
                digits[i] = 0  # Set current digit to 0
                if i - 1 >= 0:  # Check if there is a next digit to carry to
                    digits[i - 1] += 1
                else:
                    # If we are at the first digit and it rolled over, we need to insert '1' at the start
                    digits.insert(0, 1)
        
        return digits

#4:27AM January 1, 2025. Abrehot Library. 
