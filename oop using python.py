print("this is a simple code for the follwoing code for oops in python")


# lets code after i guess more than 1 year shall we?

# classes in python

# general syntax for making a class in python

class Computer:
    # types of variables in OOP
    # instance variable: they are the one which you can change whenever you want
    # i.e the example we are using in init funciton is an instance variable

    # static variable: they are same for all objects
    # i.e we make a class of computers of intel , the company name  = intel will be same for all objects
    # they are defined inside the class but outside the init funciton
    # however if we need to  change the class varaiable, it will be changed for all the objects made
    # we can do it using the class name

    # i.e  Computer.mf_year = 2021

    mf_year = 2020

    # init is basically used to initialize the object , or in other words we can all it a constructor
    # we populate out object using the constructor in cpp here we are doing the same with init method

    def __init__(self, model, ram, price):
        print("init called for object")
        self.model = model
        self.ram = ram
        self.price = price

    # the thing here to notice is that it is called automaticaly whenever we create an object just as
    # we used to do in cpp when we make a class and its constructor is automatically called

    # simple behaviour/ function/ methods we use in Classes
    def congif(self):
        print("the object made is :  ", self.model, self.ram, self.mf_year, self.price)

    # so here we got the reason of using self  , to use it and pass ist so that we dont need to write the name of
    # obejct again and again
    def compare(self, other):
        if self.ram > other.ram:
            print(self.ram, " is faster ")
        else:
            print(other.ram, " is faster ")

    def expense(self):
        if self.price >= 100000:
            print("this laptop is expensive")
        else:
            print("this laptop is not expensive")


a = 5
x = 8
# this computer is something like we call constructor in c++ and other languages
b = Computer('i5', '16gb', 130000)
c = Computer('ryzen 3', '24 gb', 123000)
d = Computer('i7', '8gb', 80000)
# now another thing to notice is that we are passing 3, not 2 parameters to init .. the first is the object
# itself and then comes the values


print(type(a))
print(type(b))

# lets call the config function
# we will call it the same way as we call np.array(and this the name)

Computer.congif(b)
# here we didn't call print because the method was already using the print function
c.congif()
# now u see we can also do it in this way as we used to do in c++ classes i.e x.print etc

# another thing to notice is that in PYTHON every thing is a project
# have a look at when i printed the type of a, it said <class int>
# it means that it will have its own behaviours

print(a.bit_length())
print(x.bit_length())
# bit length was a method made by the developer of int class which told us the bit lenght 5 = 101 in bit

b.compare(c)

b.expense()
d.expense()


# ACESSORS AND MUTATOR ARE ALSO USED IN OOP
# acessors which are also known as GETTERS are used to fetch a particular value of an instance
# mutators aka SETTERS are used to update a particular value  of an instance

####################################################################################################

class Student:
    school = "FAST NU"
    dept = "CS"

    def __init__(self, name, age, rollno, cgpa):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.cgpa = cgpa
        self.c = self.subject()

    def grader(self):
        if 3.5 < self.cgpa <= 4.00:
            print(self.name, " has an A grade")
        elif self.cgpa > 3.0 and self.cgpa <= 3.5:
            print(self.name, " has a B grade")
        elif 2.5 < self.cgpa <= 3.00:
            print(self.name, " needs to improve his grade")
        else:
            print(self.name, " doesnt has a good grade")

    # mutator(setter)
    def set_age(self, age):
        self.age = age

    def printstd(self):
        print("University Name: ", self.school)
        print("DEPT name: ", self.dept)
        print("Student name : ", self.name)
        print("Student Roll no : ", self.rollno)
        print("Student Age : ", self.age)
        print("Student CGPA : ", self.cgpa)
        print("Student list of courses : ")
        self.c.show()

    # inner class concept
    # we can use another class inside a class which has different syntax from others
    # its object is decalred outside the inner class but inside the outer class if we need it
    class subject:

        def __init__(self):
            self.courses1 = 'pf'
            self.courses2 = 'oop'
            self.courses3 = 'dsa'

        def show(self):
            print(self.courses1, self.courses2, self.courses3)


s1 = Student("Naveed", 20, "20L-1244", 2.45, )
s2 = Student("Taimour", 20, "20L-1309", 2.75)
s3 = Student("Mahd", 20, "20L-1299", 2.35)

s1.grader()
s1.printstd()
s1.set_age(21)
s1.printstd()


#############################################################################################33
# INHERITENCE IN OOP IN PYTHON LANGAUGE

#single level inheritence

class vehicle:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def show(self):
        print(self.model, self.year, self.price)

    def option1(self):
        print("this is option 1 just to show how child class inherits the parent")


class sedan(vehicle):
    # this is how the constructor is called of parent class in python when u r inheriting all the stuff in there
    def __init__(self, color, model, year, price):
        super().__init__(model, year, price)
        self.color = color

    def show(self):
        print(self.color, self.model, self.year, self.price)


car1 = vehicle('euro 2',2002,890000)
liana = sedan('white','fully optioned',2009,10000)
car1.show()
liana.show()
liana.option1()

#multi level inheritence
# it refers to the situation when your parent class is also child of another class, thus making u a grandchild class

class newsedan(sedan):

    def __init__(self,version, color, model, year, price):
        super().__init__(color, model, year, price)
        self.version = version

    def optionmax(self):
        print("i am the grandchild class inherting stuff fromm my grand parents and my parent")

    def prnt(self):
        super().show()
        print(self.version)

alto= newsedan('VXl','black','euro2',2020,1900000)
# the option 1 he took it from grandparent class
alto.option1()
alto.prnt()

######################################################################################################