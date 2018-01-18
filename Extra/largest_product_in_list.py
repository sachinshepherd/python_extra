def adjacentElementsProduct(t):
    return max(list(t[i]*t[i+1] for i in range(len(t)-1)))
c =adjacentElementsProduct([5, 1, 2, 3, 1, 4])
print(c)
