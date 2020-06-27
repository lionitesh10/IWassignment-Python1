t1=[(1,5),(2,4),(3,3),(4,2),(5,1)]

def lambdaSort(my_tuple):
    my_tuple.sort(key=lambda x:x[1])
    return my_tuple

print("Sorted tuple ",lambdaSort(t1))