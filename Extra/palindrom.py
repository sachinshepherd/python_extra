def checkPalindrome(a):
    return a == a[::-1]
c = checkPalindrome('abab')
print(c)