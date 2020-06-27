n=int(input("Enter a no : "))
def isPrime(number):
    if number>1:
        for i in range(2,number):
            if number%i==0 and number!=i:
                print("Not prime")
                break
        else:
            print("Prime no")
    else:
        print("Not prime")

isPrime(n)            