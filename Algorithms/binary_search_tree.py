# binary_search_tree.py
"""
achieve binary search tree.
"""

class node:
    """
    Binary search tree node.
    """
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def set_data(self, data):
        self.data = data

    @property
    def get_data(self):
        return self.data

class binary_search_tree(object):
    """
    A class of binary search tree.
    """
    def __init__(self):
        self.node = None

    def construct_bst(self, lst):
        """
        Using a list to construct a bianry search tree.
        :param lst: list
        :return:
        """
        for item in lst:
            self.insert(item)

    def insert(self, data):
        """
        Insert data to binary search tree.
        :param data: int
        :return: bool
        """
        if self.node is None:
            self.node = node(data)
        else:
            pretemp = self.node
            temp = self.node
            # whether insert left or right
            sign = 0
            while temp is not None:
                # parent node
                pretemp = temp
                if  data > temp.data:  # right
                    temp = temp.right
                    sign = 1
                elif data < temp.data: # left
                    temp = temp.left
                    sign = 0
                else: # exit
                    return False
            temp = node(data)
            if sign == 1: #right
                pretemp.right = temp
            else:   #left
                pretemp.left = temp
        return True

    def remove(self, data):
        """
        Remove data from binary search tree.
        case 1: node that will reomve has no child
        case 2: node that will remove has one child
        case 3: node that will remove has two childs
        :param data: int
        :return: bool
        """
        if self.node is not None:
            pre_node = self.node
            temp = self.node
            sign = 0
            while temp is not None:
                if data > temp.data:    #right
                    pre_node = temp     #parent node
                    temp = temp.right
                    sign = 1
                elif data < temp.data:  #left
                    pre_node = temp     #parent node
                    temp = temp.left
                    sign = 0
                else:
                    if temp.left!=None and temp.right!=None: #case 3
                        right_node = temp.right
                        while right_node.left != None:
                            right_node = right_node.left
                        temp.data, right_node.data = right_node.data, temp.data
                        self.remove(data)
                    else:
                        if sign == 1:
                            if temp.right is None:
                                pre_node.right = temp.left
                            else:
                                pre_node.right = temp.right
                        else:
                            if temp.right is None:
                                pre_node.left = temp.left
                            else:
                                pre_node.left = temp.right
                        return True
            return False
        else:
            return False

    def output(self):
        """
        Output data with level visit.
        :return:
        """
        if self.node is None:
            return
        queue = []
        queue.append(self.node)
        while len(queue) != 0:
            node = queue[0]
            queue.pop(0)
            print node.data
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

if __name__ == '__main__':
    bst = binary_search_tree()

    lst = [3, 2, 1, 4, 5, 9, 8, 7, 6]
    bst.construct_bst(lst)
    bst.remove(1)

    bst.output()