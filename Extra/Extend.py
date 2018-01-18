f1 = open('movie.txt', 'r')
l,i = [],0
for a in f1:
    l.append(a)
    if l[i][2] == 1 :
        l.extend('\tAvailable\n')
    else:
        l.extend('\tNot Available\n')
    i += 1
print(l)

