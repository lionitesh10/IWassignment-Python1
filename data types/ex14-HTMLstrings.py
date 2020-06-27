def add_tags(tag, content):
    out = "<"+tag+">"+content+"</"+tag+">"
    return out


print("Enter tag and content : ")
tag = input()
content = input()

print(add_tags(tag, content))
