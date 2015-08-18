class queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    def dequeue(self):
        print "The last element is " + str(self.items[-1])
        print "I am going to delete that element"
        del self.items[1]
    def topelem(self):
        print "The last element is " + str(self.items[-1])
    def show(self):
            for counter in range(len(self.items)-1, -1, -1):
                print self.items[counter]
    
choice =int(input("\n 1.push an item into queue \n 2.pop an item from queue \n 3.show all items in queue \n 4.check whether the queue is empty or not \n"))
new=queue()
if choice == 1:
    lim=input("enter no.of items to be inserted")
    elem=[raw_input("enter the item") for elem in range(lim)]
    new.enqueue(elem)
    print "",new.show()

elif choice == 2:
    print new.dequeue()

elif choice == 3:
    print new.show()

elif choice == 4:
    print new.isEmpty()

elif choice == 5:
    print new.topelem()

else:
    print "invalid choice"


