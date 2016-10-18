k = [3,2,6,1]
print(k)
for index in range(len(k)):
    value = k[index]
    i = index - 1
    while i > 0 and value < k[i]:
            k[i+1] = k[i]
            i = i -1
    k[i] = value
