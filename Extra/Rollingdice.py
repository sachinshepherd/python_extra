import random

def rolling(a):
    if a=='1':
        for x in range(1):
            i = random.randint(1,6)
            print("1st dice value = ",i)
        for x in range(1):
            j = random.randint(1,6)
            print("2nd dice value = ",j)
        print("total = ",i+j)
        play()
    else:
        print("Good bye!")

def play():
    a=input("Press 1 for Rolling the dice : ")
    rolling(a)
            
play()
