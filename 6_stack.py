class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    def pop(self):
        print "The last element is " + str(self.items[-1])
        print "I am going to delete that element"
        del self.items[-1]
    def peek(self):
        print "The last element is " + str(self.items[-1])
    def show(self):
            for counter in range(len(self.items)-1, -1, -1):
                print self.items[counter]
    
choice =int(input("\n 1.push an item into stack \n 2.pop an item from stack \n 3.show all items in stack \n 4.check whether the stack is empty or not \n 5.top element of stack\n"))
new=stack()
if choice == 1:
    new.push(10)
    new.push(20)
    lim=input("enter no.of items")
    elem=[raw_input("enter the item") for elem in range(lim)]
    new.push(elem)
    print "stack elements are",new.show()

elif choice == 2:
    print new.pop()

elif choice == 3:
    print new.show()

elif choice == 4:
    print new.isEmpty()

elif choice == 5:
    print new.peek()

else:
    print "invalid choice"

