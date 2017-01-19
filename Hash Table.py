hashTable = []

for i in range(10):
    hashTable.append(None)

def menu():
    print("1. Add item")
    print("2. Search item")

    option = int(input(""))
    if option == 1:
        data = input("Data: ")
        hashNo = hashItem(data)
        
        loop = True
        while loop:
            if hashTable[hashNo] == None:
                hashTable[hashNo] = data
                loop = False
            else:
                hashNo += 1
                if hashNo > len(hashTable)-1:
                    hashNo = 0

    elif option == 2:
        found = search()
        if found == True:
            print("Item found!")
        else:
            print("Item not found!")

def hashItem(data):
    sum = 0
    for letter in data:
        sum += ord(letter)
    hashNo = sum % len(hashTable)
    return hashNo

def search():
    data = input("Data: ")
    hashNo = hashItem(data)
    
    loop = True
    while loop:
        if hashTable[hashNo] == None:
            return False
        elif hashTable[hashNo] != data:
            hashNo += 1
        else:
            return True

while True:
    print(hashTable)
    menu()
    
