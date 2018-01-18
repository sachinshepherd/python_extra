import time

with open('file1.txt','a') as f:
    line1 = 1000
    f.write("Total amount =  {}".format(line1))
    time=time.asctime()
    f.write("({})\n".format(time))
    f.read()
f.close()


