from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_time = 0
        last_index_m = last_index_p = last_index_g = -1
        n = len(garbage)
        for i in range(n):
            total_time += len(garbage[i]) 
            
            if 'M' in garbage[i]:
                last_index_m = i
            if 'P' in garbage[i]:
                last_index_p = i
            if 'G' in garbage[i]:
                last_index_g = i
        for i in range(last_index_m):
            total_time += travel[i]
        for i in range(last_index_p):
            total_time += travel[i]
        for i in range(last_index_g):
            total_time += travel[i]

        return total_time

