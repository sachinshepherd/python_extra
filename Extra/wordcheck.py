f1=open('balance.txt','r')
y=f1.readline()
x = y.split(" ")
amt=x[2]
print(amt)
f1.close()
