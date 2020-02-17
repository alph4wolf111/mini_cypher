# Equipo 4

MSG_INS = 'Opcion no válida, vuelve a ver las instrucciones'


def ver_instrucciones():
    print('Seleccione método a utilizar:')
    print('1.- Cesar \n2.- Plybios\n3.- Vigerene\n4.- Ver instrucciones de nuevo\n5.- Salir')


def seleccion():
    ver_instrucciones()
    while True:
        tipo = input(':')
        if tipo == '1':
            params = cryptDecrypt(tipo)
            cesar(params[0], params[1], params[2])
        elif tipo == '2':
            params = cryptDecrypt(tipo)
            plybios(params[0], params[1])
        elif tipo == '3':
            params = cryptDecrypt(tipo)
            vigerene(params[0], params[1], params[2])
        elif tipo == '4':
            ver_instrucciones()
        elif tipo == '5':
            break
        else:
            print(MSG_INS)
            ver_instrucciones()


def cesar(opc, texto, clave):
    if opc == "1":
        print("Selecciona modo de desplazamineto\n1.Derecha\n2.Izquierda")
        modo = input(":")
        if modo == "1":
            abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            texto = texto.upper()
            cifrado = ""
            for txt in texto:
                if txt in abc:
                    letra = abc.index(txt)
                    letra_nueva = (letra + clave) % len(abc)
                    cifrado += abc[letra_nueva]
                print(txt)
            print("Mensaje cifrado: " + cifrado)
        elif modo == "2":
            abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            texto = texto.upper()
            cifrado = ""
            for txt in texto:
                if txt in abc:
                    letra = abc.index(txt)
                    letra_nueva = (letra - clave) % len(abc)
                    cifrado += abc[letra_nueva]
                print(txt)
            print("Mensaje cifrado: " + cifrado)
        else:
            print(MSG_INS)
            ver_instrucciones()
    else:
        print("Descifrar")
        abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        texto = texto.upper()
        descifrado = ""
        for txt in texto:
            if txt in abc:
                letra = abc.index(txt)
                letra_nueva = (letra - clave) % len(abc)
                descifrado += abc[letra_nueva]
            print(txt)
        print("Mensaje descifrado: " + descifrado)


def plybios(opc, texto):
    cifrado = ""
    texto = texto.upper()
    clave = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15', 'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25', 'L': '31',
             'M': '32', 'N': '33', 'Ñ': '33', 'O': '34', 'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'}
    if opc == "1":
        print("Cifrar")
        for txt in texto:
            if txt in clave:
                cifrado += clave[txt]
        print(cifrado)
    elif opc == "2":
        print("Descifrar")
        n = 2
        texto = [texto[i:i+n] for i in range(0, len(texto), n)]
        for txt in texto:
            for key, value in clave.items():
                if txt == value:
                    cifrado += key
        print(cifrado)

    else:
        print(MSG_INS)
        ver_instrucciones()


def vigerene(opc, texto, clave):
    abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    final = list()
    indice = 0
    texto, clave = texto.upper(), clave.upper()

    for txt in texto:
        i = abc.find(txt)
        if i != -1:
            if opc == '1':
                i += abc.find(clave[indice])
            elif opc == '2':
                i -= abc.find(clave[indice])
            i %= len(abc)
            final.append(abc[i])
            indice += 1
            if indice == len(clave):
                indice = 0
        else:
            final.append(txt)
    print(('').join(final))


def cryptDecrypt(tipo):
    print('Selección de opciones')
    print('1.-Cifrar\n2.-Descifrar')
    opcion = input(':')
    if opcion == '1':
        texto = str(input('Introduzca texto a cifrar: '))
        if tipo == '1':
            try:
                llave = int(input('Introduzca llave: '))
                return opcion, texto, llave
            except ValueError:
                print("Error.")
                seleccion()
        elif tipo == '2':
            try:
                return opcion, texto
            except ValueError:
                print("Error.")
                seleccion()
        elif tipo == '3':
            llave = str(input('Introduzca llave: '))
            return opcion, texto, llave
    elif opcion == '2':
        texto = str(input('Introduzca texto a descifrar: '))
        if tipo == '1':
            try:
                llave = int(input('Introduzca llave: '))
                return opcion, texto, llave
            except ValueError:
                print("Error.")
                seleccion()
        elif tipo == '2':
            try:
                return opcion, texto
            except ValueError:
                print("Error.")
                seleccion()
        elif tipo == '3':
            llave = str(input('Introduzca llave: '))
            return opcion, texto, llave
    else:
        print(MSG_INS)
        seleccion()


seleccion()
