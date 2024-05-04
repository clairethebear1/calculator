import math

try: 
   num1_str = input("What is your first number?")
   num1 = float(num1_str)
except ValueError:
   print("Please input a number for goodness sakes, this is a calculator! Try again.")
   exit()

try:
  num2_str = input("What is your second number?")
  num2 = float(num2_str)

except ValueError:
   print("Girl. Just put in a second number, please! Try again.")
   exit()

operation_str = input("What operation do you want to do? Add, subtract, etc. You get the point.")
operation_str = operation_str.lower()

def calculate(num1, num2, operation_str):
   if operation_str == "+" or operation_str == "add" or operation_str == "addition":
      print(num1 + num2)

   if operation_str in ["-", "subtract", "subtraction"]:
     print(num1 - num2)

   if operation_str in ["*", "multiply", "multiplication"]:
     print(num1 * num2)

   if operation_str in ["/", "division", "divide"]:
     if num2 == 0:
        print("Cannot divide by zero.")
     else:
        print(num1 / num2)

calculate(num1, num2, operation_str)
