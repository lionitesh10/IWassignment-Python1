def insert_sting_middle(brackets, string):
    out = brackets[:2]+string+brackets[2:]
    return out


print(insert_sting_middle("[[]]", "Python"))
print(insert_sting_middle("{{}}", "PHP"))
