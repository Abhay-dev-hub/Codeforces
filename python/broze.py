code = str(input())
res = ""
for i in range(0,len(code)-1):
    if code[i] and code[i+1] == "-.":
        res += "1"

    if code[i] and code[i+1] == "--":
        res += "2"
    
    if code[i] ==".":
        res += "0"
print(res)
