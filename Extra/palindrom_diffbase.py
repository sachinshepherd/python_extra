def diff_base_palindrom():
    base = [2,3,5,6,8]
    for n in range(1,1000,1):
        for i in base:
            rem = 0
            divd = n
            while divd > 0:
                rem = (rem*10) + (divd%i)
                divd = int(divd/i)
            if rem == n:
                print "{} : {} ".format(n,i)
                break
diff_base_palindrom()
