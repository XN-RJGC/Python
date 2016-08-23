
class Solution(object):
    def match(self, s, dict, length):
        """
        :type s: str
        :type dict: dict
        :type length: int
        :rtype: bool
        """
        index = 0
        while index <= len(s) - length:
            # split and match
            sub_str = s[index:index + length]
            # sub_str exits in dict
            if sub_str in dict and dict[sub_str] != 0:
                dict[sub_str] -= 1
            # sub_str is not exits in dict
            else:
                return False
            index += length
        return True

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        length = len(words)
        if length == 0:
            return []
        # else
        # storing words of dict
        dict_words = {}
        for item in words:
            if item in dict_words:
                dict_words[item] += 1
            else:
                dict_words[item] = 1
        # item of words' length
        words_length = len(words[0])
        # length of s
        s_length = len(s)
        index = 0
        result = []
        # match
        while index <= s_length - words_length * length:
            temp_dict = dict_words.copy()
            #
            if self.match(s[index:index + words_length * length], temp_dict, words_length):
                result.append(index)
            index += 1
        return result

if __name__ == '__main__':
    solute = Solution()

    for item in solute.findSubstring('barfoothefoobarthe', ["foo", "bar"]):
        print item
