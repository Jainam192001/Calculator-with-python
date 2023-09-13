# CRERATING A CALCULATOR
print ("@CREATED BY JAINAM")
print("THIS IS MY CALCULATOR")

a = int(input("Enter digit1"))
b = int(input("Enter digit2"))
operation = input("bolo bolo kya karu")

if operation == "+":
  print(a+b)
elif operation == "-":
  print(a-b)
elif operation == "*":
  print(a*b)
elif operation == "/":
  print(a/b)
elif operation ==" //":
  print(a//b)
elif operation == "%":
  print(a%b)
elif operation == "**":
  print(a*b)
else:
  print("invalid operation")