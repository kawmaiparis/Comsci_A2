def binarysearch(needle, haystack):
    
    while True:
        print(haystack)
        size = len(haystack)
        middle = int(round((size-1)/2, 0))
        pointer = haystack[middle]
        print(pointer)
        print(middle)
        
        if pointer == needle:
            return "found"
        else:
            posi = haystack.index(pointer)
            if len(haystack) == 2:
                if needle == haystack[1]:
                    return "found"
                else:
                    return "not found"

            elif pointer < needle:
                for i in range(posi):
                    haystack.pop(0)
            elif pointer > needle:
                print(posi)
                for i in range(posi):
                    haystack.pop(posi)
            

print(binarysearch(5,[1,2,3,4,5,15,53,66,77,88,989,124214]))
