class tree_node:
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None
            
    def getData(self):
        return self.__value

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def setValue(self, newdata):
        self.__value = newdata

    def setLeft(self, newdata):
        self.__left = newdata

    def setRight(self, newdata):
        self.__right = newdata

class binary_tree:
    def __init__(self):
        self.__first = None

    def search(self, value):
        root = self.__first
        if value == root:
            print("True!")
        elif value > root:
            root = self.__right
            if value == root:
                print("TRUETRUE!")
        elif value < root:
            root = self.__left
            if value == root:
                print("TRUETRUE 2x")
        else:
            print("False !!")

    def add(self, value):
        root = self.__first
        if root == None:
            self.__first = value
        elif value < root:
            root.setLeft(value)
        elif value > root:
            root.setRight(value)



mytree = binary_tree()
mytree.add(3)
mytree.add(2)
print(mytree.search(3))
print(mytree.search(2))
