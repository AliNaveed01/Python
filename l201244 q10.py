def gensquares(num):
    for i in range(num): 
        yield i**2
for x in gensquares(10):
    print (x)