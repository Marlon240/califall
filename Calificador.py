import time, os
from os import listdir, remove
#funciones con grupos
def crearGrupo(nGrupo ="."):
    file = open(f"calf/{nGrupo}.txt", "w")
    file.close()
    fileExist = existGrupo(nGrupo)
    if fileExist == True:
        print("Grupo creado correctamente")
        time.sleep(2)
    elif fileExist == False:
        print("Ha ocurrido un error")
        time.sleep(2)
def borrarGrupo(nGrupo = "."):
    try:
        fileExist = existGrupo(nGrupo)
        remove(f"calf/{nGrupo}.txt")
        if fileExist == False:
            print("Grupo borrado correctamente")
            time.sleep(2)
    except:
        return False
def existGrupo(grupo = "."):
    content = listdir("calf")
    if not content:
        return breakpoint
    if f"{grupo}.txt" in content:
        return True
    elif f"{grupo}.txt" not in content:
        return False 
#Funciones para calificar
def calfGrupo(grupo):
    while True:
        os.system("clear")
        print(('> Registro de Calificaciones por Grupo <'.title()).center(70,'=')+ '\n')
        materiasY = ["Matematicas", "Ciencias", "Educación Fisica", "Español", "Artes", "Quimica", "Fisica"]
        materiaToCalf = str(input("Que materia desea calificar? "))
        if materiaToCalf in materiasY:
            pass
        else:
            print("No ok")
            time.sleep(2)


#Aplicacion para calificar
def salir(dec):
    answerY = ["Si", "S","s", "yes", "Yes", "y"]
    answerN = ["N", "No", "n"]
    if dec in answerY:
        os.system("clear")
        return breakpoint
    elif dec in answerN:
        os.system("clear")
        menuRegCalif()
def menuRegCalif():
    while True:
        #Preguntar seleccion
        print(('> Registro de Calificaciones <'.title()).center(70,'=')+ '\n')
        print("Seleccione la accion a realizar: ")
        print("1. Crear nuevo grupo")
        print("2. Eliminar un grupo")
        print("3. Registrar calificaciones de un grupo ya existente")
        print("0. Salir")
        try:
            user_inputC = int(input("Seleccione una opcion: "))
            if user_inputC in range(5):
                if user_inputC == 0:
                    while True:
                        os.system("clear")
                        print(('> Registro de Calificaciones <'.title()).center(70,'=')+ '\n')
                        user_dec = str(input("Seguro que desea salir? (S/N): "))
                        dec = salir(user_dec)
                        if dec == breakpoint:
                            os.system("clear")
                            break
                elif user_inputC == 1:
                    while True:
                        os.system("clear")
                        print(('> Registro de Calificaciones <'.title()).center(70,'=')+ '\n')
                        try:
                            nGrupo = int(input("Ingrese el numero del grupo que desea crear: "))
                            if len(str(nGrupo)) == 3:
                                if existGrupo(nGrupo) == True:
                                    print("Ese grupo ya existe.")
                                    time.sleep(2)
                                elif existGrupo(nGrupo) == False:
                                    crearGrupo(nGrupo)
                                    break
                            elif nGrupo == None:
                                break
                            else:
                                print("Los grupos pueden tener solo 3 digitos obligatoriamente ")
                                time.sleep(2)
                                os.system("clear")
                        except ValueError:
                            print("Error, ingrese solamente numeros")
                            time.sleep(2)
                            continue
                        break
                elif user_inputC == 2:
                    while True:
                        os.system("clear")
                        print(('> Registro de Calificaciones <'.title()).center(70,'=')+ '\n')
                        try:
                            numGrupo = int(input("Ingrese el numero del grupo que desea borrar: "))
                            if len(str(numGrupo)) == 3:
                                numGrupo = int(numGrupo)
                                GroupExist = existGrupo(numGrupo)
                                if GroupExist == True:
                                    borrarGrupo(numGrupo)
                                    break
                                elif GroupExist == False:
                                    print("Ese grupo actualmente no existe, digite de nuevo")
                                    time.sleep(2)

                                elif GroupExist == breakpoint:
                                    print("No hay ningun grupo registrado")
                                    time.sleep(2)
                            else:
                                print("Los grupos pueden tener solo 3 digitos obligatoriamente ")
                                time.sleep(2)
                                os.system("clear")
                        except ValueError:
                            print("Error, ingrese solamente numeros")
                        break
                elif user_inputC == 3:
                    os.system("clear")
                    regGrupo()
        except ValueError:
            print("Error, ingrese solamente numeros")
        break
def menuSubirCalf():
    pass
def regGrupo():
    while True:
        try:
            os.system("clear")
            print(('> Registro de Calificaciones por grupo <'.title()).center(70,'=')+ '\n')
            grupotoCalf = int(input("Digite el grupo a calificar: "))
            if existGrupo(grupotoCalf) == True:
                calfGrupo(grupotoCalf)
                break
            else:
                print("El grupo que desea registrar no existe.")
                time.sleep(2)
                continue
        except ValueError:
            print("Error, solo puede digitar un numero de grupo")
        break
def opcionesMenu():
    os.system("clear")
    print(('> Califall <'.title()).center(70,'=')+ '\n')
    print("1. Registrar calificaciones.")
    print("2. Subir calificaciones")
    print("3. Salir")
def menu():
    while True:
        opcionesMenu()
        try:
            user_input = int(input("Seleccione una opcion: "))
            if user_input in range(4):
                if user_input == 1:
                    while True:
                        os.system("clear")
                        menuRegCalif()
                        break
                if user_input == 2:
                    while True:
                        menuSubirCalf()
                        break
            else:
                os.system("clear")
                print("Error solo se aceptan numeros del 1 al 3")
                time.sleep(2)
        except ValueError:
            os.system("clear")
            print("Error, ingrese solamente numeros")

if __name__ == "__main__":
    menu()