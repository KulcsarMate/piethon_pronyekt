def válassz(lista):
    while True:
        elem = input("Adja meg a keresni kívánt programozói tétel nevét: ").capitalize()
        good = search(lista, elem)
        if good == False:
            print("Adjon meg egy választ a lehetőségek közül")
        else:
            return good

def search(lista, elem):
    i = 0
    while i < len(lista)-1 and not(elem == lista[i]):
        i += 1
    if not(i < len(lista)-1):
        return False
    else:
        return i

def alkalmaz(szám):
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
    lista = ["Megszámolás", "Összegzés", "Minimum", "Maximum", "Keresés", "Kiválogatás", "Rendezés"]
    alkalmaz(int(válassz(lista)))

main()
