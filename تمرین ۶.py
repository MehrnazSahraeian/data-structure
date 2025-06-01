class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

class GeneralTree:
    def __init__(self):
        self.root = None

    def level_order(self):
        if not self.root:
            return []

        result = []
        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            current_node = q.dequeue()
            result.append(current_node.data)

            for child in current_node.children:
                q.enqueue(child)
        return result
