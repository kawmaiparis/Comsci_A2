def reverse(string):
    if len(string) == 1:
        return string[0]
    else:
        return string[len(string)-1] + reverse(string[0:len(string)-1])


print(reverse("glom"))
