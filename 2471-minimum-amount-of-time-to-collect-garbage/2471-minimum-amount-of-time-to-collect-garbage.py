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
        
        
        prefix_sum = [0] * (len(travel)+1)
        prefix_sum[0] = 0
        for i in range(1, len(travel)+1):
            prefix_sum[i] = prefix_sum[i-1] + travel[i-1]
        print(prefix_sum)
        if last_index_m != -1:
            total_time += prefix_sum[last_index_m]
        if last_index_p != -1:
            total_time += prefix_sum[last_index_p]
        if last_index_g != -1:
            total_time += prefix_sum[last_index_g]

        return total_time
