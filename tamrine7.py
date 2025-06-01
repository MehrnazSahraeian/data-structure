class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right
            else: # Duplicate data, do nothing or handle as per requirement
                return

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else: # Node with matching data found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._find_min_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)
        return node

    def count_leaves(self):
        return self._count_leaves_recursive(self.root)

    def _count_leaves_recursive(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves_recursive(node.left) + self._count_leaves_recursive(node.right)

    def count_degree_one_nodes(self):
        return self._count_degree_one_nodes_recursive(self.root)

    def _count_degree_one_nodes_recursive(self, node):
        if node is None:
            return 0
        
        count = 0
        if (node.left is not None and node.right is None) or \
           (node.left is None and node.right is not None):
            count = 1
        
        return count + self._count_degree_one_nodes_recursive(node.left) + \
               self._count_degree_one_nodes_recursive(node.right)

    def count_degree_two_nodes(self):
        return self._count_degree_two_nodes_recursive(self.root)

    def _count_degree_two_nodes_recursive(self, node):
        if node is None:
            return 0
        
        count = 0
        if node.left is not None and node.right is not None:
            count = 1
        
        return count + self._count_degree_two_nodes_recursive(node.left) + \
               self._count_degree_two_nodes_recursive(node.right)

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def replace(self, old_data, new_data):
        if not self.search(old_data):
            return False # Old data not found

        # First, delete the old data
        self.delete(old_data)
        
        # Then, insert the new data
        self.insert(new_data)
        return True

    def inorder_traversal(self): # Helper for verification
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node is not None:
            self._inorder_recursive(node.left, elements)
            elements.append(node.data)
            self._inorder_recursive(node.right, elements)
