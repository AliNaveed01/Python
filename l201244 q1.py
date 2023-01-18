# l201244 q1
str = 'Print only the words that start with s in this sentence'
x = str.split()
for n in x:
    if(n[0] == 's' or n[0] == 'S'):
        print(n)