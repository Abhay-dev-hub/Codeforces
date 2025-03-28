t = int(input())
res = 0
for _ in range(0,t):
    x = str(input())
    if x == "Tetrahedron":
        res += 4
    if x == "Cube":
        res += 6
    if x == "Octahedron":
        res += 8
    if x == "Dodecahedron":
        res += 12
    if x == "Icosahedron":
        res += 20
print(res)
