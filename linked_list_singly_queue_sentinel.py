class Node(object):

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node

class LinkedList(object):

    def __init__(self, head = None):
        self.head = head
        self.sentinel = Node()
        self.head.set_next(self.sentinel)
        self.sentinel.set_next(self.head)

    def size(self):
        pointer = self.head
        count = 0
        while pointer:
            count += 1
            pointer = pointer.get_next()
        return count

    def search(self, data):
        pointer = self.head
        while pointer:
            if pointer.get_data() == data:
                return pointer
            pointer = pointer.get_next()
        raise ValueError("Data not in list")

    def search_alt(self, data):
        pointer = self.head
        while pointer:
            if pointer.get_data() == data:
                return pointer
            pointer = pointer.get_next()
        raise ValueError("Data not in list")

    def dequeue(self):
        if self.head:
            x = self.head
            self.head = self.head.get_next()
        return x

    def enqueue(self, data):
        self.sentinel.data = data
        new_node = Node()
        self.sentinel.set_next(new_node)
        self.sentinel = new_node
        self.sentinel.set_next(self.head)

    def output(self):
        pointer = self.head
        while(pointer):
            print pointer.get_data(),
            pointer = pointer.get_next()
        print



a = Node('a')
linked = LinkedList(a)
linked.enqueue('b')
linked.enqueue('c')
linked.enqueue('d')
linked.enqueue('e')
linked.enqueue('f')
linked.output()

linked.dequeue()
linked.output()

linked.dequeue()
linked.output()

linked.enqueue('g')
linked.output()
