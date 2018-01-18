try:
    data = open('file.txt','r')
    print(data.readline(), end='')
except IOError:
    print('File error')
finally:
    data.close()
