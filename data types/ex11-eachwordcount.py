my_string = input("Enter any sentence ")
word = my_string.split()
out = {}
for i in word:
    if i in out:
        out[i] = out[i]+1
    else:
        out[i] = 1
print(out)
