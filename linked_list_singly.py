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

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

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

    def delete(self, data):
        pointer = self.head
        while pointer:
            if pointer.get_data() == data:
                if pointer == self.head:
                    self.head = self.head.get_next()
                else:
                    last_node.set_next(pointer.get_next())
                    return None
            last_node = pointer
            pointer = pointer.get_next()
        raise ValueError("Data not in list")

    def output(self):
        pointer = self.head
        while(pointer):
            print pointer.get_data(),
            pointer = pointer.get_next()
        print

# a = Node('a')
# linked = LinkedList(a)
# print linked.head.get_data()
#
# linked.insert('b')
# print linked.head.get_data()
# linked.insert('c')
# print linked.head.get_data()
# linked.insert('d')
# print linked.head.get_data()
# linked.insert('e')
# print linked.head.get_data()
# linked.insert('f')
# print linked.head.get_data()
#
# print linked.size()
# print linked.search('e')
# linked.delete('e')
# print linked.size()
# print linked.search('e')
