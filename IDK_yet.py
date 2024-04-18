from random import randint

def válassz(játék, nézők, hossz):
    ez = input("Add meg a megnyitni kívánt fájl nevét: ")
    file = open(f"{ez}", "r", encoding="utf-8")
    line = file.readline().strip()
    while line != "":
        chunk = line.split(";")
        játék.append(chunk[0])
        nézők.append(int(chunk[1]))
        hossz.append(float(chunk[2]))
        line = file.readline().strip()
    file.close()

def alkalmaz(lista):
    good = False
    while good == False:
        niceprint(lista)
        szám = int(input("Add meg a kívánt információ számát: "))-1
        if szám < 0 or szám > 6:
            print("Adjon meg egy jelenlévő elemet!")
        else:
            good == True
    if szám == 0:
        megszámolás()
    elif szám == 1:
        összegzés()
    elif szám == 2:
        minimum()
    elif szám == 3:
        maximum()
    elif szám == 4:
        keresés()
    elif szám == 5:
        kiválogatás()
    elif szám == 6:
        rendezés()

def megszámolás():
    db = 0
    l = []
    for i in range(len(l)):
        db += 1
    return db

def összegzés():
    s = 0
    l = []
    for i in range(len(l)):
        s += l[i]
    return s

def minimum():
    mini = 0
    l = []
    for i in range(len(l)):
        if l[i] < l[mini]:
            mini = i
    return l[mini]

def maximum():
    maxi = 0
    l = []
    for i in range(len(l)):
        if l[i] > l[maxi]:
            maxi = i
    return l[maxi]

def keresés():
    x = 0
    i = 0
    l = []
    while i < len(l) and not(l[i] == x):
        i += 1
    return i < len(l)

def kiválogatás():
    x, i = 0, 0
    l, y = [], []
    for i in range(len(l)):
        if l[i] == x:
            y.append(l[i])
    return y

def rendezés():
    l = []
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

def niceprint(lista):
    for i in range(len(lista)-1):
        print(lista[i], end="; ")
    print(lista[len(lista)-1])

def main():
    játék, nézők, hossz = [], [], []
    válassz(játék, nézők, hossz)
    lista = ["Megszámolás (1)", "Összegzés (2)", "Minimum (3)", "Maximum (4)", "Keresés (5)", "Kiválogatás (6)", "Rendezés (7)"]
    alkalmaz(lista)

main()
