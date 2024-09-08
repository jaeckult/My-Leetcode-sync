from collections import Counter

class Solution:
    def countAndSay(self, n: int) -> str:
        x = "1"
        def count(s):
            result = []
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1  
                else:
                    result.append(str(count))
                    result.append(s[i - 1])
                    count = 1  
            result.append(str(count))
            result.append(s[-1])
            return ''.join(result) 
        for _ in range(n - 1):
            x = count(x)
        
        return x
