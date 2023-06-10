from controller.CineController import CineController
from estructura_Lista.ListaSala import ListaSala
from estructura_Lista.ListaUser import ListaUser
from model.Usuario import Usuario
from estructura_Lista.ListaCategory import ListaCategory

#EL VALOR POR DEFECTO PARA TODAS LAS PELICULAS ES DE Q42

# Extraigo los datos del xml
lista: ListaUser = ListaUser()
lista.CargarXML(1)
listaCategoria: ListaCategory = ListaCategory()
listaCategoria.CargarXML_Category()
listaCines:[] = []
cineController = CineController()
listaCines = cineController.CargarXML_Cine(listaCines)

userLoged: Usuario = None

print('Bienvenido a USAC-CINEMA')

# MENU INICIAL DONDE TE PODRAS REGISTAR O INICIAR SESION
iniciar_Sesion: bool = False
salir_App: bool = False

while salir_App is not True:

    while iniciar_Sesion is not True:

        print("Este es el menú inicial ¿que deseas hacer ahora?")
        print("1. Iniciar Sesión   2. Registrarse   3. Listado de peliculas   4. Salir de la app")

        try:

            opcion_Menu_Inicial: int = int(input("por favor, elije una opción \n"))

            if opcion_Menu_Inicial == 1:

                print("Por favor, ingresa los siguientes datos\n")
                correo: str = input("Correo electrónico: ")
                contrasena: str = input("Contraseña: ")
                userLoged = lista.Iniciar_Sesion(correo, contrasena)

                if userLoged is not None:

                    print("Se inicio sesión correctamente\n")
                    print(f"Bienvenido {userLoged.get_nombre()} {userLoged.get_apellido()}")
                    iniciar_Sesion = True

                    # -------- MENÚ DE USUARIO

                    opcion_Menu_Usuario: int = None

                    while opcion_Menu_Usuario != 3:

                        print("MENÚ DE USUARIO \n"
                              "Este es el menú de usuario ¿Qué deseas hacer ahora? \n"
                              "1. Ver listado de películas \n"
                              "2. Ver mis peliculas favoritas \n"
                              "3. cerrar sesión")

                        try:

                            opcion_Menu_Usuario = int(input("Tu respuesta: "))

                            if opcion_Menu_Usuario == 1:

                                print("\n¿Cómo quieres el listado?\n"
                                      "1. Por categoría     2. General \n")
                                opcion: int = int(input("Tu respuesta: "))
                                listaCategoria.Listar_Categorias(opcion)

                                print(" ")
                                opcion = int(input("¿Deseas guardar una pelicula a tu lista de favoritos?\n"
                                                   "1. Si   2. No   3. Comprar Boletos\n"))

                                if opcion == 1:

                                    peli_Favorito: str = input("Escribe el nombre de la pelicula: ")
                                    print(" ")
                                    lista_Pelis: [] = userLoged.get_peliFav()
                                    lista_Pelis.append(peli_Favorito)
                                    copiaUserLoged: Usuario = userLoged
                                    copiaUserLoged.set_peliFav(lista_Pelis)
                                    userLoged = lista.actualizar_Usuario(copiaUserLoged)

                                elif opcion == 3:

                                    obtener_TituloP:str = input("¿De qué película quieres comprar boletos (nombre)?\n"
                                                                 "tu respuesta: ")
                                    findedPelicula = listaCategoria.categoria_Buscar_Peli(obtener_TituloP)
                                    print(f"La pelicula es: {findedPelicula.get_titulo()}\n"
                                          f"fecha: {findedPelicula.get_fecha()}\n"
                                          f"hora: {findedPelicula.get_hora()}\n")
                                    no_Boletos:int = int(input("¿Cuántos boletos quieres? \n"
                                                               "Tu respuesta: "))
                                    print("Estas son las salas disponibles, ingresa el numero de sala: \n")
                                    cineController.Listar_Cines_Salas(listaCines)
                                    numero_Sala: str = input("Tu respuesta: ")

                            elif opcion_Menu_Usuario == 2:

                                if len(userLoged.get_peliFav()) == 0:

                                    print("Aún no hay favoritos en tu lista\n")

                                else:

                                    print("\n Estas son tus películas favoritas: \n")
                                    contador: int = 1
                                    for titulos in userLoged.get_peliFav():
                                        print(f"{contador}. Titulo: {titulos}")
                                        contador += 1
                                    print("")

                            elif opcion_Menu_Usuario == 3:

                                iniciar_Sesion = False
                                print("La sesion se cerro con exito \n")

                            else:

                                print("Esta opcion no es valida, por favor intanta de nuevo")

                        except ValueError:

                            print("La opción brindada no es un número, intenta de nuevo\n")

                else:
                    print("No se han encontrado concidencias, intenta de nuevo\n")

            elif opcion_Menu_Inicial == 2:

                print("A continuación se le solicitara la información para registrarse exitosamente\n")
                rol = "cliente"
                nombre: str = input("nombre: ")
                apellido: str = input("apellido: ")
                telefono: int = int(input("teléfono: "))
                correo: str = input("correo electrónico: ")
                contrasena: str = input("contraseña: ")

                lista.Registrarse(rol, nombre, apellido, telefono, correo, contrasena)

            elif opcion_Menu_Inicial == 3:

                print("\n¿Cómo quieres el listado?\n"
                      "1. Por categoría     2. General\n")
                opcion: int = int(input("Tu respuesta: "))
                listaCategoria.Listar_Categorias(opcion)

            elif opcion_Menu_Inicial == 4:

                salir_App = True
                iniciar_Sesion = True
                print("Ejecución de la aplicación finalizada")

            else:
                print("opción no valida \n")

        except ValueError:

            print("La opción brindada no es un número, intenta de nuevo\n")
    # --------  FIN MENÚ PRINCIPAL ----------->
