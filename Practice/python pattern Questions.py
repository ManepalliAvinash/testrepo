"""Pattern:

1

2 2

3 3 3

4 4 4 4

5 5 5 5 5"""

"""for i in range(1,6):
    print(str(i) * i)"""

"""Pattern #2: Inverted Pyramid of Numbers
Pattern:

1 1 1 1 1 

2 2 2 2 

3 3 3 

4 4 

5"""

"""rows = int(input("enter no of rows: "))
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print()
    
nter no of rows: 5
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 """

"""rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

enter no of rows: 5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 """

"""rows=int(input("enter no of rows : "))
for i in range(rows,0,-1):
    b=i
    for j in range(0,i):
        print(b,end=" ")
    print()

enter no of rows : 5
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 """

"""rows=int(input("enter no of rows: "))
i=rows
while i>=0:
    print(str(rows)*i)
    i-=1
enter no of rows: 5
55555
5555
555
55
5"""

"""rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
enter no of rows: 5
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 """

"""rows=int(input("enteer no of rows: "))
for i in range(rows,0,-1):
    for j in range(0,i+1):
        print(j,end=" ")
    print()

enteer no of rows: 5
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1 """

"""n = 3  # Number of rows for the pattern
num = 1  # Starting number

# Outer loop for the number of rows
for i in range(1, n + 1):
    # Inner loop for each row
    for j in range(1, i * 2):
        print(num, end=' ')
        num += 1
    print()  # Move to the next line after each row

output:
1 
2 3 4 
5 6 7 8 9 """

"""n = 4  # Number of rows for the pattern
num = 1  # Starting number

# Outer loop for the number of rows
for i in range(1, n + 1):
    # Inner loop for each row
    for j in range(i, 0, -1):
        print(num, end=' ')
        num += 1
    print()  # Move to the next line after each row

output:
1 
2 3 
4 5 6 
7 8 9 10 """

#n = 5  # Number of rows for the pattern

# Loop to iterate through each row
"""for i in range(1, n + 1):
    # Print the first half of the row in increasing order
    for j in range(1, i + 1):
        print(j, end=' ')

    # Print the second half of the row in decreasing order (excluding the first number)
    for j in range(i - 1, 0, -1):
        print(j, end=' ')

    # Move to the next line after each row
    print()

output:
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 """

"""rows=int(input("enter num of rows: "))
for i in range(1,rows+1):
    for j in range(rows,i-1,-1):
        print(j,end=" ")
    for j in range(i,rows+1):
        print(j,end=" ")
    print()

enter num of rows: 5
5 4 3 2 1 1 2 3 4 5 
5 4 3 2 2 3 4 5 
5 4 3 3 4 5 
5 4 4 5 
5 5 """


"""rows=int(input("enter no of rows: "))
even=int(input("even number should start from: "))

for i in range(1,rows+1):
    for j in  range(even,even-(i*2),-2):
        print(j,end=" ")
    print()

enter no of rows: 5
even number should start from: 10
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2 """

"""rows=int(input("enter numb of rows: "))
for i in range(0,rows+1):
    for j in range(0,i+1):
        print(i*j,end=" ")
    print()
enter numb of rows: 6
0 
0 1 
0 2 4 
0 3 6 9 
0 4 8 12 16 
0 5 10 15 20 25 
0 6 12 18 24 30 36 """

"""rows=int(input("enter num of rows: "))
for i in range(1,rows+1):
    num=i*2-1
    for j in range(i):
        print(num,end=" ")
    print()
enter num of rows: 5
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9 """

"""rows=int(input("enter number of rows: "))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
enter number of rows: 5
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 """


#    rows=int(input("enter number of inputs: "))
"""for i in range(0,rows+1):
    spaces=" "*(rows-i)
    stars="*"*(i*2-1)
    print(spaces+stars)"""
"""rows=int(input("enter no of rows: "))
i=1
while i<=rows:
    print("*"*i)
    i+=1"""

"""rows=int(input("enter no of rows: "))
for i in range(rows,0,-1):
    stars="*"*i
    spaces=" "*(rows-i)
    print(spaces+stars)"""

"""rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")"""

"""rows=7
k=2*rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")"""

rows=5
k=2*rows-2
for i in range(6,-1,-1):
    for j in range(0,k):
        print(end=" ")
    k+=1
    for j in range(0,i+1):
        print("*",end=" ")
    print()

"""rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""

"""rows=int(input("enter no of rows: "))
num=1
for i in range(1, rows + 1):
    # Inner loop for each row
    for j in range(i, 0, -1):
        print(num, end=' ')
        num += 1
    print()"""

"""rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    print("*"*i,end=" ")
    print()"""

"""rows=int(input("enter no of rows: "))
for i in range(rows,0,-1):
    spaces=" "*(rows-i)
    stars="*"*i
    print(spaces+stars)"""
rows=int(input("enter no of rows: "))
"""for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""

"""for i in range(rows,0,-1):
    stars="*"*(i)
    spaces=" "*(rows-i)
    print(stars+spaces)"""

"""for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars="*"*(i*2-1)
    print(spaces+stars)"""

"""for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""

"""for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars="*"*(i)
    print(spaces+stars)"""

"""for i in range(rows,0,-1):
    stars="*"*(i*2-1)
    spaces=" "*(rows-i)
    print(spaces+stars)"""


"""def func(rows):
    i=1
    while i<=rows:
        spaces=" "*i
        stars="*"*(rows-i)
        print(spaces+stars)
        i+=1

for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars="*"*(i)
    print(spaces+stars)
    if i==rows:
        func(rows)
output:
enter no of rows: 5
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *"""

"""def func(rows):
    i=rows
    while i>=0:
        stars="*"*(i-1)
        spaces=" "*(rows-i)
        print(stars+spaces)
        i-=1
for i in range(1,rows+1):
    stars="*"*i
    spaces=" "*(rows-i)
    print(stars+spaces)
    if i==rows:
        func(rows)
output:
enter no of rows: 5
*    
**   
***  
**** 
*****
****
*** 
**  
*"""

"""for i in range(1,rows):
    spaces=" "*(rows-i)
    stars="*"*(i*2-1)
    print(spaces+stars)
for i in range(rows,0,-1):
    spaces=" "*(rows-i)
    stars="*"*(i*2-1)
    print(spaces+stars)
enter no of rows: 5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *"""

"""outupt:
enter no of rows: 5
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *"""

"""num=1
for i in range(1,rows):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
output:
enter no of rows: 5
1 
2 3 
4 5 6 
7 8 9 10 """

"""for i in range(rows,0,-1):
    spaces=" "*(i)
    stars="*"*(rows)
    print(spaces+stars)"""
"""for i in range(1,rows+1):
    spaces=" "*i
    stars="*"*(rows)
    print(spaces+stars)
"""

"""for i in range(1,rows):
    stars="*"*rows
    print(stars)"""
"""l=int(input("enter the length: "))
b=int(input("enter the breadth: "))
for i in range(1,b+1):
    if i==1 or i==b:
        print("*"*l)
    else:
        spaces=" "*(l-2)
        stars="*"
        print(stars +spaces+stars)"""

"""for i in range(1,rows):
    if i%2!=0:
        star="*"*i
        spaces=" "*(rows-i)
        print(spaces+star)
    else:
        minus="-"*i
        spaces=" "*(rows-i)
        print(spaces+minus)
for i in range(rows,0,-1):
    if i%2!=0:
        star="*"*i
        spaces=" "*(rows-i)
        print(spaces+star)
    else:
        minus="-"*i
        spaces=" "*(rows-i)
        print(spaces+minus)
output: 
enter no of rows: 5
    *
   --
  ***
 ----
*****
 ----
  ***
   --
    *"""

"""for i in range(1,rows):
    if i%2!=0:
        star="*"*i
        print(star)
    else:
        minus="-"*i
        print(minus)

for i in range(rows,0,-1):
    if i%2!=0:
        star="*"*(i)
        print(star)
    else:
        minus="-"*i
        print(minus)
        
output:
enter no of rows: 5
*
--
***
----
*****
----
***
--
*"""


"""for i in range(0,rows+1):
    if i==0:
        spaces=" "*(rows-i)
        print(spaces+"*")
    else:
        under_score="_"*(i*2-1)
        spaces=" "*(rows-i)
        print(spaces+"*"+under_score+"*")
output:
enter no of rows: 5
     *
    *_*
   *___*
  *_____*
 *_______*
*_________*"""

"""for i in range(rows,0,-1):
    if i==1:
        spaces=" "*(rows-i)
        print(spaces+"*")
    else:
        spaces=" "*(rows-i)
        under_scores="_"*(i*2-3)
        print(spaces+"*"+under_scores+"*")
output=
*_______*
 *_____*
  *___*
   *_*
    *"""

"""for i in range(1,rows):
    if i%2!=0:
        spaces=" "*(rows-i)
        stars="*"*(i*2-1)
        print(spaces+stars)
    else:
        spaces=" "*(rows-i)
        minus="-"*(i*2-1)
        print(spaces+minus)
for i in range(rows,0,-1):
    if i%2!=0:
        spaces=" "*(rows-i)
        stars="*"*(i*2-1)
        print(spaces+stars)
    else:
        spaces=" "*(rows-i)
        minus="-"*(i*2-1)
        print(spaces+minus)

enter no of rows: 5
    *
   ---
  *****
 -------
*********
 -------
  *****
   ---
    *"""

"""for i in range(1,rows+1):
    spaces=" "*(rows-i)
    print(spaces,end=" ")
    for i in range(1,i+1):
        print(i,end=" ")
    print(" ")

output: -
enter no of rows: 5
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5"""
