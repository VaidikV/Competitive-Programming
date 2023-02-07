class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ex = {"IV": 2, "IX": 2, "XL": 20, "XC": 20, "CD": 200, "CM": 200}

        tot = 0

        for i in s:
            tot += rom_to_int[i]

        for n in ex:
            if n in s:
                tot -= ex[n]
        
        return tot
                    
