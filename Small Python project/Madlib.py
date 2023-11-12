# The first small project is MadLIB
# we will do this using string concatenation

yt = "Naveed Ali"
print("subsribe to " + yt)
print("Subsribe to {}".format(yt))
print(f"Subsribe to {yt}")

def Madlib():
        name = input("please enter your name: ")
        hobby = input("enter your fav part of programming: ")
        sourse = input("enter where you see most of your hobbies:")
        fam_person = input("Tell your idol: ")
        
        #clear screen
        print("\n"*10)
        
# these above are the three methods for string concatenation
# now in madlib, we will be using the 3rd type of string concatenation
        promt = f"Hey there {name}. Welcome to this small project of madlib where we will be filing in the blanks.\
                \nPlease be there till the end  {name}.\
                \nLets start with the madlib. So the purpose of this madlib is to let you know that there are many people who\
                dont know the use of string concatenation. for example if you like {hobby} then you should be doing that most of the time\
                when you are free. You might also like to watch {hobby} videos on youtube.\
                perhaps you might also like to visit {sourse} to learn more about {hobby}.\
                Python is a very good language to learn {hobby}.\
                \nHope you like this madlib {name}\
                Live like you are {fam_person}"
    
        print(promt)
        
Madlib()

# # now import the script Madlib.py in this script and run it
# from Madlib import Madlib
# Madlib()
