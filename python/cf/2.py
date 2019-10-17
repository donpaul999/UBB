t = int(input())
while t > 0 :
    t -= 1
    x = input()
    lista = x.split()
    if int(lista[0]) - int(lista[1]) == 1:
        print("NO")
    else:
        print("YES")
