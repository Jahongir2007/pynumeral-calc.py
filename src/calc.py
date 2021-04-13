# upload pynumeral:
import pynumeral
import os

# save pynumeral function in num variable
num = pynumeral

# menu:
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")

# enter number:
inp_num = int(input("Enter number: "))

# add:
if inp_num == 1:
  a = int(input("First number: "))
  b = int(input("Second number: "))
  num.add(
  
    num = a,
    set = b

  )
  
 # subtract:
elif inp_num == 2:
  a = int(input("First number: "))
  b = int(input("Second number: "))
  num.sub(
  
    num = a,
    set = b

  )
  
# multiply:
elif inp_num == 3:
  a = int(input("First number: "))
  b = int(input("Second number: "))
  num.mul(
  
    num = a,
    set = b

  )
  
  # division:
elif inp_num == 4:
  a = int(input("First number: "))
  b = int(input("Second number: "))
  num.div(
  
    num = a,
    set = b

  )

os.system("pause")
