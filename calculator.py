import addition
import subtraction
import multiplication
import division

num1 = float(input("Enter first number: "))
num2 = float(input ("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter: ")

if choice == "1":
    print("Result:", addition.add(num1, num2))
    pass
elif choice == "2":
    print("Result:", subtraction.sub(num1, num2))
    pass
elif choice == "3":
    print("Result:", multiplication.multiply(num1, num2))
    pass
elif choice == "4":
    print("Result:", division.divide(num1, num2))
    pass
else :
    print("Invalid choice!")