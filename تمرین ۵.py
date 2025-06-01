class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self._tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self._tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            new_node.next = self.head
            self.head.prev = new_node
            self._tail = new_node
        self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self._tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self._tail
            self._tail.next = new_node
            self.head = new_node
        self.size += 1

    def display(self):
        if self.is_empty():
            return
        elements = []
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        print(elements)

    def display_reverse(self):
        if self.is_empty():
            return
        elements = []
        current = self._tail
        while True:
            elements.append(current.data)
            current = current.prev
            if current == self._tail:
                break
        print(elements)

    def delete_after(self, target_data):
        if self.is_empty():
            return False

        if self.size == 1:
            if self.head.data == target_data:
                return False
            else:
                return False

        current = self.head
        start_node = self.head

        while True:
            if current.data == target_data:
                node_to_delete = current.next
                
                if node_to_delete == self.head:
                    if self.size == 1:
                        self.head = None
                        self._tail = None
                    else:
                        self._tail = current
                        self._tail.next = self.head
                        self.head.prev = self._tail
                else:
                    current.next = node_to_delete.next
                    node_to_delete.next.prev = current
                
                self.size -= 1
                return True

            current = current.next
            if current == start_node:
                break
        return False

    def delete_before(self, target_data):
        if self.is_empty():
            return False

        if self.size == 1:
            return False

        current = self.head
        start_node = self.head

        while True:
            if current.data == target_data:
                node_to_delete = current.prev
                
                if node_to_delete == self.head:
                    if self.size == 1:
                        self.head = None
                        self._tail = None
                    else:
                        self.head = self.head.next
                        self.head.prev = self._tail
                        self._tail.next = self.head
                elif node_to_delete == self._tail:
                    self._tail = self._tail.prev
                    self._tail.next = self.head
                    self.head.prev = self._tail
                else:
                    node_to_delete.prev.next = node_to_delete.next
                    node_to_delete.next.prev = node_to_delete.prev
                
                self.size -= 1
                return True

            current = current.next
            if current == start_node:
                break
        return False

    def delete_x(self, x_data):
        if self.is_empty():
            return False

        current = self.head
        found = False
        
        if self.size == 1 and self.head.data == x_data:
            self.head = None
            self._tail = None
            self.size = 0
            return True

        nodes_to_delete = []

        start_node = self.head
        first_pass = True

        while True:
            if current.data == x_data:
                nodes_to_delete.append(current)
                found = True
            
            if current.next == start_node and not first_pass:
                break
            
            current = current.next
            first_pass = False

        if not found:
            return False

        for node_to_remove in nodes_to_delete:
            if self.size == 0:
                break

            if node_to_remove == self.head and self.size == 1:
                self.head = None
                self._tail = None
            elif node_to_remove == self.head:
                self.head = self.head.next
                self._tail.next = self.head
                self.head.prev = self._tail
            elif node_to_remove == self._tail:
                self._tail = self._tail.prev
                self._tail.next = self.head
                self.head.prev = self._tail
            else:
                node_to_remove.prev.next = node_to_remove.next
                node_to_remove.next.prev = node_to_remove.prev
            
            self.size -= 1

        return True
