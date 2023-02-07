class Solution:
    def isValid(self, s: str) -> bool:
        sym = [""]
        bracs = {')':'(',']':'[','}':'{'}

        for i in s:
            if i in bracs:
                if sym.pop() != bracs[i]:
                    return False
            else:
                sym.append(i)
                
        return len(sym) == 1
    
