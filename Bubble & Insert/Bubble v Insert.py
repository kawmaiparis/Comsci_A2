import time
import random

def main():
    unsorted = []
    while True:
        print("1. Random List")
        print("2. Make your own list")
        print("3. Pre-Set List")
        print("4. Run Bubble Sort")
        print("5. Run Insertion Sort")
        option = input("")
        unsorted2 = list(unsorted)
        if option == "1":
            num = input("how many numbers: ")
            for k in range(int(num)):
                r = random.randint(1,100)
                unsorted.append(r)
            print(unsorted)
        elif option == "2":
            add = input("input number [type x to end]: ")
            if add == "x":
                print(unsorted)
                break
            else:
                unsorted.append(add)
        if option == "3":
            print("1. Ordered List")
            print("2. Bigger List")
            print("3. Smaller List")
            print("4. Reverse List")
            option2 = input("")
            if option2 == "1":
                for i in range(0,500):
                    unsorted.append(i)
            elif option2 == "2":
                for i in range(0,1000):
                    unsorted.append(i)
            elif option2 == "3":
                for i in range(0,100):
                    unsorted.append(i)                   
            elif option2 == "4":
                for i in range(999,0,-1):
                    unsorted.append(i)
            print(unsorted)
                    
        elif option == "4":
            print(1,unsorted)
            bubble(unsorted)
        elif option == "5":
            insert(unsorted)

def bubble(unsorted):
    print(unsorted)
    hold = unsorted
    start = time.clock()
    for c in range(len(unsorted)):
        posi = 0
        for z in range(len(unsorted)-1):
                if unsorted[posi] > unsorted[posi+1]:
                        value = unsorted[posi]
                        unsorted.remove(value)
                        unsorted.insert(posi+1,value)
                posi = posi + 1
    end = time.clock()
    bubtime = end - start
    print(hold)
    print(unsorted)
    print("Total time: " + str(bubtime))
    file = open("test.txt","a")
    file.write("Bub, " + str(bubtime) + '\n')
    file.close()
    return(bubtime)

def insert(unsorted):
    print(unsorted)
    hold = unsorted
    start = time.clock()
    for pointer in range(1,len(unsorted)):
        insert = unsorted[pointer]
        CurrentItem = pointer - 1
        while unsorted[CurrentItem] > insert and CurrentItem >= 0:
            unsorted[CurrentItem + 1] = unsorted[CurrentItem]
            CurrentItem = CurrentItem - 1
        unsorted[CurrentItem + 1] = insert
    end = time.clock()
    instime = end - start
    print(hold)
    print(unsorted)
    print("Total time: " + str(instime))
    file = open("test.txt", "a")
    file.write("Ins," + str(instime) + "\n")
    file.close()
    return(instime)

main()
