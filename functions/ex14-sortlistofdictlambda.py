list1=[{"roll_no":1,"marks":99},{"roll_no":2,"marks":80},{"roll_no":3,"marks":50}]
def sortlistdictionary(my_list):
    new_list=sorted(my_list,key=lambda x:x['marks'])
    return new_list
print("Sorted list dictionaries ",sortlistdictionary(list1))