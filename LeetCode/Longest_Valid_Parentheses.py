# coding:utf-8
"""
题目描述（url:https://leetcode.com/problems/longest-valid-parentheses/）:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For example:
(1)、"(()", the longest valid parentheses substring is "()", which has length = 2.
(2)、")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        # else
        stack = [] # store the index of '(' in s
        stack.append(-1)
        result = 0
        index = 0
        while index < length:
            #if s[index] == '(':
                # append the index of '(' in s
            #    stack.append(index)
            if s[index] == ')' and stack[-1]!=-1 and s[stack[-1]]=='(':
                    stack.pop()
                    #print index, stack[-1]
                    result = max(result, index-stack[-1])
            else:
                stack.append(index)
            index += 1
        return result

if __name__ == '__main__':
    solute = Solution()

    print solute.longestValidParentheses('(()))())(')
