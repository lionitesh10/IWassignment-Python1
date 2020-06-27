lo,up=input("Enter range lower upper ").split()
n=int(input("Enter no to be checked "))

def checkInRange(lo,up,n):
    lo,up=int(lo),int(up)

    if n>=lo and n<=up:
        print("{0} is in range {1} and {2}".format(n,lo,up))
    else:
        print("The no is not in range ")

checkInRange(lo,up,n)
