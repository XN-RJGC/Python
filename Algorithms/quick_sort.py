# quick_sort.py
"""
to achieve quick sort
"""

def partition(lst, left, right):
    """
    Left and right division.
    :param lst: list
    :param left: int
    :param right: int
    :return: int
    """
    pivot = lst[left]
    part = left
    for index in xrange(left+1, right+1):
        # if pivot is greater than lst[index]
        if pivot > lst[index]:
            part += 1
            if part != index:
                # exchange
                lst[part], lst[index] = lst[index], lst[part]
    lst[left] = lst[part]
    lst[part] = pivot

    return part

def quick_sort(lst, left, right):
    """
    left = 0, right = len(lst)-1
    :param lst: list
    :param left: int
    :param right: int
    :return: list
    """
    if (right-left) >= 1:
        # divide partition
        part = partition(lst, left, right)
        # left
        quick_sort(lst, left, part-1)
        # right
        quick_sort(lst, part+1, right)

    return lst

if __name__ == '__main__':
    lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    for item in quick_sort(lst, 0, len(lst)-1):
        print item