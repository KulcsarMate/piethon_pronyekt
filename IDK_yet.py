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
    print("asd")

def összegzés():
    print("asd")

def minimum():
    print("asd")

def maximum():
    print("asd")

def keresés():
    print("asd")

def kiválogatás():
    print("asd")

def rendezés():
    print("asd")

def niceprint(lista):
    for i in range(len(lista)-1):
        print(lista[i], end="; ")
    print(lista[len(lista)-1])

def main():
    lista = ["Megszámolás", "Összegzés", "Minimum", "Maximum", "Keresés", "Kiválogatás", "Rendezés"]
    alkalmaz(int(válassz(lista)))

main()
