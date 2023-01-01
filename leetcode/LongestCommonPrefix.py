class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest_pref = min(strs, key=len)

        for item in strs:
            while len(shortest_pref) > 0:
                if item.startswith(shortest_pref):
                    break
                else:
                    shortest_pref = shortest_pref[:-1]
        return shortest_pref
