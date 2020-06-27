list1=[{},{},{}]
list2=[{1,2},{},{}]

def checklist(listme):
    empcount=0
    for i in listme:
        empcount+=len(i)
    if empcount==0:
        return True
    else:
        return False
print(checklist(list2))