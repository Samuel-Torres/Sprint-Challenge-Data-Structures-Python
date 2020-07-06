class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class CircularDoublyLinkedList:
    def __init__(self, node=None, capacity=None):
        self.head = node
        self.tail = node
        self.oldest_node = node
        self.length = 0

    def append(self, value, capacity):
        new_node = Node(value)

        if self.length == 0:
            # print('Initial Insert')
            new_node.next_node = self.tail
            new_node.prev_node = self.head
            self.head = new_node
            self.tail = new_node
            self.oldest_node = new_node
            self.length += 1

        elif self.length != capacity and self.length >= 1:
            new_node.prev_node = self.tail
            new_node.next_node = self.head
            self.tail.next_node = new_node
            self.head.prev_node = new_node
            self.tail = new_node
            self.length += 1

        elif self.length == capacity and self.length >= capacity:
            prev_oldest_node = self.oldest_node
            self.oldest_node.value = value
            self.oldest_node = prev_oldest_node.next_node

    def get(self):
        get_list = []
        current_node = self.head
        while current_node:
            if current_node != self.tail:
                get_list.append(current_node.value)
                current_node = current_node.next_node
            elif current_node == self.tail:
                get_list.append(current_node.value)
                break
        return get_list


class RingBuffer:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.size = 0
        self.storage = CircularDoublyLinkedList()

    def append(self, item):
        self.storage.append(item, self.capacity)

    def get(self):
        return self.storage.get()
