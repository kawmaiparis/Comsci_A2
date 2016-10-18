class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, pointer):
        self.__next = pointer

class LinkedList:
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head == None

    def add(self, data):
        tempNode = Node(data)
        tempNode.setNext(self.__head)
        self.__head = tempNode

    def size(self):
        current = self.__head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count           

    def search(self, checkdata):
        current = self.__head
        while current != None:
            if current.getData() == checkdata:
                return True
            current = current.getNext()
        return False
        
    def removeFront(self):
        current = self.__head
        current = current.getNext()
        current = self.__head

    def removeLast(self):
        current = self.__head
        size = self.size()
        for x in range(size-1):
            current = current.getNext()
        current.setNext(None)

    def __str__(self):
        return str(self.__items)
    
mylist = LinkedList()
mylist.add(1)
mylist.add(2)
#print(mylist.size())
mylist.removeFront()
print(mylist.search(2))
#mylist.removeLast()
#print(mylist.size())
#print(mylist.search(2))
    
