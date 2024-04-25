from os import truncate
from random import randint

def kerdes():
    choice = input("Mit szeretne tenni?\nAdatot rögzíteni? Ha igen, akkor írja 'adat'\nStatisztikát látni? Ha igen, akkor írja 'statisztika'\n")
    if choice == "adat":
        rogzit()
    if choice == "statisztika":
        return True
    next = input("Akar statisztikát látni?(i/n)")
    if next == "i":
        return True

def rogzit():
    ez = input("Adja meg a fájlt, amelybe rögzíteni szeretne: ")
    file = open(f"{ez}.txt", "a", encoding="utf-8")
    print("Minta:\nLethal Company;285;1.2\nFormátum:\nstr;int;float")
    line = input("Adja meg a rögzíteni kívánt adatot a minta szerint: ")
    file.write(f"{line}")
    next = input("\nAkar-e többet írni?(i/n) ")
    while next != "n":
        print("Minta:\nLethal Company;285;1.2\nFormátum:\nstr;int;float")
        line = input("Adja meg a rögzíteni kívánt adatot a minta szerint: ")
        file.write(f"{line}\n")
        next = input("Akar-e többet írni?(i/n) ")
    file.close()

def valassz(jatek, nezok, hossz):
    ez = input("Add meg a megnyitni kívánt fájl nevét (be1 / be2): ")
    print()
    file = open(f"{ez}.txt", "r", encoding="utf-8")
    line = file.readline().strip()
    while line != "":
        chunk = line.split(";")
        jatek.append(chunk[0])
        nezok.append(int(chunk[1]))
        hossz.append(float(chunk[2]))
        line = file.readline().strip()
    file.close()

def bekerd(lista):
    good = False
    while good != True:
        niceprint(lista)
        szam = input("Add meg az ismerni kívánt információ számát (ha nem akar választani, írja 'random'): ")
        if szam == "random":
            szam = randint(0, 6)
        else:
            szam = int(szam)-1
        if szam < 0 or szam > 6:
            print("\nAdjon meg egy jelenlévő elemet! \n")
        else:
            good = True
    print()
    return szam

def alkalmaz(lista, jatek, nezok, hossz):
    szam = bekerd(lista)
    if szam == 0:
        ora = input("Adja meg ismerni kívánt maximum hosszt (ne írjon semmit, ha az alapértelmezett 1 órát szeretné használni): ")
        if ora == "":
            ora = 1
        print(f"\nA stream {megszamolas(hossz, float(ora))}-szer crashelt {ora} óra elélrése előtt.")
    elif szam == 1:
        print(f"Streamelt órák száma: {osszegzes(hossz)}")
    elif szam == 2:
        act = minimum(hossz)
        print(f"A leghamarabb crashelő stream {act} óráig tartott.")
    elif szam == 3:
        print(f"A legnagyobb nézőszám {maximum(nezok)} volt")
    elif szam == 4:
        num = input("Milyen számnál kevesebb nézővel rendelkező steam-et keres (ne írjon semmit, ha az alapértelmezett 100-at használná): ")
        if num == "":
            num = 100
        print(f"\nStreamelt játékok, {num} amelyet-nál kevesebben néztek:")
        act = kivalogatas(jatek, nezok, int(num))
        niceprint(act)
    elif szam == 5:
        rendezes(hossz, nezok, jatek)
        file = open("Rendezett.txt", "a", encoding="utf-8")
        file.truncate(0)
        file.seek(0)
        for i in range(len(hossz)):
            file.write(f"{jatek[i]};{nezok[i]}; {hossz[i]} \n")
        print("Fájl létrejött 'Rendezett.txt' néven.")
        file.close()
    elif szam == 6:
        niceprint(jatek)
        kivant_elem = input("Adja meg az elemt, amely streamjéről többet szeretne megtudni: ").title()
        index = kereses(jatek, kivant_elem)
        while index == None:
            print("\nA megadott elem helytelen.")
            kivant_elem = input("Adja meg az elemt, amely streamjéről többet szeretne megtudni: ").title()
            index = kereses(jatek, kivant_elem)
        print(f"\nA keresett stream összes adata: \nStreamelt játék: {jatek[index]}\nStream hossza: {hossz[index]}\nNézők száma: {nezok[index]}")

        

def megszamolas(lista, limit):
    db = 0
    for i in range(len(lista)):
        if lista[i] < limit:
            db += 1
    return db

def osszegzes(lista):
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

def kereses(lista, elem):
    i = 0
    while i < len(lista) and not(lista[i].title() == elem):
        i += 1
    if i < len(lista):
        return i

def kivalogatas(lista1, lista2, kuszob):
    eredmeny = []
    for i in range(len(lista1)):
        if lista2[i] < kuszob:
            eredmeny.append(lista1[i])
    return eredmeny

def rendezes(lista, masik, jatek):
    for i in range(len(lista)):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                jatek[j], jatek[j+1] = jatek[j+1], jatek[j]
                masik[j], masik[j+1] = masik[j+1], masik[j]

def niceprint(lista):
    for i in range(len(lista)):
        print(lista[i], end="\n")

def main():
    quest = kerdes()
    if quest == None:
        quit()
    jatek, nezok, hossz = [], [], []
    valassz(jatek, nezok, hossz)
    lista = ["Megszámolás (1)", "Összegzés (2)", "Minimum (3)", "Maximum (4)", "Kiválogatás (5)", "Rendezés (6)", "Keresés (7)"]
    alkalmaz(lista, jatek, nezok, hossz)

main()
