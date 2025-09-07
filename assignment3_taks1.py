def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Enter the number of its factorial : "))
print(f"The factorial of your number is : {factorial(n)}")


factorial(n)