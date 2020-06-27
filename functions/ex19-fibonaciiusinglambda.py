from functools import reduce
fib = lambda x: reduce(lambda y, _: y+[y[-1]+y[-2]],range(x-2), [0, 1]) 
n=int(input("Enter n value "))
print(fib(n)) 
