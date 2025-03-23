def addition(p,Q):
 return p + Q
def substract(p,Q) :
 return p- Q
def multiplication(p,Q):
 return p*Q
def divide(p,Q):
 return p/Q
print("please select the operation.")
print("a.Add")
print("b.substract")
print("c.multiplication")
print("d.divide")
choice = input("please enter choice a/b/c/d:")
num1=input("enter the first number")
num2=input("enter the second number")
if choice == 'a':

 print(num1, "+", num2, "=", addition(num1, num2))

elif choice == 'b':

 print(num1, "-", num2, "=", substract(num1, num2))

elif choice == 'c':

 print(num1, "*", num2, "=", multiplication(num1, num2))
elif choice == 'd':

 print(num1, "/", num2, "=", divide(num1, num2))

else:

 print("This is an invalid input")
 

