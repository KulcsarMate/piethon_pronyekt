from random import randint

def válassz(játék, nézők, hossz):
    ez = input("Add meg a megnyitni kívánt fájl nevét: ")
    file = open(f"{ez}.txt", "r", encoding="utf-8")
    line = file.readline().strip()
    while line != "":
        chunk = line.split(";")
        játék.append(chunk[0])
        nézők.append(int(chunk[1]))
        hossz.append(float(chunk[2]))
        line = file.readline().strip()
    file.close()

def alkalmaz(lista, játék, nézők, hossz):
    good = False
    while good != True:
        niceprint(lista)
        szám = int(input("Add meg a kívánt információ számát: "))-1
        if szám < 0 or szám > 5:
            print("Adjon meg egy jelenlévő elemet! \n")
        else:
            good = True
    if szám == 0:
        megszámolás(lista)
    elif szám == 1:
        print(f"Streamelt órák száma: {összegzés(hossz)}")
    elif szám == 2:
        act = minimum(hossz)
        index = keresés(hossz, act)
        print(f"A leghamarabb crashelő stream hossza: {act}, játéka: {játék[index]}, nézőszáma: {nézők[index]}")
    elif szám == 3:
        maximum(lista)
    elif szám == 4:
        kiválogatás(lista)
    elif szám == 5:
        rendezés(lista)

def megszámolás(list):
    db = 0
    for i in range(len(list)):
        db += 1
    return db

def összegzés(lista):
    s = 0
    for i in range(len(lista)):
        s += lista[i]
    return s

def minimum(lista):
    mini = 0
    for i in range(len(lista)):
        if lista[i] < lista[mini]:
            mini = i
    return lista[mini]

def maximum(lista):
    maxi = 0
    for i in range(len(lista)):
        if lista[i] > lista[maxi]:
            maxi = i
    return lista[maxi]

def keresés(lista, elem):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    if i < len(lista):
        return i

def kiválogatás(lista):
    lista, y = [], []
    for i in range(len(lista)):
        if lista[i] >= x:
            y.append(lista[i])
    return y

def rendezés(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def niceprint(lista):
    for i in range(len(lista)-1):
        print(lista[i], end="; ")
    print(lista[len(lista)-1])

def main():
    játék, nézők, hossz = [], [], []
    válassz(játék, nézők, hossz)
    lista = ["Megszámolás (1)", "Összegzés (2)", "Minimum (3)", "Maximum (4)", "Kiválogatás (5)", "Rendezés (6)"]
    alkalmaz(lista, játék, nézők, hossz)

main()
