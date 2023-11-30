try:
    a=int(input("Enter the number: "))
    print(a/2)
    print(a/0)
except(ArithmeticError,ValueError):
    print("An error Occured\n")