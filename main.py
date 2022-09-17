n = int(input("Введите кол-во строк:"))
m = int(input("Введите кол-во столбцов:"))
listC=[]
for i in range(n):
    listC1 = []
    for j in range(m):
        a = int(input("a:"))
        listC1.append(a)
    listC.append(listC1)

for i in listC:
    print(i)


