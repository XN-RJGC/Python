
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        # if the len of nums less than 3
        if length < 3:
            return 0
        # else
        tsum = nums[0] + nums[1] + nums[2]
        # sort
        nums.sort()
        # the max value of i is equal len(nums)-2
        for i in xrange(length-2):
            j = i+1
            k = length-1
            while j < k:
                value_sum = nums[i] + nums[j] + nums[k]
                # if value_sum is closer than tsum of target
                if abs(target-tsum) > abs(target-value_sum):
                    tsum = value_sum
                # look for the next set of data
                if value_sum < target:
                    j += 1
                elif value_sum > target:
                    k -= 1
                else:
                    j += 1
                    k -= 1
        return tsum

if __name__ == '__main__':
    solute = Solution()

    print solute.threeSumClosest([-1, 2, 1, -4], 1)