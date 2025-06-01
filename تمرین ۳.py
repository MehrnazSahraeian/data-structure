class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    def insert_after(self, target_data, new_data):
        if not self.head:
            return

        current = self.head
        found_at_least_one = False
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                found_at_least_one = True
                current = new_node.next
            else:
                current = current.next
        return found_at_least_one

    def delete_before(self, target_data):
        if not self.head or self.head.data == target_data:
            return False

        if self.head.next and self.head.next.data == target_data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next and current.next.next:
            if current.next.next.data == target_data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def is_empty(self):
        return self.head is None

    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return True
            current = current.next
        return False

    def is_find(self, target_data):
        current = self.head
        while current:
            if current.data == target_data:
                return True
            current = current.next
        return False
