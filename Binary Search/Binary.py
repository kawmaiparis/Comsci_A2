def binarysearch(needle, haystack):
    size = len(haystack)
    middle = int(round((size-1)/2, 0))
    print(middle)
    constant = haystack[middle]
    while True:
        start = 0
        end = size - 1
        pointer = haystack[middle]
        if pointer == needle:
            return "found"
            
        else:
            if pointer > needle:
                if pointer > constant:
                    return "not found"
                start = middle + 1
                middle = int(round((start + end)/2, 0))
            else:
                if pointer < constant:
                    return "not found"
                end = middle - 1
                middle = int(round((start + end)/2, 0))

print(binarysearch(4, [1,2,3,4,5]))
