# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
# 所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = {}
        for a in A:
            for b in B:
                if (a + b) not in count:
                    count[a + b] = 1
                else:
                    count[a + b] += 1

        res = 0

        for c in C:
            for d in D:
                if (-c - d) in count:
                    res += count[-c - d]

        return res


s = Solution()
print(s.fourSumCount(A=[1, 2], B=[-2, -1], C=[-1, 2], D=[0, 2]))
