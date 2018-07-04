import re

error = True

while (error):
    errorUsuario = True
    errorContrasenia = True

    usuario = str(input("Introduce el nombre de usuario: "))
    contrasenia = str(input("Introduce la contraseña: "))

    if (len(usuario) >= 6 and len(usuario) <= 12):
        if (re.match('\\w+', usuario)):
            errorUsuario = False
        else:
            print("ERROR: El nombre de usuario debe estar compuesto solamente por caracteres alfanumericos")
    else:
        print("ERROR: El nombre de usuario debe tener entre 6 y 12 caracteres")

    if (len(contrasenia) >= 8):
        if (re.match('.?\\d+.?\\W+.?', contrasenia)):
            errorContrasenia = False
        else:
            print(
                "ERROR: La contraseña debera estar compuesta por letras y al menos un numero y un caracter no alfanumerico")
    else:
        print("ERROR: La contraseña debe tener al menos 8 caracteres")

    if (errorUsuario or errorContrasenia):
        error = True
    else:
        error = False
