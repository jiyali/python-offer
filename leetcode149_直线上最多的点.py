class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(points)
        if n < 3:
            return n

        for i in range(n):
            dic = {}
            same_point = 0
            val = 0
            for j in range(i + 1, n):
                if self.samePoint(points[i], points[j]):
                    same_point += 1
                    continue
                k = self.get_slope(points[i], points[j])
                # print('1', k)
                if k not in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1
                val = max(val, dic[k])
            # print(val)
            res = max(res, val + same_point)
        return res + 1

    def get_slope(self, p_a, p_b):
        # print('hhh0', p_a)
        # print('hhh0', p_b)
        if p_a[0] - p_b[0] == 0:
            return None
        return 10.0 * (p_a[1] - p_b[1]) / (p_a[0] - p_b[0])

    def samePoint(self, p_a, p_b):
        if (p_a[0] - p_b[0]) == (p_a[1] - p_b[1]) == 0:
            return True


s = Solution()
print(s.maxPoints([[1,1],[1,1],[1,1]]))
