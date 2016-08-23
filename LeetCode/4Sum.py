
class Solution(object):
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[list[int]]
        """
        length = len(nums)

        result = []
        # filter out the same of results
        unique = set()
        for i in xrange(length - 2):
            if nums[i] in unique:
                continue
            else:
                unique.add(nums[i])
            j = i + 1
            k = length - 1
            while j < k:
                tsum = nums[i] + nums[j] + nums[k]
                if tsum > target:
                    k -= 1
                elif tsum < target:
                    j += 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    # whether exits
                    if temp not in result:
                        result.append(temp)
                    k -= 1
                    j += 1
        return result

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4:
            return []
        # else
        nums.sort()
        value = []
        # filter out the same of results
        unique = set()
        for i in xrange(length - 3):
            if nums[i] in unique:
                continue
            else:
                unique.add(nums[i])
            # to transform threeSum problem
            new_target = target - nums[i]
            result = self.threeSum(nums[i + 1:], new_target)
            if result is not None:
                for item in result:
                    item.append(nums[i])
                    value.append(item)
        for item in value:
            item.sort()
        return value

if __name__ == '__main__':
    solute = Solution()

    for item in solute.fourSum([-2, -1, 0, 0, 1, 2, -1], 0):
        print item
