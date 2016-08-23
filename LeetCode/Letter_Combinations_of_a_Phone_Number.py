
class Solution(object):
    def add_digits(self, digits, lst):
        """
        :type digits: str
        :type lst: List[str]
        :rtype: List[str]
        """
        temp = []
        for item in digits:
            # if lst is empty
            if len(lst) == 0:
                temp.append(item)
            # else
            for s in lst:
                temp.append(s + item)
        return temp

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # storing
        store = {
            '1': "*",
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
            '0': ' '
        }

        lst = []
        for item in digits:
            lst = self.add_digits(store[item], lst)

        lst.sort()
        return lst

if __name__ == '__main__':
    solute = Solution()

    for item in solute.letterCombinations('12345'):
        print item,
