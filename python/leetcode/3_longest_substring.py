#!/usr/bin/env python

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        not_repeated_str = []
        for c in s:
            if c not in not_repeated_str:
                not_repeated_str.append(c)

        ret = []
        for i in s:
            arr = []
            for j in not_repeated_str:
                if i == j:
                    arr.append(1)
                else:
                    arr.append(0)
            ret.append(arr)

        longest_sub_dict = {}

        r = len(ret)
        c = len(not_repeated_str)
        longtest = []
        for i in range(r):
            for j in range(c):
                m = i
                n = j
                tmp = 0
                while m < r and n < c:
                    if ret[m][n]:
                        tmp += 1
                    n = n + 1
                    m = m + 1
                longtest.append(tmp)
        return max(longtest) if longtest else 0
def main():
    s = Solution()
    case = ["abcabcbb", "bbbbb", "pwwkew", "dvdf", ""]
    #case = ["dvdf"]
    for d in case:
        print d
        print s.lengthOfLongestSubstring(d)

if __name__ == '__main__':
    main()
