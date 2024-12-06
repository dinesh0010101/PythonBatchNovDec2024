"""
Purpose: Python is a dynamic Typed Language
    programming Languages
        - Classfication
            1. Static-Typed Languages
                -first declare the variables, &
                -then use them
                    int a, float b  # Declaration
                    a=10            # initalization
            
            2. Dyanmic Typed Languages
                - Create when you need, No declaration needed
                    num1=123
                - line or block based execution
    python code-> python byte code -> pythonInterpreter -> c compiler -> machine
    python is slower compared to compiler based languages

"""

num1=100
type(num1)

print(type(num1))

print(num1)
print("num1")

print("num1=",num1,"type=",type(num1))

#works in both static and dynamic typing
num1= 300
print("num1=",num1,"type=",type(num1)) #integer

# Python is a dynamic typed language
num1=300.0
print("num1=",num1,"type=",type(num1)) #Float

num1=300.
print("num1=",num1,"type=",type(num1)) #float

num1=300,
print("num1=",num1,"type=",type(num1)) #typle

num1=300.0
print("num1=",num1,"type=",type(num1)) #float

num1=-0.99
print("num1=",num1,"type=",type(num1)) #float

num1=-0.99j
print("num1=",num1,"type=",type(num1)) #float

num1="300"
print("num1=",num1,"type=",type(num1)) #float

num1=True

#num1=true # PYTHON IS A CASE SENSITIVE LANGUAGE

print("num1=",num1,"type=",type(num1))#boolen

num1=False

#num1=false # PYTHON IS A CASE SENSITIVE LANGUAGE

print("num1=",num1,"type=",type(num1))#boolen

num1=None
print("num1=",num1,"type=",type(num1)) #none

num1="NONE"
print("num1=",num1,"type=",type(num1))#string

num1="none"
print("num1=",num1,"type=",type(num1))#string

# NOTE:Strings need to be declared in quotes
