from Calc.add import addin
from Calc.sub import subin
from Calc.mul import mulin
from Calc.div import divin

a=float(input("Enter 1st Value : "))
b=float(input("Enter 2nd Value : "))
sign=input("Enter any(+,-,*,/) sign : ")
if sign=='+':
    addin(a,b)
elif sign=='-':
    subin(a,b)
elif sign=='*':
    mulin(a,b)    
elif sign=='/':
    divin(a,b)
else:
    print("Diffrent Sign")
