class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        count_0 = 0
        count_1 = s.count('1')
        max_score = 0
        for i in range(n - 1): 
            if s[i] == '0':
                count_0 += 1
            else:
                count_1 -= 1
            score = count_0 + count_1
            max_score = max(max_score, score)
        
        return max_score