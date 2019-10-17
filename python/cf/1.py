def calc(suma, n):
    medie = suma // n
    if medie * n < suma:
        return medie + 1
    return medie



q = int(input())
while q > 0:
    q -= 1
    n = int(input())
    x = input()
    lista = x.split()
    suma = 0
    for i in range(0,n):
        suma += int(lista[i])
    print(calc(suma,n)s)
    
        
