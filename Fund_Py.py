"""for i in range(1,5):
    if i==3:
        break
    print(i)

for i in range(1,5):
    if i==3:
        continue
    print(i)

for i in range(1,10):
    if (i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")"""

"""for i in range(0,10):
    if i%2==0:
        continue
    print(i)"""
"""
i=0
while i<5:
    if i==3:
        break
    print(i)
    i+=1

i=0
while i<5:
    i+=1
    if i==3:
        continue
    print(i)"""

"""num =int(input("enter number: "))
for i in range(2,num):
    if (num%i==0):
        print("not prime")
        break
else:
    print("prime")"""

"""sum=0
for i in range(2,101):
    num=2
    for j in range(2,i):
        if (i%j==0):
            num=i
            break
    if num is not i:
        sum+=i
print(sum)"""

"""str1="cat"
str2="act"

str1_sort=sorted(str1)
str2_sort=sorted(str2)
print(str1_sort)
print(str2_sort)

if str1_sort==str2_sort:
    print("it is anagram")
else:
    print("not anagram")"""

"""str1="groot"
reverse_str1=str1[::-1]
print(reverse_str1)
if str1==reverse_str1:
    print("palindrome")
else:
    print("not palindrome")"""

"""num=int(input("enter number: "))
str_num=str(num)
str_len=len(str_num)
sum_str=[int(i)**str_len for i in str_num]
sum_num=sum(sum_str)
print(sum_num)
if sum_num==num:
    print("given num is amstrong num")
else:
    print("not amstrong number")"""

"""for i in range(1,5+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()"""
n=int(input("enter number: "))
"""def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

fib(n)"""

"""def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))"""



