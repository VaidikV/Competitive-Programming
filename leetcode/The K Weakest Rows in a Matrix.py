class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        for i in mat:
            result.append(sum(i))

        answer = []
        for j in sorted(result):
            x = result.index(j)
            answer.append(x)
            result[x] = -1
        return answer[0:k]
