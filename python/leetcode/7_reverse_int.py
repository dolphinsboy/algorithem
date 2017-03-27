class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = x if x > 0 else -x
        w = 0
        while y:
            w += y%10
            y = y/10
            w *= 10
        w = w/10 if x > 0 else -w/10
        if w >0 and w < 2147483648:
            return w
        elif w<0 and w>-2147483648:
            return w
        else:
            return 0


s = Solution()
print s.reverse(123)
print s.reverse(-123)
print s.reverse(1534236469)

