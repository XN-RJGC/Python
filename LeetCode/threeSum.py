# threeSum.py
"""
to solute threeSum problem of leetcode
"""

def threeSum(self, nums):
    """
    a + b + c = 0
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # sort
    nums.sort()
    length = len(nums)
    result = []
    # get unique list
    unique = set()
    for i in xrange(length):
        # if nums[i] exist in unique
        if nums[i] in unique:
            continue
        else:
            unique.add(nums[i])
        j = i + 1
        k = length - 1
        # get unique nums[j]
        unique_local = set()
        while k > j:
            unique_local.add(nums[j])
            # when need j+=1: sign = 1
            sign = 0
            if (nums[j] + nums[k]) < -nums[i]:
                j += 1
                sign = 1
            elif (nums[j] + nums[k]) > -nums[i]:
                k -= 1
            else: #nums[j] + nums[k] == -nums[i]
                lst = [nums[i], nums[j], nums[k]]
                result.append(lst)
                j += 1
                k -= 1
                sign = 1
            if sign == 1:
                # if nums[j] in unique_local: j++
                while j < length and nums[j] in unique_local:
                    j += 1
    return result