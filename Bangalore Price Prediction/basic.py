# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:30:12 2020

@author: ADIL KHAN
"""

print("Hello World!")

print('Abhinav')

print(2.5)

#Single Assignment

a = 5
b = 4.5
c = "Abhinav"

d = True

e = a

'''
If statements
Python supports the usual logical conditions from mathematics:
'''

a = 2000
b = 300

if(b > a):
    print("b is greater than a")


'''
Elif
The elif keyword is pythons way of saying "if the previous conditions were not true, 
then try this condition".
'''

if (b >a):
    print("b is greater than a")

elif (b<a):
    print("b is less than a")

'''
Else
The else keyword catches anything which isn't caught by the preceding conditions.
'''

if(b>a):
    print("b is greater than a")

elif (a ==b):
    print("a and b are equal")	
else:
    print("a is greater than b")


'''
And
The and keyword is a logical operator, and is used to combine conditional statements
'''

a = 200
b = 33
c = 500

if (a>b and c>a):
    print("Both conditions are True")


'''
Or
The or keyword is a logical operator, and is used to combine conditional statements
'''

if (a > b or a > c):
    print("At least one of the conditions is True")
    
'''
Nested If
You can have if statements inside if  statements, this is called nested if statements.
'''

x = 19
if (x > 10):
    print("Above ten,")
    if (x > 20):
        print("and also above 20")
    else:
        print("but not above 20.")


'''
pass
If statements cannot be empty, but if you for some reason have an if  statement 
with no content, put in the pass  statement to avoid getting an error.
'''

a =33
b =200
if (b > a):
    pass


'''
break 
With the break statement we can stop the loop even if the while condition is true:
'''

i = 0
while (i < 6):
    i += 1 
    if (i == 3):
        break
    print(i)  

'''
continue
With the continue statement we can stop the current iteration, and continue with 
the next
'''

i = 0
while (i <6):
    i+=1
    if(i==3):
        continue
    print(i)	

'''
while Loop 
With the while loop we can execute a set of statements as long as a condition is true.
'''

i=1
while(i <6):
    print(i)
    i+=1

'''
For Loop
With the for loop we can execute a set of statements, once for each item in a 
list, tuple, set etc.
'''

fruits=["apple","banana","cherry"]

for x in fruits:
    print(x)

'''
range() Function      0 1 2 3 4 5 
To loop through a set of code a specified number of times, 
we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.
'''

for x in range(6):   
    print(x)
    

'''
The range() function defaults to increment the sequence by 1, however 
it is possible to specify the increment value by adding a third parameter 
range(Start, End, Interval)

(1   ,   5  , 1)  
'''

for x in range (2, 23, 3):
    print(x)

'''
Nested Loops
A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop":
'''

adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]

for x in adj:      x= big
    for y in fruits:  y=apple
        print(x, y)



'''
How to Create List
        nghgvh
        jgjhg  
'''


A1 = [ 4, 4 , 5.2 , "cherry"]

print(A1)


mylist = ["apple","banana","cherry"] 

print(mylist)

#Access Items


mylist[1]

print(mylist[-2])

#Range of Indexes

thislist = ["apple","banana","cherry","orange","kiwi"] 
                        1       2       3
[ start     :     end+1]             [1    : 4  ]

print(thislist[1:4])
                                    [ :4]
                                    
                                    
print(thislist[:4])     

print(thislist[2:])

#Change Item Value

thislist = ["apple", "banana", "cherry"]	

thislist[1] = "orange"

print(thislist)

#Add Items-by append

thislist = ["apple","banana","cherry"]
thislist.append("orange")

print(thislist)

#Add Items-by insert

thislist = ["apple","banana","cherry"]

thislist.insert(1,"orange")

print(thislist)

#Remove Item- by Remove

thislist = ["apple","banana","cherry"]

thislist.remove("banana")

print(thislist)


#pop

thislist = ["apple","banana","cherry"]
thislist.pop()

print(thislist)

#to delete list

thislist = ["apple","banana","cherry"]
del thislist

del thislist[1]  


#to Clear a list

thislist = ["apple","banana","cherry"]
thislist.clear()

print(thislist)

#Copy a List

thislist = ["apple","banana","cherry"]

A =thislist

A[1]=4


thislist[1]='hi'



A =thislist.copy() 

thislist[1]=4

A[1]=6.5

print(mylist)

#Join Two Lists(join or concatenate)

list1 = ["a","b","c"]
list2 = [1, 2, 3]

list3 = list1 + list2

print(list3)



