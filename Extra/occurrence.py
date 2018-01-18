def occurrence(s,a):
        count = 0
        data = s.split(a) #split string into a list
        for temp in data:
                if temp == a:
                        count = count + 1 
        print(count)

s = input("Enter string = ")
a = input("Enter occurrence string = ")
occurrence(s,a)

