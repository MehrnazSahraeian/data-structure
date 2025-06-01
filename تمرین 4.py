class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self._tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self._tail = new_node
            new_node.next = self.head
            return
        
        self._tail.next = new_node
        new_node.next = self.head
        self._tail = new_node

    def display(self):
        if not self.head:
            return

        elements = []
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        print(elements)

    def insert_after(self, target_data, new_data):
        if not self.head:
            return False

        new_node_to_insert = Node(new_data)
        current = self.head
        found_at_least_one = False
        
        start_node = self.head 
        first_pass = True

        while True:
            if current.data == target_data:
                new_node_to_insert = Node(new_data) 
                new_node_to_insert.next = current.next
                current.next = new_node_to_insert
                
                if current == self._tail:
                    self._tail = new_node_to_insert
                
                found_at_least_one = True
                current = new_node_to_insert 
            
            current = current.next
            
            if current == start_node and not first_pass:
                break
            first_pass = False

        return found_at_least_one

    def delete_before(self, target_data):
        if not self.head or self.head.next == self.head:
            return False

        if self.head.data == target_data:
            return False

        prev = None
        current = self.head
        
        start_node = self.head
        first_pass = True

        while True:
            next_node = current.next
            
            if next_node.data == target_data:
                if current == self.head:
                    if self._tail == self.head:
                        self.head = None
                        self._tail = None
                    else:
                        temp_head = self.head.next
                        self._tail.next = temp_head
                        self.head = temp_head
                    return True
                else:
                    prev.next = next_node
                    if next_node == self.head:
                        self._tail = prev
                    return True
            
            prev = current
            current = current.next

            if current == start_node and not first_pass:
                break
            first_pass = False

        return False

    def is_empty(self):
        return self.head is None

    def replace(self, old_data, new_data):
        if not self.head:
            return False

        current = self.head
        found = False
        start_node = self.head
        first_pass = True

        while True:
            if current.data == old_data:
                current.data = new_data
                found = True
            
            current = current.next
            
            if current == start_node and not first_pass:
                break
            first_pass = False
        return found

    def is_find(self, target_data):
        if not self.head:
            return False

        current = self.head
        start_node = self.head
        first_pass = True

        while True:
            if current.data == target_data:
                return True
            
            current = current.next
            
            if current == start_node and not first_pass:
                break
            first_pass = False
        return False
