class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n or k == 0:
            return []

        res = []

        def backtrack(start=1, tmp=[]):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            for i in range(start, n + 1):
                tmp.append(i)
                backtrack(i + 1, tmp)
                tmp.pop()

        backtrack()

        return res
