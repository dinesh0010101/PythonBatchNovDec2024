"""
Purpose: Impotance of Indentation



"""

print("Hello World 1")
 #   print("Hello World 2")  # Indentation : unexpectes indent
print("Hello World 3")

# block code - if, else, elif, for, while, def, class, ....
#if 12>3:
#print('12 is greater than 3')
# IndentationError: expected an indented block after "if" statement on line

if 12 > 3:
    print('12 is greater than 3')

if 12 > 3:
    print('greater')
else:
    print('It is lesser')

if 1<2:
    print('case 1')
elif 2>1:
    print('case 2')
else:
    print('case 3')


if 1<2:
    if 2<4:
        if 3<4:
            if 4<5:
                print('LESSER')
            else:
                print('something')
        else:
            print('something')
    else:
        print('something')


for i in range(9):
    print(i)

i=0
while i<10:
    print(i)
    i+=1