class Solution:
    def maxScore(self, s: str) -> int:

        # Total count of '1's in the string
        total_ones = s.count('1')
        max_score = 0
        left_zeros = 0
        
        # Iterate through the string except for the last character
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                total_ones -= 1
            
            # Calculate score for the current split
            current_score = left_zeros + total_ones
            max_score = max(max_score, current_score)
        
        return max_score
# 4:04AM january 1, 2025. Abrehot Library.
