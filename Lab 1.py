Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello, World")
Hello, World
x=1
#The initial value of x is 1.
if x>0:
    print("These are two comments") #Print a string

    
These are two comments
txt=input("Type something to test this out:")
Type something to test this out:
print(txt)

print("Statement1")
Statement1
print("Statement2")
Statement2
#you can write above two statements in the following way

print("Statement1");print("Statement2")
Statement1
Statement2

x=1
if x>0:
    print("This statement has a single space indentation")
    print("This statement has a single space indentation")

    
This statement has a single space indentation
This statement has a single space indentation

x=1
if x>0:
     print("This statement has a single space+tab indentation")
     print("This statement has a single space+tab indentation")

     
This statement has a single space+tab indentation
This statement has a single space+tab indentation

a=1452
type(a)
<class 'int'>
b=(-4587)
type(b)
<class 'int'>
c=0
type(c)
<class 'int'>
g=1.03
type(g)
<class 'float'>
h=-11.23
type(g)
<class 'float'>
i=.34
type(i)
<class 'float'>
j=2.12e-10
type(j)
<class 'float'>
k=5E220
type(k)
<class 'float'>

x=complex(1,2)
type(x)
<class 'complex'>
print(x)
(1+2j)
z=1+2j
>>> type(z)
<class 'complex'>
>>> z=1+2j
>>> type(z)
<class 'complex'>
>>> 
>>> x=True
>>> type(x)
<class 'bool'>
>>> y=false
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    y=false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> NameError: name 'false' is not defined. Did you mean: 'False'?
SyntaxError: invalid syntax
>>> x=True
>>> type(x)
<class 'bool'>
>>> y=False
>>> type(y)
<class 'bool'>
>>> 
>>> str1="String" #Strings start and ends with double qoutes
>>> print(str1)
String
>>> str2="String" #strings starts and ends with single qoutes
>>> print(str2)
String
>>> str3="String' #string start with double qoutes and end with single qoute
SyntaxError: unterminated string literal (detected at line 1)
>>> str1='String" #strings start with single qoute and ends with double qoute
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> str2="Day's" #single qoutes within double qoutes
>>> print(str2)
Day's
>>> str2='Day"s' #double qoutes within single qoutes
>>> print(str2)
Day"s
>>> >>> print("This ia a backslash (\\) mark.")
This ia a backslash (\) mark.
>>> print("This is tab \t mark.")
This is tab      mark.
>>> print("These are \'single qoutes\'")
These are 'single qoutes'
>>> print("These are \"double qoutes\"")
These are "double qoutes"
>>> print("This is a new line\nNew line")
This is a new line
New line
>>> string1 = "PYTHON TUTORIAL"
>>> print(string1[0]) #print first character
P
>>> print(string1[-15]) #print first character
P
>>> print(string1[14]) #print last character
L
>>> print(string1[-1]) #print last character
L
>>> print(string1[4]) #print 4 character
O
>>> print(string1[-11]) #print 4 character
O
>>> print(string1[16]) #out of index range
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> my_list1 = [5, 12, 13, 14] #the list contain all integer values
>>> print(my_list1)
[5, 12, 13, 14]
>>> my_list2 = ['red', 'blue', 'black', 'white'] #the list contains all integer values
>>> print(my_list2)
['red', 'blue', 'black', 'white']
>>> my_list3 = ['red', 12, 112.12] #the string contain a string, an integer and a float value
>>> print(my_list3)
['red', 12, 112.12]

>>> my_list=[]
>>> print(my_list)
[]
>>> color_list=["red", "blue", "green", "black"] #the list have four element indices start at 0 and end at 3
>>> color_list[0] #return the first element
'red'
>>> print(color_list[0],color_list[3]) #print first and last elements
red black
>>> color_list[-1] #return last element
'black'
>>> print(color_list[4]) #create error as the indices is out of range
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> color_list=["red", "blue", "green", "black"] #the list have four element indices start at 0 and end at 3
>>> print(color_list[0:2]) #cut first two elements
['red', 'blue']
>>> print(color_list[1:2]) #cut second item
['blue']
>>> print(color_list[1:-2]) #cut second item
['blue']
>>> print(color_list[:3]) #cut first three items
['red', 'blue', 'green']
>>> print(color_list[:]) #creates copy of original list
['red', 'blue', 'green', 'black']


