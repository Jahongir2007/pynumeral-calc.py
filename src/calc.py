import pynumeral
import os

num = pynumeral

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")

code = int(input("Enter the number: "))

if code == 1:

    numone = int(input("First number: "))
    numtwo = int(input("Second number: "))

    num.add(

        num = numone,
        set = numtwo

    )

elif code == 2:

    numone = int(input("First number: "))
    numtwo = int(input("Second number: "))

    num.sub(

        num = numone,
        set = numtwo
        
    )

elif code == 3:

    numone = int(input("First number: "))
    numtwo = int(input("Second number: "))

    num.mul(

        num = numone,
        set = numtwo
        
    )

if code == 4:

    numone = int(input("First number: "))
    numtwo = int(input("Second number: "))

    num.div(

        num = numone,
        set = numtwo
        
    )

os.system("pause")
