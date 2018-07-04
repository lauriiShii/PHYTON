"5.	Crea un programa que compruebe si dos fichas de dominó encajan o no. Las fichas se representarán mediante dos tuplas: (3,4) y (4,6) por ejemplo."

def encajarFichas(ficha1, ficha2):
    if ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[1] or ficha1[1] == ficha2[0]:
        print("Las fichas encajan")
    else:
        print("Las fichas no encajan")

def main():
    ficha1 = (3, 4);
    ficha2 = (4, 6);

    encajarFichas(ficha1, ficha2);

if __name__ == '__main__':
    main();