code = str(input())
res = ""
i = 0
while i < len(code):
    if code[i] == ".":
        res += "0"
        i += 1
    elif i + 1 < len(code) and code[i] == "-" and code[i+1] == ".":
        res += "1"
        i += 2
        # he condin true zali amhnun i += 2 kela 
    elif i + 1 < len(code) and code[i] == "-" and code[i+1] == "-":
        res += "2"
        i += 2

print(res)
