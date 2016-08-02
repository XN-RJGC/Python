# heap_sort.py
"""
using max-heap to sort
"""
import heap_max

def sort(lst):
    """
    Using max-heap to sort lst.
    :param lst: list
    :return: list
    """
    # make max-heap
    max_heap = heap_max.heap()
    max_heap.construct_max_heap(lst)
    # heap sort
    for i in xrange(len(lst)-1, 0, -1):
        # exchange data
        max_heap.heap_list[0], max_heap.heap_list[i] = max_heap.heap_list[i], max_heap.heap_list[0]
        max_heap.sift_down(0, i-1)
    # max_heap is not a max-heap anymore.
    return max_heap.get_list

if __name__ == '__main__':
    lst = [9, 3, 4, 7, 1, 2, 5, 6, 8, 10]

    for item in sort(lst):
        print item