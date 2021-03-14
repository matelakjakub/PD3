print("\nZAD1\n")

a=[1-x for x in range (1,11)]
b=[4**x for x in range (8)]
c=[x for x in b if x%2==0]
print(a)
print(b)
print(c)


print("\nZAD2\n")

lista_a= []
for x in range(10):
    lista_a.append(x)
print(lista_a)

lista_a1=[x for x in lista_a if x%2==0]
print(lista_a1)

print("\nZAD3\n")
slownik={"pomelo": "sztuki" , "ziemniaki": "kg" , "jajka": "sztuki", "cebula": "kg"}
slownik_1 = {key for(key,value) in slownik.items() if value=="sztuki"}
print(slownik_1)

print("\nZAD4\n")
def czyprostokatny(a,b,c):
    if(pow(a,2) + pow(b,2) == pow(c,2)):
        print("Trójkąt jest prostokątny")
    else:
        print("Trójkąt nie jest prostokątny")

czyprostokatny(3,4,5)

print("\nZAD5\n")
def pole_trapezu(a=2, b=2, h=4):
    return (1/2*(a+b)*h)

print(pole_trapezu())

print("\nZAD6\n")
ciag=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
wynik=[]
def iloczyn(a=1,b=4,ile=10):
    for a in range(a-1,ile+a-1):
        wynik.append(ciag[a] * b)

    return wynik
print(iloczyn())

print("\nZAD7\n")
def iloczyn_ciagu2(b, *x):
    wynik = []
    for a in x:
        wynik.append(a*b)
    return wynik

print("Pierwszy argument to b, potem elementy ciągu\n", iloczyn_ciagu2(4,5,7,12))

print("\nZAD8\n")
def produkty(**zakupy):
    suma = 0

    for (key,value) in zakupy.items():
        suma+=value
    print(suma)
    print(len(zakupy))

produkty(jajka=7,mleko=5.40)















