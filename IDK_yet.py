def válassz(lista):
    while True:
        elem = input("Adja meg a keresni kívánt programozói tétel nevét: ")
        good = search(lista, elem)
        if good == False:
            print("Adjon meg egy választ a lehetőségek közül")
        else:
            return elem

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
    ...

def összegzés():
    ...

def minimum():
    ...

def maximum():
    ...

def keresés():
    ...

def kiválogatás():
    ...

def rendezés():
    ...

def search(lista, elem):
    i = 0
    while i < len(lista) or not(elem == lista[i]):
        i += 1
    if not(i < len(lista)):
        return False
    else:
        return i

def main():
    lista = []
    alkalmaz(válassz(lista))


main()
