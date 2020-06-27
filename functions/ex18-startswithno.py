my_string=input("Enter your String ")

checkNo = lambda x: True if x.isnumeric() else False
print(checkNo(my_string))