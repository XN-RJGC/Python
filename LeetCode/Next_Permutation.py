# url:https://leetcode.com/problems/next-permutation/

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # find the number of nums can increase from nums'right
        index = length - 2
        while (index >= 0) and (nums[index] >= nums[index + 1]):
            index -= 1
        # not find
        if index < 0:
            nums.reverse()
        # finded
        else:
            # find number greater than nums[index]
            index_1 = length - 1
            while (index_1 >= 0) and (nums[index] >= nums[index_1]):
                index_1 -= 1
            # swap nums[index] and nums[index_1]
            nums[index], nums[index_1] = nums[index_1], nums[index]
            # reverse nums[index+1:]
            i = index + 1
            j = length - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

if __name__ == '__main__':
    solute = Solution()

    nums = [1, 2, 3, 4, 5]
    solute.nextPermutation(nums)

    print nums