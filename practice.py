#Day 1
#name
"""str=str(input("enter your name: "))
print(str)"""
# add
"""a=2
b=4
print(a+b)"""
#subtraction
"""a=10
b=4
print(a-b)"""
#multiply
"""a=10
b=5
print(a*b)"""
#division
"""a=25
b=5
print(a%b)"""

# Day2
"""name="groot!"
print("Hello",name)"""
"""pi=3.14
print(pi)"""
"""is_raining=str(input("enter the boolen exp: "))
is_raining=bool(is_raining)
if is_raining:
    print(type(is_raining),"the data type is converted to boolen)"""

"""sentance=input("enter the number: ")
sentance=int(sentance)
print(type(sentance))
print("the sentance repated that number of times")"""

"""x=10
y=20
add=x+y
sub=y-x
mul=x*y
div=x/y
pow=x**y
rdm=x%y
flr=x//y
print(add,sub,mul,div,pow,rdm,flr)"""

"""value=20
value=int(input("enter the number: "))
print(value)"""

"""str="hello world"
print(len(str))
print(str[-1])"""

"""list=[23,45]
sum=sum(list)
total=len(list)*sum
print(total)"""

"""num=-5
if num>0:
    print("positive")
else:
    print("negative")
if num%2==0:
    print("even")
else:
    print("odd")"""
"""for i in range(1,10):
    if i==6:
        break
    print(i)"""
"""for i in range(1,10):
    if i%5==0:
        break
    print(i)"""
"""for i in range(1,10):
    if i%2==0:
        continue
    print(i)"""
"""for i in range(1,10):
   if i==5:
        continue
    print(i)"""

"""i=0
while i<=10:
    if i==5:
        break
    print(i)
    i+=1"""

"""i=0
while i<10:
    i += 1
    if i==7:
        continue
    print(i)"""

"""baby, child, teenager, or adult"""

"""age=int(input("enter age: "))
if age<2:
    print("baby")
elif age<8:
    print("child")
elif age<17:
    print("teenager")
else:
    print("adult")"""

"""A (90-100), B (80-89), C (70-79), D (60-69), and F (below 60)."""

"""marks=int(input("enter marks: "))
if marks<=100 and marks>=90:
    print("Grade A")
elif marks<90 and marks>=80:
    print("Grade B")
elif marks<80 and marks>=70:
    print("Grade C")
elif marks<70 and marks>=60:
    print("Grade D")
else:
    print("Grade F")"""


#Check if a given year is a leap year, and if it is, find the number of days in February for that year.

"""year=int(input("enter year :"))
if (year%400==0) or (year%100!=0) and (year%4==0):
    print("year is leapyear , it has 29 days in february month")
else:
    print("year is not leap year, it has 28 days in february month")"""
"""i=1
while i<=10:
    print(i)
    i+=1
"""
"""sum=0
i=1
n=int(input("enter the value of n:"))
while i<=n:
    sum+=i
    i+=1
print(sum)"""

"""i=1
while i<=10:
    if i%2==0:
        print(i)
    i=i+1"""

"""while True:
    number=int(input("enter the number: "))
    if number<0:
        print("negative")"""

"""n=int(input("enter number: "))
i=1
while i<=n:
    print(i**2)
    i+=1"""
"""    for i in range(1,6):
        print(i)
    sum=0
    for i in range(1,11):
        sum+=i
    print(sum)"""

"""str=input("enter str: ")
for i in str:
    print(i)"""

"""for i in range(1,6):
    print(i+i)"""
"""str="Hello,World!"
print(str.lower())
print(len(str))
print(str.upper())
str1=" python programming "
print(str1.strip())
str2="I love python programming"
list=str2.split(" ")
for i in list:
    print(i)
str="I love Python programming, Python is great."
print(str.replace("Python","Java"))
str="Hello,World!"
print(str.startswith("Hello"))
print(str.endswith("World!"))
str="banana"
print(str.count("a"))
str="Hello,World!"
print(str.find("l"))
str="12345"
print(str.isnumeric())
print(str.isalnum())
print(str.isalnum())"""

"""for i in range(5):
    for j in range(5):
        print("*",end="")
    print()"""
"""for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=" ")
    print()"""
"""for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")                                   
    print()"""

"""
5  4  3  2  1
10 8  6  4  2
15 12 9  6  3
20 16 12 8  4
25 20 15 10 5"""

"""i=1
while i<=5:
    print("*"*i)
    i=i+1"""

"""for i in range(2,20):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")"""
"""fact=1
for i in range(1,6):
    fact=fact*i
    print(fact,end=" ")"""

"""for i in range(1,10):
    if i==5:
        break
    print(i)"""

"""list=[1,2,3,4,5]
for i in list:
    if i==3:
        continue
    print(i)"""
"""str="Hello,World!"
for i in str:
    if i=="o":
        print("found 'o'")
        break"""

"""list=[1,2,3,4,5]
for i in list:
    if i==4:
        continue
    print(i*2)"""
"""i=1
while i<=20:
    if i==15:
        break
    print(i)
    i=i+1"""

"""print(str1==str2)
str1=""
str2=""
print(str1==str2)"""

"""for i in range(1,10):
    if i==5:
        break
    print(i)"""

"""list=[1,2,3,4,5]
for i in list:
    if i==3:
        continue
    print(i)"""

"""list=[1,2,3,4,5]
for i in list:
    if i==4:
        continue
    print(i*2)"""

"""i=1
while i<=20:
    if i==15:
        break
    print(i)
    i+=1"""
"""str1="Python"
str2="python"
print(str1==str2)

str=input("enter the input: ")
if str=="":
    print(True)
else:
    print(False)"""

"""list=[]
for i in range(5):
    x=int(input("enter the number: "))
    list.append(x)
for i in list:
    print(i)"""
"""
list=["apple","banana","orange"]
for i in list:
    print(i,end=" ")"""

"""list=[1,2,3,4,5]
sum=0
for i in list:
    sum+=i
print(sum)"""
"""list=[10,20,30,40,50]
print(max(list))"""

"""list=["Alice","Bob","Charlie"]
str=input("enter the string: ")
if str in list:
    print("name found")
else:
    print("name not found")"""

"""print(('apple',5,True))"""

"""tup=('cat','dog','bird','fish')
print(tup[1])"""
"""tup=(1,2,3)
tup1=('a','b','c')
print(tup+tup1)"""

"""tup=(10,20,30,40,50)
print(len(tup))"""

"""tup=(10,20,30,40,50)
no=int(input("enter the number "))
if no in tup:
    print("found")
else:
    print("not found")"""
"""tup=(3,6,9)
print(tup*3)"""

"""dict={}
print(dict)"""
"""dict={"jhon":25,"Alice":30}
print(dict.keys())
print(dict.values())
dict["Groot"]=5
print(dict)"""

"""Dictionary= {"name": "Alice", "city": "New York", "age": 30}
print(Dictionary.get("city"))"""

"""dict={}
dict["name"]="Bob"
dict["email"]="groot8@mail.com"
print(dict)"""

"""employee= {"name":"Alice","age":30}
print(employee)
fruits={"apple":5,"banana":7}
fruits["orange"]=3
print(fruits)
inventory={"apple":5,"banana":15,"sugar":2}
inventory.pop("sugar")
print(inventory)"""

"""def add_stock(stock,item_name):
    if item_name in stock:
        stock[item_name]+=1
    print(stock)
stock={"apple":10,"banana":15}
item_name="banana"
add_stock(stock,item_name)

scores={"bob":85,"charlie":90,"alice":78}
key=input("enter the str: ")
if key in scores:
    print(scores.get(key))"""

"""vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
str=input("enter the string : ")
for i in str:
    if i in vowels:
        vowels[i]+=1
print(vowels)"""

"""student_grade={"alice":85,"bob":90,"charlie":78}
x=student_grade.values()
y=max(x)
for i in student_grade.items():
    if y in i:
        print(i)"""

"""set1={}
print(set1)
set={1,2,3}
set.add(4)
print(set)
set.remove(3)
print(set)"""
"""list=[5,10,15,20]
x=set(list)
print(x)"""
"""set={10,20,30,40}
set.discard(20)
set.discard(50)
print(set)"""

"""a={1,2,3}
b={3,4,5}
symetric=a.symmetric_difference(b)
print(symetric)
set={1,2,3}
print(2 in set)
a={1,2,3}
b={3,4,5}
union_set=a.union(b)
print(union_set)

intersection_sets=a.intersection(b)
print(intersection_sets)

a={1,2,3,4}
b={3,4,5}

diff_sets=a.difference(b)
print(diff_sets)"""


"""list4=[1,2,2,3,4,4,5]
x=set(list4)
print(list(x))"""
"""set={1,2,3,4,5}
print(len(set))"""

"""a={1,2,3}
b={4,5,6}
print(a.isdisjoint(b))"""

"""a={1,2,3,4,5}
a.clear()
print(a)"""

"""def fun():
    print("hello python")

fun()"""

"""def fun(Name):
    print("Hello welcome {Name2}".format(Name2=Name))
fun("Groot")"""


"""def fun(Name):
    return "hello"+ Name

print(fun("Groot"))"""

"""def fun(a,b):
    return a+b
print(fun(5,10))"""

"""def fun(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
num=int(input("enter number : "))
print(fun(num))"""

"""def fun():
    name="guest"
    return "Hello"+ name
print(fun())"""

"""def fun(list):
    sum=0
    for i in list:
        sum+=i
    return sum
list=[2,4,6,8,10]
print(fun(list))"""

"""def fun(num):
    return num**2
num=int(input("enter num :"))
print(fun(num))"""
"""
x=10
def func():
    x=20
    print(x)
func()
print(x)"""

"""x=10
def fun():
    global x
    x=20
    print(x)
fun()
print(x)"""

"""x=10
def fun():
    h=globals()["x"]
    print(h)
fun()
print(x)"""

"""def func(name="Guest"):
    print("hello",name)
func("hulk")"""

"""def func(a,b,c):
    sum=a+b+c
    return sum
print(func(5,10,15))"""

"""def sqr_fun(num):
    return num**2
def dbl_fun(num):
    sqr=sqr_fun(num)
    return sqr*2
print(dbl_fun(2))"""

"""def outer_function():
    outer_variable="I'm outer"
    def inner_function():
        inner_varriable="I'm inner"
        print(outer_variable)
        print(inner_varriable)
    inner_function()
    print(outer_variable)

outer_function()"""

"""def divide_and_remainder(a,b):
    div=a//b
    rem=a%b
    return div,rem
print(divide_and_remainder(4,2))"""

"""def fun(n):
    if n==0:
        return 1
    else:
        return n*fun(n-1)
n=5
print(fun(n))"""

"""def fun(a,b):
    return a+b
print(fun(5,10))"""

"""def func(name,age):
    print("hello,{Name}! You are {Age} years old".format(Name=name,Age=age))
func(name="groot",age=20)"""

"""def func(a,b=2):
    return a*b
print(func(5))"""

"""def fun(name,age,country):
    return "Name :{Name},Age:{Age},Country={Country}".format(Name=name,Age=age,Country=country)
print(fun("Alice",25,"USA"))"""

"""str='a1b2c3'
no_lst=[]
for i in str:
    if i.isnumeric():
        no_lst.append(int(i))
print(no_lst)
alp_list=[]
for i in str:
    if i.isalpha():
        alp_list.append(i)
print(alp_list)"""

"""def decode_string(input_str):
    output_str = ""
    i = 0

    while i < len(input_str):
        letter = input_str[i]
        count = 0
        i += 1

        while i < len(input_str) and input_str[i].isdigit():
            count = count * 10 + int(input_str[i])
            i += 1

        output_str += letter * count

    return output_str

input_str = input("Enter the input string: ")
result = decode_string(input_str)
print("Output:", result)"""


"""def func(input_str):

    out_str=""
    i=0

    while i<len(input_str):
        letter=input_str[i]
        count=0
        i+=1

        while i<len(input_str) and input_str[i].isdigit():
            count=count*1+int(input_str[i])
            i+=1

            out_str+=letter*count
    return out_str

str=input("enter str:")
output=func(str)
print(output)"""

"""def custom_sort(arr):
    even_pos = []
    odd_pos = []

    for i, num in enumerate(arr):
        if i % 2 == 0:
            even_pos.append(num)
        else:
            odd_pos.append(num)

    even_pos.sort()
    odd_pos.sort(reverse=True)

    result = []
    for i in range(len(even_pos)):
        result.append(even_pos[i])
        if i < len(odd_pos):
            result.append(odd_pos[i])

    return result

input_str = input("Enter the input string (comma-separated numbers): ")
input_list = [int(num) for num in input_str.split(",")]
result = custom_sort(input_list)
output_str = ",".join(map(str, result))
print("Output:", output_str)"""

"""num=[10,5,8,5,3]
print(max(num))
print(min(num))

num=[1,2,3,4,5]
print(sum(num))

print(list(range(2,10,2)))
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))

txt="hello world!"
print(len(txt))

num=-10
print(abs(num))

bool_list = [True, True, False, True]
print(all(bool_list))
print(any(bool_list))"""

"""i=1
while i<=5:
    print("*"*i)
    i+=1
"""
"""def pyramid(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

pyramid(5)"""

"""l=4
b=6
for i in range(l):
    if i==0 or i==3:
        print("* "*6)
    else:
        print("*"+" "*(b*2-3)+"*")"""

# * * * * * *
# *         *
# *         *
# * * * * * *


# *****
# *   *
# *   *
# *   *
# *****

"""l=int(input("enter the length: "))
b=int(input("enter the breadth: "))
for i in range(l):
    if i==0 or i==l-1:
        print("*"*b)
    else:
        print("*"+" "*(b-2)+"*")"""

"""i=5
while i>=1:
    print("*"*i)
    i-=1"""
"""rows=int(input("enter the no of rows: "))
for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars="*"*(i)
    print(spaces+stars)"""

"""rows=int(input("enter no rows: "))
for i in range(1,rows+1):
    if i==1 or i==2:
        print("*"*i)
    elif i==rows:
        print("*"*rows)
    else:
        print("*"+" "*(i-2)+"*")"""
"""rows=int(input("enter the no of rows : "))
for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars="*"*(2*i-1)
    print(spaces+stars)"""

"""row =int(input("enter no of rows: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""

"""def func(rows):
    i=rows
    while i>=0:
        spaces=" "*(rows+1-i)
        stars="*"*(i-1)
        print(spaces+stars)
        i-=1

rows=int(input("enter no of rows: "))
i=1
while i<=rows:
    spaces=" "*(rows-i)
    stars="*"*(i)
    print(spaces+stars)
    if i==rows:
        func(rows)
    i+=1
    
output:
     *
    **
   ***
  ****
 *****
******
 *****
  ****
   ***
    **
     *
"""

"""def func(rows):
    i=rows
    while i>=0:
        stars="*"*(i-1)
        spaces=" "*i
        print(stars+spaces)
        i-=1

rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    stars="*"*i
    spaces=" "*(rows-i)
    print(stars+spaces)
    if i==rows:
        func(rows)"""
# diamond pattern
"""def func(rows):
    i=rows
    while i>=0:
        stars="*"*(2*i-1)
        spaces=" "*(rows-i)
        print(spaces+stars)
        i-=1

rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars="*"*(2*i-1)
    print(spaces+stars)
    if i==rows:
        func(rows)
        
output=*
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *"""

"""name="Avinash"
print("Welcome",name)
str="42"
print(int(str))
tuple=("cat","dog","rabbit")
print(tuple[2])
a=4
b=2
temp=a
a=b
b=temp
print(a,b)
age=int(input("enter you age: "))
print("You are {Age} years old".format(Age=age))
num1=int(input("enter the mum1: "))
num2=int(input("enter the num2: "))
print(num1*num2)
Item="book"
Price=25.99
print("the price of the {item} is {price}".format(item=Item,price=Price))

def func(num):
    if num>0:
        print("positive")
    elif num<0:
        print("negative")
    else:
        print("zero")
num=int(input("enter the number: "))
func(num)

num=int(input("enter the number: "))
if (num%2==0):
    print("even")
else:
    print("odd")

year=int(input("enter the year: "))
if (year%400 and year%4==0 or year%100==0):
    print("leap year")
else:
    print("non leapyear")

for i in range(1,6):
    print(i)

sum=0
i=0
while i<=20:
    sum+=i
    i+=1
print(sum)

str1="Hello"
for i in str1:
    print(i)
list=["apple","grapes","banana","pineapple","strawberry"]
print(list[1])
set={1,2,3,4,5,6,7}
set.add(7)
print(set)"""

"""def func(list):
    new_list=[]
    for i in list:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    return new_list

list1=[5,6,4,1,6,7,3,1]
for i in range(7):
    num=int(input("enter numbers into the list: "))
    list1.append(num)
result=func(list1)
print(result)

tuple=(2012,'December',21)
print(tuple)
def calculate_average(list):
    sum=0
    for i in list:
        sum+=i
    average=sum%len(list)
    return average

list=[]
for i in range(7):
    num=int(input("enter the number into list: "))
    list.append(num)
result=calculate_average(list)
print(result)

def power(base,exponent):
    powers=base**exponent
    return powers

result=power(4,4)
print(result)"""

"""def func(words):
    if words==" ":
        print("the word doesnot contain string")
    return words+func(words)

words=(input("enter the string: "))
result=func(words)
print(result)"""

"""string="I like apples and oranges"
if "apples" in string:
    print(True)
else:
    print(False)

string_count={"i":0}
string="Mississippi"
for i in string:
    if i=="i":
        string_count[i]+=1
print(string_count)

count=0
for i in string:
    if i=="i":
        count+=1
print(count)

string="Python"
reverse_string=string[::-1]
print(reverse_string)

car={"make":"India","model":"Tata nano","Year":"2013"}
print(car["model"])

car["Year"]=2011
print(car)"""

"""name="Avinash"
print("Hello"+name+"!")

num="37"
print(int(num))"""

"""a=2
b=3
a,b=b,a
print(a,b)

a=2
b=3
temp=a
a=b
b=temp
print(a,b)

a=2
b=3
a=a+b
b=a-b
a=a-b
print(a,b)

a=2
b=3
a=a^b
b=a^b
a=a^b
print(a,b)"""

"""def func():
    a=0
    print(a)
    b=1
    print(b)
    for i in range(2,10):
        c=a+b
        a=b
        b=c
        print(c)
func()"""
"""tuple=("apple","banana","cherry","date")
print(tuple[1])"""

"""a=4
b=5
a=a+b
b=a-b
a=a-b
print(a,b)

print("the price of the {item} is {price}".format(item="hat",price="19.99"))

num=int(input("enter the number to check whether the number is even or odd :  "))
if num%2==0:
    print("even")
else:
    print("odd")

num=int(input("enter the number: "))
if num>1:
    for i in range(2,num):
        if (num%i==0):
            print("not prime")
            break
    else:
        print("prime")
else:
    print("the given number should be greatert than 1")


color=["red","yellow","green","red"]
for i in color:
    print("I like"+i)
set={1,2,3,4,5}
set.add(5)
print(set)"""

"""def func(num):
    if num==1:
       return 1
    else:
        return num*func(num-1)
print(func(5))

def func(num):
    a=0
    print(a)
    b=1
    print(b)
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)
func(10)

string="Testing the text for t's."
t=0
for i in string:
    if i=="t":
        t+=1
print("t's in the string: ",t)
dict={"title":"Titanic","author":"jamescameron","year":1998}
print(dict["author"])

dict["title1"]="hello"
dict["title"]="Tenent"

print(dict)

rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    stars="*"*i
    print(stars)

_var=5
print(_var)"""

"""sentence = "Python programming is fun"
words = sentence.split("o")
print(words)
print(len(words))

string="o".join(words)
print(string)
x=10/3
print(x)"""

"""rows=int(input("enter num of rows: "))
for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars="*"*(i*2-1)
    print(spaces+stars)"""

"""string=input("enter the string: ")

for i in range(0,len(string),2):
    even_position=string[i]
    print(even_position,end="")
print()
for i in range(1,len(string),2):
    odd_postion=string[i]
    print(odd_postion,end="")
print()"""

"""string=input("enter the string: ")
for i in range(0,len(string),2):
    even_str=string[i]
    print(even_str,end="")
print()

for j in range(1,len(string),2):
    odd_string=string[j]
    print(odd_string,end="")
print()"""

"""def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
list=[5,3,8,6,7,2]
sort(list)"""

"""def sort(list):
    for i in range(len(list)):
        minpos=i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos=j
        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp
list=[5,3,8,6,7,2]
sort(list)
print(list)"""

"""i=0
while i<10:
    if i==5:
        break
    print(i)
    i+=1

print("  ")
i=0
while i<10:
    i+=1
    if i==5:
        continue
    print(i)"""

"""num1=eval(input("enter number1: "))
num2=eval(input("enter number2: "))
oper=input("enter the operator (+,-,*,/) : ")

if oper=="+":
    print(num1+num2)
elif oper=="-":
    print(num1-num2)
elif oper=="*":
    print(num1*num2)
elif oper=="/":
    print(num1/num2)
else:
    print("operator not found")


print(num1)
print(num2)"""

"""prime=int(input("enter number: "))
if prime>1:
    for i in range(2,prime):
        if (prime%i==0):
            print("not prime")
            break
    else:
        print("prime")"""

"""sum=0
for num in range(2,101):
    i=2
    for i in range(2,num):
        if (num%i==0):
            i=num
            break

    if i is not num:
        sum+=i


print(sum)"""

"""def even(n):
    return n%2==0
def mul(n):
    return n*2
num=[1,2,3,4,5,6,7,8,9]

def sum(a,b):
    return a+b

even_list=list(filter(even,num))
print(even_list)
double_list=list(map(mul,even_list))
print(double_list)

from functools import reduce
sum_of_list=reduce(sum,double_list)
print(sum_of_list)


list=[i for i in range(1,10)]
print(list)"""


"""list=[i for i in range(1,10) if i%2!=0]
print(list)

rows=int(input("enter number of rows: "))"""
"""for i in range(1,rows+1):
    stars="*"*(i*2-1)
    spaces=" "*(rows-i)
    print(spaces+stars)

for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars="*"*i
    print(spaces+stars)
"""

"""for i in range(1,rows+1):
    if i%2==0:
        spaces=" "*(rows-i)
        stars="*"*(i*2-1)
        print(spaces+stars)
    else:
        spaces=" "*(rows-i)
        dash="-"*(i*2-1)
        print(spaces+dash)"""

"""for i in range(1,rows):
    spaces=" "*(rows-i)
    stars="*"*(i*2-1)
    print(spaces+stars)
for j in range(rows,0,-1):
    stars="*"*(j*2-1)
    spaces=" "*(rows-j)
    print(spaces+stars)"""

"""for i in range(1,10):
    if (i==5):
        break
    print(i)

for j in range(1,10):
    if (j==5):
        continue
    print(j)"""
"""
i=0
while i<10:
    if i==5:
        break
    print(i)
    i+=1"""

"""i=1
while i<10:
    i += 1
    if i==5:
        continue
    print(i)"""


"""i=5
while i>0:
    print(i)
    i-=1"""

import math

"""class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        return "Hello i am {Name} & i am {Age} old".format(Name=self.name,Age=self.age)


person1=student("groot",22)
person2=student("honey",21)

print(person1.name)
print(person1.age)

print(person1.greet())
print(person2.greet())"""


"""class BankAccount():
    def __init__(self,AccountNumber,balance):
        self.AccountNumber=AccountNumber
        self.balance=balance

    def deposit(self,Deposit):
        self.Deposit=Deposit
        self.balance=self.Deposit+self.balance
        return "Your Account Balance {Balance}".format(Balance=self.balance)

    def withdraw(self,Withdraw):
        self.Withdraw=Withdraw
        self.balance=self.balance-self.Withdraw
        return "Your Account Balance {Balance}".format(Balance=self.balance)

person1=BankAccount(12345,10000)
person2=BankAccount(67890,20000)

print(person1.deposit(6000))
print(person1.withdraw(100))
print(person2.deposit(100))
print(person2.withdraw(10000))"""


"""num=int(input("enter the number: "))
for i in range(1,10):
    mul=num*i
    print(num,"*",i,"=",mul)"""


"""if num >1:
    for i in range(2,num):
        if (num%i==0):
            print("not prime")
            break
    else:
        print("prime")"""

"""even=[]
odd=[]

for i in range(0,num):
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)"""

"""list=[1,2,3,4,5,6,7,8,9,10]
even_idx=[]
odd_idx=[]
length=len(list)
for i in range(0,length):
    if (i%2==0):
        even_idx.append(list[i])
    else:
        odd_idx.append((list[i]))

print(even_idx)
print(odd_idx)"""

"""percent=int(input("enter percentage obtanined: "))
if percent>90 and percent<100:
    print("A Grade")
elif percent<=90 and percent>80:
    print("B Grade")
elif percent<=80 and percent>70:
    print("C Grade")
elif percent<=70 and percent>60:
    print("D Grade")
elif percent<=60 and percent>50:
    print("E Grade")
else:
    print("Fail")"""


"""str="Hello welcome to my world"
print(str[::-1])
"""

"""def func(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)

func(10,1,2,3,4,5,6)"""


"""x=20
print(x)
def func():
    global x
    x=10
    print(x)

func()
print(x)"""


"""def func():
    global x
    x=20
    print(x)

func()
print(x)"""

"""x=10
def func():
    globals()['x']=100
    print(x)                    # we can modify the global variable using globals( ) function 
                                        exp: globals()['var']= value                                    

func()
print(x)

def fuc():
    global z
    z=10
    print(z)
fuc()
print(z)"""

"""class student():
    school="sist"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def greet(cls):
        return cls.school

    def greetings(self):
        return "hello i am {} i am {} old".format(self.name,self.age)

person1=student("groot",22)
print(student.greet())
print(person1.greet())
print(person1.greetings())"""



"""class student():
    school="sist"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def greet(cls):
        return cls.school

    def greetings(self):
        return "hello i am {} i am {} old".format(self.name,self.age)
    @staticmethod
    def info():
        print("welcome to static method")


person1=student("groot",22)
print(student.greet())
print(person1.greet())
print(person1.greetings())
person1.info()
student.info()"""

"""class Employee:
    Emp_raise=1.04
    Emp_count=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first+"."+last+"@company.com"

        Employee.Emp_count+=1


    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def pay_raise(self):
        return (self.pay * self.Emp_raise)

    @classmethod
    def set_emp_raise(cls,new_raise):
        cls.Emp_raise=new_raise

    @classmethod
    def from_string(cls,new_string):
        first,last,pay=new_string.split("-")
        return cls(first,last,pay)


    @staticmethod
    def check_weekday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp1=Employee("groot","green",10000)
emp2=Employee("hulk","green",20000)



emp3="jhon-dhes-2000"
empx=Employee.from_string(emp3)
print(empx.fullname())
import datetime
new_date=datetime.date(2024,2,5)
print(Employee.check_weekday(new_date))"""


"""class Employee:
    Emp_raise=1.05

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first+"."+last+"@company.com"


    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def pay_raise(self):
        self.pay=int(self.pay*self.Emp_raise)

    @classmethod
    def set_emp_raise(cls,new_raise):
        cls.Emp_raise=new_raise

emp1=Employee("groot","g",2000)
emp2=Employee("Hulk","h",1000)

class Developers(Employee):
    Emp_raise = 2.01

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

class Manager(Employee):

    def __init__(self,first,last,pay,employee=None):
        super().__init__(first,last,pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee

    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def rem_emp(self,emp):
        if emp not in self.employee:
            self.employee.remove(emp)

    def print_all_employee(self):
        for i in self.employee:
            print(i.fullname())

Dev1=Developers ("teddy","t",3000,"python")
Dev2=Developers("donna","d",2000,"c++")


mnrg1=Manager("hanna","deby",30000)
mnrg1.add_emp(Dev2)
mnrg1.add_emp(Dev1)
mnrg1.rem_emp(Dev2)
print(mnrg1.print_all_employee())"""


"""def even(n):
    return n%2==0

num=[1,2,3,4,5,6,7,8,9]

x=list(filter(even,num))
print(x)

def mul(n):
    return n*2

y=list(map(mul,x))
print(y)

def sum(a,b):
    return a+b

from functools import reduce

z=reduce(sum,y)
print(z)"""

"""dicts={"model":"swift","year":2009,"color":"red"}
for key,value in dicts.items():
    print([key,value])"""

"""x={1,2,3,4}
y={1,2}
print(x.intersection(y))
print(x.issubset(y))
print(x.issuperset(y))
z=x.update(y)
print(z)"""

"""x={"groot":{1,2},"hulk":{2,5}}
y={"thor":{3},"groot":{1}}

words=["apple","banana","grapes","apple","orange","banana","melon","cherry","grapes"]

fruits_count={}

for i in words:
    fruits_count[i]=words.count(i)

print(fruits_count)"""

"""strs=input("enter string: ")
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}

for i in strs:
    if i in vowels:
        vowels[i]+=1
print(vowels)"""

"""exp_str="hello welcome to my world"

print(exp_str.count('e'))
print(exp_str.istitle())
print(exp_str.isprintable())
print(exp_str.isspace())
print(exp_str.split())
x=exp_str.split("e")
print(x)
print("e".join(x))"""

"""def fib():
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,10):
        c=a+b
        a=b
        b=c
        print(c)

fib()

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(4))"""

"""import re

str="Hello welcome"

search=re.match("me",str)
if search:
    print("successful")
else:
    print("unsuccessful")

reg=re.findall("He..o",str)
print(reg)
reg=re.findall('[a-z]',str)
print(reg)"""

"""with open("file.txt","r") as file:
    f=file.readlines()
for i in f:
    x=i.strip().split(" ")
    print(x)"""

"""with open("file.txt","w") as file:
    f=file.write("Hello ninja")
    file.close()

with open("file.txt","r") as file:
    x=file.read()
    print(x)"""

"""strs="Hello"
if  not type(strs) is int:
    raise TypeError("it is not integer type")"""

with open("file.txt","a") as file:
    f=file.append("hello")