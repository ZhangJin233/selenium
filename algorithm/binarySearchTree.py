class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        temp = self.root
        if self.root is None:
            self.root = new_node
            return True
        while True:
            if temp.value == new_node.value:
                return False
            if new_node.value > temp.value:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self,value):
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            if value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return False






my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))
print(my_tree.contains(17))


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
