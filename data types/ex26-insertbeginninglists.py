list1=[1,2,3,4]
string='emp'
list2=[]
for i in list1:
    list2.append(string+str(i))
list1=list2
print(list1)