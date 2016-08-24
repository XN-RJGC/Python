# coding:utf-8
"""
题目描述(url:https://leetcode.com/problems/valid-sudoku/):

There are just 3 rules to Sudoku:
    (1) Each row must have the numbers 1-9 occuring just once.
    (2) Each column must have the numbers 1-9 occuring just once.
    (3) And the numbers 1-9 must occur just once in each of the 9 sub-boxes of the grid.

description:
The Sudoku board could be partially filled, where empty cells are filled with the character '.'

for example:
test data: [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
return True
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # rows
        i = 0
        while i < 9:
            j = 0
            d = {}
            while j < 9:
                if board[i][j] != '.' and board[i][j] in d:
                    return False
                else:
                    d[board[i][j]] = True
                j += 1
            i += 1
        # columns
        i = 0
        while i < 9:
            j = 0
            d = {}
            while j < 9:
                if board[j][i] != '.' and board[j][i] in d:
                    return False
                else:
                    d[board[j][i]] = True
                j += 1
            i += 1
        # the 9 sub-boxes of the grid
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                m = 0
                d = {}
                while m < 3:
                    n = 0
                    while n < 3:
                        if board[i + m][j + n] != '.' and board[i + m][j + n] in d:
                            return False
                        else:
                            d[board[i + m][j + n]] = True
                        n += 1
                    m += 1
                j += 3
            i += 3

        return True

if __name__ == '__main__':
    solute = Solution()

    print solute.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
