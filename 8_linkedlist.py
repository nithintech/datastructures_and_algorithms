class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_node

    def setNext(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
new1=LinkedList()
new1.insert(5)
new1.insert(10)
new1.insert(15)
