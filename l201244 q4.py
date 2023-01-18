#l201244 q4

def string_test(sample):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in sample:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
	   pass
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('Hello Mr. Rogers, how are you this fine Tuesday?')