def main():
    while True:
        try:
            n = int(input("Input the number: "))
            print(factorial(n))
            break
        except ValueError:
            print("Enter an integer instead!")

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        print("The factorial does not exist!")
    else:
        return n * factorial(n-1)

main()