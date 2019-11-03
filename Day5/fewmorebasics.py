# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 06:29:17 2019

@author: For 
"""



# Some More basic codes
"""
Similar to talking or communicating with some one, you can communicate with 
computer using a programming language.

General communication vs programming
say something:print("")
    listen:input("")
        follow:while, for
"""
print("This is cog")
a=input("Hi , how are u doing")
print(a)

age=input("what is your age")
type(age)
print(age)
newage=int(age)
type(newage)

1. ask your age
2. add 10 years to your age and print it

age=18
print(age+10)
print("Ten years from now i will be",age+10)
input is not same as Input
Input("hi")

a=10
print(A)
print(a)
# add 10 years to your age
newage=age+10       # you get error
newage=int(age)+10 # else use a=int(input)
print("age after 10 years is",newage)
a=10
type(a)
print('a is'+str(a))# why error here. you are tring to add what type with what
print(a)

hi='hello'
hi*3
####
'''Comments'''
# If you do not want some part of the code to compile, you can use 
# for single line
'''
either triple ' or " to open and close section or block
''' 

# Where am I? 
import os
getcwd()
os.getcwd()

 

#What are variables and identifiers?
"""
variable values can be changed.
Variable refers to a Memory location where value is stored

Identifiers are the names we give to identify a variable, function, class,etc.
whenever we give an entity a name, that’s called identifier.
Identifier is nothing but the name we give to refer to a memory location.

Identifiers(variable names) cannot start with digit and cannot contain spl.
characters like &,*,$

"""
 
#What are keywords . how to know available variables in python using code?
'''
Keywords are reserved words in Python. They are used by python language for 
internal processing. So we cannot use it for any user defined actions.
We cannot use a keyword as variable name, function name or any other identifier.
'''
import keyword
keyword.kwlist

kword='for'
if keyword.iskeyword(kword):
    print(kword+ ' is a python keyword')
else: 
    print(kword+ ' is not a python keyword')
    
a,b=10,15
print(a)
print(b)

if (a>b):
    print("yes it is")

else:
    print("is it so")

a=10
type(a)
b='10'
type(b)
#What are data types?
    '''
data type is an attribute of data which tells the compiler or interpreter
how the programmer intends to use the data.

It represents the kind of value that tells what operations can be
 performed on a particular data.
 
 Following are the standard or built-in data type of python:

Numeric
Sequence Type
Boolean
Set
Dictionary
 '''
 #Numeric: int,float,complex
a=5
type(a)
a=9.0
type(a)
b=5+8j
type(b)
 #Sequence: string,list,tuple
hi='hello na'
type(hi)
names=['ajay','karthik','bibhav']
type(names) 
mytup=('jolly','holly','bolly')
type(mytup)
# Difference and usage of list and tuple?########################

'''https://docs.python.org/3/tutorial/index.html'''
#Boolean : true or false

type(True)

a,b=10,5
if(a>b):
    print("a is greater")
else:
    print('b is greater')

#set
'''
unordered collection of data type that is iterable, mutable and 
has no duplicate elements.
'''
#Dictionary
'''
 unordered collection of data values, used to store data 
 unlike other Data Types that hold only single value as an element, Dictionary holds key:value
'''
my_dictionary={}
print(my_dictionary)
cog_courses={1:'dspy',2:'mlpy',3:'ai','institute':'cogni'}
print(cog_courses)

print(cog_courses[1])
print(cog_courses['institute'])

# HOW to list all keys and all values of a dictionary##################
######################################################
Numeric ops:

+,/,//,%,**,+=,-=

 

What are comprehensions in python?

 

What are decorators?

 #####################################################################
 5**3
 5//2
(5%2)
int 
import datetime

x = datetime.datetime.now()

####################
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

#######################
a=b is assigning value b to a
a==b is check ing if a equals b
import os
file_name = 'my_file.txt'
print(os.path.splitext(file_name))
You will get the output:

('my_file', '.txt')

alternate sol:
name, ext = os.path.splitext('file.txt')
name
'file'
ext
'.txt'
###################

https://pynative.com/python-exercises-with-solutions/

########################
1. Take a number n as input and compute the sum of first n numbers.
2. Take len,br as input and compute the area.
3. Find the sum of digits of an integer - a 3 digit natural number
4. Find if the given number is even or odd.
5. IS the given character a vowel or consonant.
6. Is given string a palindrome. ie. anna, amma, liril are palindromes.
######################

     
print("Hello prasanna")

n=int(input("Type your value of n:"))
sum=int(n*(n+1)/2)
print("The sum of first n numbers is :",sum)

prasanna=10
br=5
area=prasanna*br
print(prasanna*br)

length=10
breadth=5
print(length*breadth)

123
1+2+3=6
int(123/100)
123-100
int(23/10)
123/10
23%10
#print(int)
a = int(input("enter a 3 digit natural number: "))
c = 0
while a>0:
    b = a%10
    c = c+b
    a = a//10
print ("sum is: ", c)

nbr = input("Input a 3 digit natural number?")
d1 = int(nbr%100) --123
d2 = nbr-100
d22= d2%10
d3 = nbr-
Sum = d1+d22+d33
print("Sum of all 3 digits of the input number:", Sum)

number=123
a=int((123/100))
print(a)
a=int(a)
b=int(123-100)/10

mynum=input("Enter your 3-digit number:")
type(mynum)
sum=mynum[0]+mynum[1]+mynum[2]
sum=int(mynum[0])+int(mynum[1])+int(mynum[2])
print("sum of digits is:",sum)

num='123' #index will start from 0 till n-1
num[0]
len(num)
mynum='123'
a=int(mynum[1])
print(a)

################################# DAY 6
range() generates the integer numbers between the given start integer to the stop integer,
 which is generally used to iterate over with for loop. 
# find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))

################################ 
C = (5/9) * (F - 32)  
write program to convert farenheit to centigrade
###############################
# vowel or consonant
hi=input("enter ur alphabet")
hi='e'
if (hi=='a'or'e'):
    print("vovel")

else:
    print('consonanat')
    
alphabet = input()

if alphabet == ('a') or ('e') or ('i') or ('o') or ('u'):
    print ('vovel')
#if alphabet == 'a' or alphabet == 'e'
elif alphabet == 'y':
    print("y is sometime a volvel and sometime consonant")
    
else:
    print("consonant")

##############################################
vowels=['a','e','i','o','u']
cha=input("Enter a character: ")
if cha in vowels:
    print(cha,"is vowel")
elif cha == 'y':
    print("Sometimes y is vowel & sometimes y is consonant")
else:
    print(cha,"is consonant")

################################# 
    # what is clour of square in chess board
 
position = input(); # read the position from user
z=int(position[1]) # read the number from input ex: if d5 read z as 5
 
if position[0] == ('a')or('c')or('e')or('g'):
    if z%2 == 0:
        print("white")
   
    else:
        print("Black")
        
       
else: 
    if position[0] == ('b')or('d')or('f')or('h'):
        if z%2 == 0:
           print("Black")
           #print("white")
        else:
            print("White")
           # print("black")
           ########################### Senthil's sol ###########
position = input("enter the position :")
z = int(position[1])
if (position [0] == 'a' or position[0] == 'c' or position[0] == 'e' or position[0] == 'g'):
    if z%2 == 0:
        print ("white")
    else:
        print ("black")
else:
    if (position [0] == 'b' or position[0] == 'd' or position[0] == 'f' or position[0] == 'h'):
        if z%2 == 0:
            print ("black")
        else:
            print ("white")

 
######################################### 
# palindrome
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('amma'))
print(isPalindrome('liril')) 
##########################################
# factorial of number
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
num=int(input("Input a number whose factorial you want : "))
print(factorial(num))
######
Write factorial using while
########################################## 
#function that takes a list and returns a new list with unique elements in list.
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 
###########
how do u add elements to a list
#############################################
# even numbers from list
def is_even_num(l):
    evnum = []
    for n in l:
        if n % 2 == 0:
            evnum.append(n)
    return evnum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
################################################ 
# multiply all numbers in list
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  # total = total *x
    return total  
print(multiply((8, 2, 3, -1, 7)))

########################################## 


        
    
