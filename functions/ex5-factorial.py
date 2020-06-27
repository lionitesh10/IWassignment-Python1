n=int(input("Enter no "))
def factorial(number):
    if number<0:
        print("Negative no not supported")
    else:
        i=1
        fact=1
        while i<=number:
            fact*=i
            i+=1
        print("The factorial of {0} is {1} ".format(number,fact))

factorial(n)