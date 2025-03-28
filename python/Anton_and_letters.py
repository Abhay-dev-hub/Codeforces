let = str(input())
let = let.replace("{","")
let = let.replace("}","")
let = let.replace(",","")
let = let.replace(" ","")

let = set(let)


print(len(let))
