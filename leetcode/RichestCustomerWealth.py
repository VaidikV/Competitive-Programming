class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        final_total = 0

        for arr in accounts:
            temp_total = 0
            
            for n in arr:
                temp_total += n
            
            if temp_total > final_total:
                final_total = temp_total

        return final_total
