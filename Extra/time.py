from time import clock

print("Enter your name: ", end="")
start_time = clock()
name = input()
total_time = clock() - start_time
print(name, "it took you", total_time, "seconds to respond")
print("currenttime = ",time.now())
