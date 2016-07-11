execfile('node.py')

class LinkedList:
    # create a linked list using Node and data passed as array to __init__
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head.get_data()

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size = size + 1
            current = current.get_next()
        return size

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def build(self, data_array):
        for data in data_array:
            self.add(data)
        return self

    def remove_dups(self):
        dups = {}
        prev = None
        current = self.head
        num_dups_removed = 0
        while current is not None:
            if current.get_data() in dups:
                # should only have key if we dup exists, but for clarity
                if dups[current.get_data()]:
                    prev.set_next(current.get_next())
                num_dups_removed += 1
            else:
                dups[current.get_data()] = True
            prev = current
            current = prev.get_next()
        return num_dups_removed
