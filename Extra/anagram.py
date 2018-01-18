def anagram(a,b):
    temp1 = list(a)
    temp2 = list(b)
    return temp1 == temp2
a = input("Enter first string = ")
b = input("Enter second string = ")
c = anagram(a,b)
print(c)