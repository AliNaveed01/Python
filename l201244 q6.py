#l20244 q6

str = "Create a list of the first letters of every word in this string"
breakdown = str.split()
flist = []
for char in breakdown:
    flist.append(char[0])
print ("The first characters in the strings are ")
print(flist)