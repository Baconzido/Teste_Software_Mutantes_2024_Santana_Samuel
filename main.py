from calculator import *

try:
  selection = get_selection()
except ValueError:
    print("Invalid selection.")
    quit()

num1 = get_num("First value: ")
num2 = get_num("Second value: ")


                 
if selection == 1:
  value = add(num1, num2)
elif selection == 2:
  value = subtract(num1, num2)
elif selection == 3:
  value = multiply(num1, num2)
elif selection == 4:
  value = divide(num1, num2)

print(f"========\nThe calculation is: {value}")