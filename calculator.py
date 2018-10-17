def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def square(x):
    return x*x

def divide(x,y):
    return x/y

print("Choose one of the options below.")
print("Addition=1")
print("Subraction=2")
print("Multiplication=3")
print("Square=4")
print("Division=5")

while True:
    choice = input("Enter choice(1 or 2 or 3 or 4 or 5):")

    try:
        if choice == '1':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1,num2))
        elif choice == '3':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1,num2))
        elif choice == '4':
            num1 = int(input("Enter first number: "))
            print(num1, "*", num1, "=", square(num1))
        elif choice == '5':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            try:
                print(num1, "/", num2, "=", divide(num1,num2))
            except ZeroDivisionError:
                print("Division by 0 now allowed")
            else:
                print("Invalid choice")
    except ValueError:
        print("Please provide integers")


