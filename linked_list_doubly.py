class Node(object):

    def __init__(self, data = None, next_node = None, last_node = None):
        self.data = data
        self.next_node = next_node
        self.last_node = last_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_last(self):
        return self.last_node

    def set_next(self, new_node):
        self.next_node = new_node

    def set_last(self, new_node):
        self.last_node = new_node

class LinkedList(object):

    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head.set_last(new_node)
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
                    self.head.set_last(None)
                else:
                    pointer.get_last().set_next(pointer.get_next())
                    return None
            pointer = pointer.get_next()
        raise ValueError("Data not in list")


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
# print linked.head.get_next().get_data()
# print linked.head.get_next().get_next().get_data()
#
# print linked.size()
# print linked.search('e')
# linked.delete('e')
# print linked.size()
# print linked.search('a')
# print linked.search('e')
