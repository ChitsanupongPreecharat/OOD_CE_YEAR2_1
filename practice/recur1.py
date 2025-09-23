def factorial(n):
    if n == 0 :
        return 1
    return n * factorial(n-1)

num = input("Enter Number : ")
print(factorial(int(num)))