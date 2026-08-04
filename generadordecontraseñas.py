import random
minusculas = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
mayusculas = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Ñ", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
numeros = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
caracteres_especiales =  ("_", ":","-", ",", ";", "!", "¡", "?", "¿")
posiblescaracteres = []
while True:
    pregunta_1 = int(input("¿De cuántos caracteres desea que sea su nueva contraseña?"))
    pregunta_2 = str(input("¿Desea añadir mayúsculas? (si/no)"))
    pregunta_3 = str(input("¿Desea añadir caracteres especiales? (si/no)"))
    pregunta_4 = str(input("¿Desea añadir números? (si/no)"))
    todos_caracteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if pregunta_1 > 100:
        print("No disponemos de esas funciones. No podemos generar contraseñas tan largas")
        continue
    if pregunta_2.lower() == "si":
        todos_caracteres.extend(mayusculas)
    if pregunta_2.lower() == "no":
        print("Sin mayúsculas")
    if pregunta_4.lower() == "si":
        todos_caracteres.extend(numeros)
    if pregunta_2.lower() == "no":
        print("Sin números")
    if pregunta_3.lower() == "si":
        todos_caracteres.extend(caracteres_especiales)
    if pregunta_2.lower() == "no":
        print("Sin caracteres especiales")
    contraseña = ""
    for i in range(pregunta_1):
       contraseña += random.choice(todos_caracteres)
    print(contraseña)