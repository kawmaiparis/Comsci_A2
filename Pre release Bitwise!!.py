x = "10101111"
print('x: ' + x)
mask = input("Mask: ")

ACC = []

def menu():
    while True:
        print('1. AND')
        print('2. OR')
        print('3. XOR')
        print('4. test for specific bit')
        choose = input("Logic Gate: ")
        if choose == '1':
            AND()
        elif choose == '2':
            OR()
        elif choose == '3':
            XOR()
        elif choose == '4':
            TEST()

        print(ACC)

def AND():
    count = 0
    for bit in x:
        if mask[count] == '1' and bit == '1':
            ACC.append(1)
        else:
            ACC.append(0)
    

def OR():
    count = 0
    for bit in x:
        if mask[count] == '1' or bit == '1':
            ACC.append(1)
        else:
            ACC.append(0)
        count += 1

def XOR():
    count = 0
    for bit in x:
        if mask[count] == '1' and bit == '1':
            ACC.append(0)
        elif mask[count] == '0' and bit == '0':
            ACC.append(0)
        else:
            ACC.append(1)

def TEST():
    bitposi = int(input('bit position (start at 0 from the left): '))
    if x[bitposi] == '1':
        print("1")
    else:
        print("0")
menu()
