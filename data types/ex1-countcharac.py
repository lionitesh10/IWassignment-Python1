import operator
my_string = input("Enter string ")
out = {}
for i in my_string:
    if i in out:
        out[i] += 1
    else:
        out[i] = 1
sorted_out = dict(
    sorted(out.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_out)
