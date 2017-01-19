def factorial(n):
    product = 1
    for x in range(n):
        product = product * (x+1)
    return product

print(factorial(6))
