class Solution:
    def sumFourDivisors(self, nums):
        if not nums:
            return 0

        sum_ = 0

        for num in nums:
            res = set()
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    res.add(i)
                    res.add(num // i)
                if len(res) > 4:
                    break
            if len(res) == 4:
                sum_ += sum(res)
        return sum_


s = Solution()
print(s.sumFourDivisors([7286, 18704, 70773, 8224, 91675]))
