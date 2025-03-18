#!/usr/bin/env python
# coding: utf-8

# ### python start 
# 

# In[2]:


#A COMMENT  1 # THIS SINGLE LINE COMMENT ,2  ''' ''' THIS IS MULTI LINE COMMENT

# B CASE SENSITIVITY  ... NAME,Name name diffrent variable consider in PYTHON

NAME='12'
Name='13'
name="rupali"
print(NAME,Name,name)


# 

# In[8]:


## CindeNTATION  refers to adding spaces or tabs at the beginning of a 
                 #line to structure the code. It helps in improving readability and maintaining code organization.

def greet():
    print("Hello, World!")  # Indented inside the function

greet()  # No indentation needed her


# In[39]:


## D line contination

total= 10+29+78+\
34+32


print(total)




# In[45]:


# multiple statments on single line
x=12;y=23; z=x+y;  s=x-y;
print(z);print(s)


# ## symantice inn python

# In[75]:


# variable assignment 
name =90; p="POOYa"; 
print(type(name),type(p))


# In[91]:


# type infernce
variable1 =10;
variable ="ryo";
print(type(variable1))
print(type(variable))


# In[99]:


age=23
if age>22:
    print(age)
#print(age) this not print not indentation


# In[118]:


##ex of indentation

if True:
    print("corect indentation")
    if False:
        
        print("not indentation")
print("hii")
print("if block outside")




# ## 2  variable

# In[131]:


# declearing and assigning variable 
a=23; b=9.0; name='KFC'; student=True;
print("a",a);print("b",b); print("name",name);
print("student",student)


# ### VARIABLE TYPES

# In[159]:


#The same variable (x) can hold different types of data at different times.
 #Python automatically detects the type when the value changes.

X=13
print(type(X))
print(X,type(X))

X='hjk'
print(type(X))
print(X,type(X))

X=True
print(type(X))




# ## TYPE CHEAKING AND CONVERSION

# In[161]:


# TYPE CHEAKING
AGE=23
print(AGE)

# type conversion
a=float(AGE)

print(a,type(a))


b=str(AGE)

print(b,type(b))


# In[155]:


r="rull"
s=float(r)
print(type(s))  #ValueError: could not convert string to float: 'rull'


# # how to give user inout

# In[166]:


a=input('WHAT IS A')
print(a)
print(a,type(a))


# In[172]:


# CALCULATOR
n1=int(input("enter the first no"))
n2=int(input("enter second no"))
sum = (n1+n2)
product = (n1-n2)

print(sum)
print(product)


# In[14]:


"""
This is a simple calculator program in Python.
It takes two numbers and an operator as input from the user and performs the respective arithmetic operation.

Functions:
- calculate(num1, num2, operator): Performs the selected operation.

Valid operators:
- '+' for addition
- '-' for subtraction
- '*' for multiplication
- '/' for division (with zero-division handling)
"""

def calculate(num1, num2, operator):
    """Performs basic arithmetic operations based on the given operator."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error! Division by zero.")
            return None
    else:
        print("Invalid operator!")
        return None

if __name__ == "__main__":
    # Taking input from the user
    num1 = float(input("Enter first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    # Performing calculation
    result = calculate(num1, num2, operator)
    
    # Displaying the result if valid
    if result is not None:
        print(f"Result: {result:.2f}")


# # intro OPRETERS

# In[ ]:




