my_string=input("Enter string ")
def caseCount(data):
    small_case=0
    upper_case=0
    for i in my_string:
        if i.isupper():
            upper_case+=1
        elif i.islower():
            small_case+=1
    print("No of Upper Case Character : ",upper_case)
    print("No of Small Case Character : ",small_case)

caseCount(my_string)