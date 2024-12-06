"""
Purpose: print() function syntax and usage

"""

name ="Dinesh" #str

print("name =",name)
print("Name of the student is name")

#       str                      str
print("Name of the student is"+ name)
print("Name of the student is "+ name)
print()

print("Name of the student is",name)
print("Name of the student is",name,sep=" ")
print("Name of the student is",name,sep="-")
print("Name of the student is",name,sep="")

print(1,2,3,4,5,6,7) #default sep=" "
print(1,2,3,4,5,6,7,sep=" ")
print()

print(1,2,3,4,5,6,7,sep="~")
print(1,2,3,4,5,6,7,sep="_")
print(1,2,3,4,5,6,7,sep=":")
print()


#NOTE: Python is dynamic typed language
name=12345
print("Name of student is", name)

#           str             int
#print("name of student is"+name)
#TypeError: can only concatenat str (not "int") to str

#NOTE: Python is a strictly typed language

print("1 + 2        =", 1 + 2)  # addition
print("'1' + '2'    =", "1" + "2")  # string concatenation
print()

# 1 + '2' # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# type converters - str(), int(), float()
print("1 + int('2') =", 1 + int("2"))
print("str(1) + '2' =", str(1) + "2")

print()
print("int('234')   =", int("234"))

# print("int('23.4')  =", int('23.4')) # ValueError: invalid literal for int() with base 10: '23.4'
# print("int('two')  =", int('two')) # ValueError: invalid literal for int() with base 10: 'two'

print("Name of Student is" + str(name))