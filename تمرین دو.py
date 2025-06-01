class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            return False
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def get_size(self):
        return self.size

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def display(self):
        if self.is_empty():
            return
        elements = []
        for i in range(self.size):
            index = (self.head + i) % self.capacity
            elements.append(self.queue[index])
        print(elements)

    def replace(self, old_item, new_item):
        if self.is_empty():
            return False

        current = self.head
        for _ in range(self.size):
            if self.queue[current] == old_item:
                self.queue[current] = new_item
                return True
            current = (current + 1) % self.capacity
        return False

    def show_v(self, count):
        if self.is_empty():
            return

        if count <= 0:
            return

        elements_to_show = []
        num_to_display = min(count, self.size)
        
        current = self.head
        for _ in range(num_to_display):
            elements_to_show.append(self.queue[current])
            current = (current + 1) % self.capacity
        print(elements_to_show)

    def show_iv(self):
        self.show_v(4)

    def show_last_three_logs(self):
        if self.size == 0:
            return
        
        start_index_relative = max(0, self.size - 3) 
        
        logs = []
        for i in range(start_index_relative, self.size):
            actual_index = (self.head + i) % self.capacity
            logs.append(self.queue[actual_index])
        
        print(logs)

    def convert_to_simple_queue(self):
        simple_queue_list = []
        if self.is_empty():
            return simple_queue_list
        
        current = self.head
        for _ in range(self.size):
            simple_queue_list.append(self.queue[current])
            current = (current + 1) % self.capacity
        
        return simple_queue_list
