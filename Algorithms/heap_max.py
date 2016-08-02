# heap_max.py
"""
achieve max-heap
"""

class heap(object):
    """
    A class of max-heap.
    """
    def __init__(self):
        # Using a list to store data.
        self.heap_list = []

    def construct_max_heap(self, lst):
        """
        # Using a list to construct a max-heap.
        :param lst: list
        :return: bool
        """
        self.heap_list = lst
        #start compare node
        node = (len(self.heap_list)-2)/2
        while node >= 0:
            self.sift_down(node, len(self.heap_list)-1)
            node -= 1

    def sift_down(self, start, end):
        """
        # Adjust heap from top to bottom.
        :param start: int
        :param end: int
        :return:
        """
        i, j = start, 2*start+1
        # Temporary variable to decrease exchange times
        temp = self.heap_list[start]
        # end is equal to len(self.heap_list)-1
        while j <= end:
            # compare left child node with right child node
            if j<end and self.heap_list[j]<self.heap_list[j+1]:
                j += 1
            if temp >= self.heap_list[j]:
                break
            else:
                #self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]
                self.heap_list[i] = self.heap_list[j]
                i = j
                j = 2*j+1
        self.heap_list[i] = temp

    @property
    def get_list(self):
        """
        Get self.heap_list.
        :return: list
        """
        return self.heap_list

    def sift_up(self, start):
        i = start
        j = (i-1)/2
        # Temporary variable to decrease exchange times
        temp = self.heap_list[start]
        # end condition
        while j >= 0:
            if temp <= self.heap_list[j]:
                break
            # not have to compare left child node with right child node
            else:
                self.heap_list[i] = self.heap_list[j]
                i = j
                j = (j-1)/2
        self.heap_list[i] = temp

    def insert(self, data):
        """
        # Insert data to max-heap'end.
        :param data: int
        :return: bool
        """
        # add data to list'end
        self.heap_list.append(data)
        # adjust max-heap from bottom to top
        self.sift_up(len(self.heap_list)-1)

    @property
    def remove(self):
        """
        # Remove top data from max-heap.
        :return: bool
        """
        length = len(self.heap_list)
        if length == 0:
            return False
        elif length == 1:
            self.heap_list.pop()
            return True
        else:
            # exchange last data with top data and remove last data
            self.heap_list[0] = self.heap_list[length-1]
            self.heap_list.pop()
            # adjust max-heap from top to bottom
            self.sift_down(0, len(self.heap_list)-1)
            return True


if __name__ == '__main__':
    # heap instance object
    max_heap = heap()
    # construct a max-heap
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    max_heap.construct_max_heap(lst)

    # output max-heap
    for item in max_heap.heap_list:
        print item,

    print
    # remove data from max-heap
    max_heap.remove
    for item in max_heap.heap_list:
        print item,

    print
    # insert data to max-heap
    max_heap.insert(10)
    max_heap.insert(0)
    for item in max_heap.heap_list:
        print item,
