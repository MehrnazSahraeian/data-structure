class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTreeOperations:
    def __init__(self):
        self.root = None

    def count_leaves_recursive(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves_recursive(node.left) + self.count_leaves_recursive(node.right)

    def count_degree_one_nodes_recursive(self, node):
        if node is None:
            return 0
        
        count = 0
        is_degree_one = (node.left is not None and node.right is None) or \
                        (node.left is None and node.right is not None)
        
        if is_degree_one:
            count = 1
        
        return count + self.count_degree_one_nodes_recursive(node.left) + \
               self.count_degree_one_nodes_recursive(node.right)

    def count_degree_two_nodes_recursive(self, node):
        if node is None:
            return 0
        
        count = 0
        if node.left is not None and node.right is not None:
            count = 1
        
        return count + self.count_degree_two_nodes_recursive(node.left) + \
               self.count_degree_two_nodes_recursive(node.right)
