"""class Student:
    student="Groot"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self)

s1=Student("groot",22)
print(s1)
print(s1.name)
print(s1.age)"""
"""class Student:
    def __init__(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def Avg_marks(self):
        average=self.marks1+self.marks2+self.marks3/3
        return f'average marks for student:{average:.3f}'

s1=Student(20,33,32)
print(s1.Avg_marks())"""

"""class Student:
    def __init__(self,accNo,accPass,accName):
        self.accNo=accNo
        self.accPass=accPass
        self.accName=accName

    def __hello(self):
        print(self.accName)

    def safe(self):
        return self.__hello()


s1=Student("12345","groot","hulk")
s1.safe()"""

"""class Car:
    def start(self):
        print("car start")

    def color(self):
        print("red")
    def stop(self):
        print("car stop")

class Toyata(Car):
    def __init__(self,name):
        self.name=name
car1=Toyata("thor")

print(car1.name)
car1.start()
car1.color()
car1.stop()"""


"""class Person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def data(self):
        print(f'i am {self.name} and i am {self.age} old')

class Person2(Person1):
    def __init__(self,name,age):
        super().__init__(name,age)

    def data2(self):
        print(f'{self.name}{self.age}')


p1=Person1("groot",20)
p1.data()
p2=Person2("hulk",22)
p2.data()
p2.data2()"""

"""class Car:
    def start(self):
        print("car start")

    def color(self):
        print("red")
    def stop(self):
        print("car stop")

class Toyata(Car):
    def __init__(self,Brand):
        self.Brand=Brand

class swift(Toyata):
    def __init__(self,Brand,Type):
        super().__init__(Brand)
        self.Type=Type




c1=swift("BMW","petrol")
print(c1.Type)
print(c1.Brand)
c1.start()
c1.color()
c1.stop()"""

"""class complex:
    def __init__(self,img,real):
        self.img=img
        self.real=real

    def show(self):
        print(self.real,"i","+",self.img,"j")

    def sum(self,num2):
        max_real=self.real+num2.real
        max_img=self.img+num2.img
        return complex(max_img,max_real)

    def __add__(self, num2):
        max_real = self.real + num2.real
        max_img = self.img + num2.img
        return complex(max_img, max_real)

num1=complex(2,3)
num1.show()
num2=complex(4,5)
num2.show()
num3=num1+num2
num3.show()"""

"""class Circle:
    def __init__(self,raidus):
        self.raidus=raidus

    def area(self):
        area_of_circle=3.14*self.raidus**2
        return area_of_circle
    def perimeter(self):
        perimenter_of_circlr=2*(3.14)*self.raidus
        return perimenter_of_circlr

c1=Circle(10)
print(c1.area())
print(c1.perimeter())"""

"""class Employee:
    def __init__(self,role,depart,salary):
        self.role=role
        self.depart=depart
        self.salary=salary

    def show_emp(self):
        print("role: ",self.role)
        print("depart: ",self.depart)
        print("salary: ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age,role,depart,salary):
        super().__init__(role,depart,salary)
        self.name=name
        self.age=age

    def Employee_details(self):
        return f'I am {self.name} and I am {self.age} old.I am working as {self.role} in {self.depart} department and my pay is {self.salary}'


emp2=Engineer("groot",22,"tester","IT",25000)
print(emp2.show_emp())
print(emp2.Employee_details())"""

"""class Order:
    def __init__(self,items,item_price):
        self.items=items
        self.item_price=item_price

    def __gt__(self, order2):
        return self.item_price>order2.item_price
    
o1=Order("pepsi",20)
o2=Order("badam milk",25)
print(o1>o2)"""


"""for i in range(1,5+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print("")"""

"""str="A"
print(ord(str))"""

"""def check_amstr(num):
    amstr=str(num)
    num_len=len(amstr)
    total=sum(int(i)**num_len for i in amstr)
    print(total)
    return num==total

if check_amstr(153):
    print("it is amstrong")
else:
    print("It is not amstrong")"""

"""def check(num):
    amst_lst=[]
    non_amst_lst=[]
    num_str=str(num)
    num_len=len(num_str)
    num_sum=sum(int(i)**num_len for i in num_str)
    return num_sum==num

for i in range(1,100):
    if check(i):
        print(i)
"""

"""from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def computer(self):
        print("groot")

c1=Computer()
c1.computer()"""

"""try:
    x=1/0
    print(x)
except ZeroDivisionError:
    print("zero can't be divided by any number")
finally:
    print("executed successfully")"""

"""class Complex:
    def __init__(self,img,real):
        self.img=img
        self.real=real

    def show(self):
        print(self.real,"i","+",self.img,"j")

    def sum(self,num2):
        max_real=self.real+num2.real
        max_img=self.img+num2.img
        return Complex(max_img,max_real)

    def __add__(self, num2):
        max_real = self.real + num2.real
        max_img = self.img + num2.img
        return Complex(max_img, max_real)

    def __mul__(self, mun2):
        max_real = self.real * num2.real
        max_img = self.img * num2.img
        return Complex(max_img, max_real)

num1=Complex(2,3)
num1.show()
num2=Complex(4,5)
num2.show()"""
"""num3=num1.sum(num2)
num3.show()"""



"""from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def computer(self):
        print("groot")


class Emp(Computer):
    pass
c2=Emp()
c2.computer()"""

"""class Student:
    def __init(self,name,age):
        self.name=name
        self.age=age

    def sum_all(self,a=None,b=None,c=None):
        sum=0
        if (a!=None and b!=None and c!=None):
            sum=a+b+c                                                               #Method Overloading
        elif a!=None and b!=None:
            sum=a+b
        else:
            sum=a

        return sum
c1=Student()
print(c1.sum_all(1,2))"""

"""class A:

    def show(self):
        print("In A show")                  #Method Overriding

class B(A):
    def show(self):
        print("In B show")

a1=B()
a1.show()"""

"""def func(a,*b):
    sum=a
    for i in b:                                             #variable length argument
        sum=sum+i
    print(sum)
func(1,2,3,4,5)"""

"""class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,s2):
        x1=self.m1+s2.m1
        x2=self.m2+s2.m2
        return Student(x1,x2)


    def __add__(self, s2):
        x1=self.m1+s2.m1
        x2=self.m2+s2.m2
        return Student(x1,x2)

    def __gt__(self, s2):
        x1=self.m1+self.m2
        x2=s2.m1+s2.m2
        if x1>x2:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.m1} {self.m2}'


s1=Student(10,20)
s2=Student(20,30)
s3=s1.sum(s2)
print(s3)

s4=s1+s2
print(s4)
"""

"""str1="race"
str2="care"

sort_str1=sorted(str1)
sort_str2=sorted(str2)
print(sort_str1)
print(sort_str2)
if sort_str1==sort_str2:
    print("it is anagram")
else:
    print("it is not anagram")"""

"""count=1
for i in range(1,5+1):
    for j in range(1,i):
        print(count,end=" ")
        count+=1
    print("")
"""
"""for i in range(5,0,-1):
    b=i
    for j in range(0,i):
        print(b,end=" ")
    print()
"""
"""rows=5
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print(" ")"""

"""rows=5
k=2*rows-2
for i in range(6,-1,-1):
    for j in range(0,k):
        print(end=" ")
    k+=1
    for j in range(0,i+1):
        print("*",end=" ")
    print()"""

"""rows=5
for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars="*"*(i*2-1)rows=5
for i in range(0,rows):
    if i==0:
        spaces=" "*(rows-i)
        stars="*"
        print(spaces+stars)

    else:
        underscore="_"*(i*2-1)
        spaces=" "*(rows-i)
        print(spaces+"*"+underscore+"*")


for i in range(rows,0,-1):
    spaces=" "*(rows-i)
    undersocre="_"*(i*2-1)
    print(spaces+"*"+undersocre+"*")
    if i==1:
        spaces=" "*rows
        star="*"
        print(spaces+star)
    print(spaces+stars)"""
""""""

"""x=10
def func():
    global x
    x=20
    print(x)

func()
print(x)"""

"""x=10
def func():
    globals()['x']=20
    x=1
    print(x)

func()
print(x)"""
"""def func():
    global x
    x=20
    print(x)

func()
print(x)"""

"""string="Groot"
def func(string):
    string="Hulk"
    print("inside function: ",string)

func(string)
print("outside function:",string)"""

"""def func(list):
    list.append('E')
    print("inside:",list)

list=['a']
func(list)
print("outside fun: ",list)"""


"""def func(string):
    string="Groot"
    print("inside function:",string)

string="Hulk"
func(string)
print(string)"""

"""year=2024

if(year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else:
    print("non leapyear")"""

#num=153

"""str_num=str(num)
str_len=len(str_num)
value=[int(i)**str_len for i in str_num]
print(value)
sum_value=sum(value)
print(sum_value)
if sum_value==num:
    print("amstrong number")
else:
    print("not amstrong number")"""

"""def amstr_numbers():
    for i in range(1,100):
        str_i=str(i)
        str_len=len(str_i)
        value=[int(i)**str_len for i in str_i]
        sum_value=sum(value)
        if sum_value==i:
            print(i)
        else:
            pass

amstr_numbers()"""

"""def check_amstr(num):
    str_num = str(num)
    str_len = len(str_num)
    value = [int(i) ** str_len for i in str_num]
    sum_value = sum(value)
    print(sum_value)
    if sum_value == num:
        print("amstrong number")
    else:
        print("not amstrong number")

check_amstr(9)"""

"""def anagram_check(str1,str2):
    sort_str1=sorted(str1)
    sort_str2=sorted(str2)
    if sort_str1==sort_str2:
        print("anagram str")
    else:
        print("not anagram")

anagram_check("rat","art")"""
"""list1=[1,2,3]
list2=[4,2,1]
if list1==list2:
    print(True)
else:
    print(False)"""


"""class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.lap=self.Laptop()

    def show(self):                                                                         # inner class
        print(self.name,self.marks)                             #if we want we can declared the inner class outside the outer class we need to give self.lap=Laptop()
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.processor = "i5"
            self.ram = "8Gb"

        def show(self):
            print(self.brand,self.processor, self.ram)

s1=Student("groot",22)
s1.show()"""


"""class Parent:
    def parent(self):
        print("parent class")

class Child1(Parent):
    def child1(self):
        print("child1 class")                                                   #hirecial inheritance
                                                                                #two child classes having one parent class

class Child2(Parent):
    def child2(self):
        print("child2 class")

c1=Child1()
c1.child1()
c1.parent()
c2=Child2()
c2.child2()
c2.parent()"""

"""class Parent:
    def parent(self):
        print("parent class")

class Child1(Parent):
    def child1(self):
        print("child1 class")                                                   #combination of hirecial inheritance and multi level inheritance
                                                                                #two child classes having one parent class

class Child2(Parent):
    def child2(self):
        print("child2 class")

class Headclass(Child1,Child2):
    def head(self):
        print("head class")

c1=Headclass()
c1.head()
c1.child2()
c1.child1()
c1.parent()"""

"""class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def show(self):
        print(self.m1,"i","+",self.m2,"j")

    def sum(self,s2):
        x1=self.m1+s2.m1
        x2=self.m2+s2.m2
        return student(x1,x2)

    def __add__(self, s2):
        x1=self.m1+s2.m1
        x2=self.m2+s2.m2
        return student(x1,x2)

    def __gt__(self, s2):
        x1=self.m1+self.m2
        x2=s2.m1+s2.m2
        return x1>x2

s1=student(2,3)
s2=student(4,5)
s1.show()
s2.show()
#s3=s1.sum(s2)
#s3.show()

s3=s1+s2
s3.show()

print(s1>s2)"""

"""n1=int(input("enter n1:"))
n2=int(input("enter n2:"))

if n1>n2:
    greater=n1
else:
    greater=n2

while (True):
    if (greater%n1==0) and (greater%n2==0):
        lcm=greater
        break
    greater+=1

print(lcm)"""

"""
n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
if n1<n2:
    smaller=n1
else:
    smaller=n2

for i in range(1,smaller+1):
    if (smaller%i==0) and (smaller%i==0):
        gcd=i

print(gcd)"""
"""x=10
def func():
    global x
    x=20
    print(x)

func()
print(x)"""

"""x=20
def func():
    globals()['x']=10
    print(x)

func()
print(x)"""

"""
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()"""

for  i in range(1,5):
    if i==3:
        print(i)
        break
