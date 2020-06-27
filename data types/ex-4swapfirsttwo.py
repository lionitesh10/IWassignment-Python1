first_string = input("Enter first string ")
second_string = input("Enter second string ")

f2 = first_string[:2]
s2 = second_string[:2]

res1 = first_string.replace(f2, s2)
res2 = second_string.replace(s2, f2)

print(res1+" "+res2)
