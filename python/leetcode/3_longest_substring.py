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

def main():
    s = Solution()
    #case = ["abcabcbb", "bbbbb", "pwwkew"]
    case = ["abcabcbb"]
    for d in case:
        s.lengthOfLongestSubstring(d)

if __name__ == '__main__':
    main()
