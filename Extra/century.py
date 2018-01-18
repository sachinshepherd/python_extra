def centuryFromYear(year):
    if year % 100 == 0:
        ans = int(year / 100)
    else:
        ans = int(year / 100) + 1 
    print("centuryFromYear({}) = {}".format(year,ans))
centuryFromYear(1905)
