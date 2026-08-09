agenda = [
    ["Carlos","6181234567"],
    ["Adrian","6182332456"],
    ["Luis","6182223444"]
]

print(agenda)

for i in agenda:
    print(i)

lista = ""
for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

lista = ""
for r in range(0,3):
    for c in range(0,2):
            lista += f"{agenda[r][c]}, "
    lista += "\n"

print(lista)