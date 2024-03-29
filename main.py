from controller.CineController import CineController
from controller.HistorialController import HistorialController
from estructura_Lista.ListaUser import ListaUser
from model.Categoria import Categoria
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
historialController = HistorialController()
incremental_Boletos:int = 0

userLoged: Usuario = None

print('Bienvenido a USAC-CINEMA')

# MENU INICIAL DONDE TE PODRAS REGISTAR O INICIAR SESION
iniciar_Sesion: bool = False
salir_App: bool = False

def menuGesteionarSalas():

    opcion: int = None
    global listaCines

    while opcion != 5:
        opcion = int(input("¿Qué deseas hacer?\n"
                           "1. Agregar Sala\n"
                           "2. Modificar Sala\n"
                           "3. Listar Sala\n"
                           "4. Eliminar Sala\n"
                           "5. Salir\n tu respuesta: "))
        if opcion == 1:
            nombre_Cine: str = input("Nombre del cine al que le agregaras una sala\n"
                                     "nombre: ")
            listaCines = cineController.modificar_Cine(listaCines, nombre_Cine, 2)

        elif opcion == 2:

            nombre_Cine: str = input("Nombre del cine al que le actualizaras una sala\n"
                                     "nombre: ")
            listaCines = cineController.modificar_Cine(listaCines, nombre_Cine, 3)

        elif opcion == 3:

            cineController.Listar_Cines_Salas(listaCines)

        elif opcion == 4:

            nombre_Cine: str = input("Nombre del cine al que le eliminaras una sala\n"
                                     "nombre: ")
            listaCines = cineController.modificar_Cine(listaCines, nombre_Cine, 4)


def menuGestionarPelis():

    opcion: int = None

    while opcion != 5:

        opcion = int(input("¿Qué deseas hacer?\n"
                           "1. Crear peliculas\n"
                           "2. Modificar peliculas\n"
                           "3. Listar peliculas\n"
                           "4. Eliminar pelicula\n"
                           "5. Salir\n tu respuesta: "))

        if opcion == 1:

            print("En que categoria quieres agregar la pelicula?\n")
            listaCategoria.Listar_Categorias(3)
            nombreCa: str = input("Tu respuesta: ")
            listaCategoria.update_Categoria(nombreCa, 2)
            print("")

        elif opcion == 2:

            print("En que categoria quieres actualizar la pelicula?\n")
            listaCategoria.Listar_Categorias(1)
            nombreCa: str = input("Tu respuesta: ")
            listaCategoria.update_Categoria(nombreCa, 3)
            print("Se actualizo con exito\n")

        elif opcion == 3:

            print("Todas las peliculas existentes son: \n")
            listaCategoria.Listar_Categorias(2)

        elif opcion == 4:

            print("En que categoria quieres eliminar la pelicula?\n")
            listaCategoria.Listar_Categorias(1)
            nombreCa: str = input("Tu respuesta: ")
            listaCategoria.update_Categoria(nombreCa, 4)
            print("Se elimino con exito\n")

def menuGestionCine():

    opcion: int = None
    global listaCines

    while opcion != 7:

        opcion = int(input("¿Qué deseas hacer?\n"
                           "1. Agregar un Cine\n"
                           "2. Modificar Cine\n"
                           "3. Listar Cines\n"
                           "4. Eliminar Cine\n"
                           "5. Gestionar Salas\n"
                           "6. Archihvo XML\n"
                           "7. Salir\n tu respuesta: "))

        if opcion == 1:

            nombre_Cine:str = input("¿Cuál es el nombre del cine? \n"
                                    "nombre: ")
            listaCines = cineController.agregar_Cine(listaCines, nombre_Cine)
            print("Se agrego el nuevo cine con exito!!!")

        elif opcion == 2:

            nombre_Cine: str = input("Nombre del cine a modificar\n"
                                     "nombre: ")
            listaCines = cineController.modificar_Cine(listaCines, nombre_Cine, 1)

        elif opcion == 3:

            cineController.Listar_Cines_Salas(listaCines)

        elif opcion == 4:

            nombre_Cine: str = input("Nombre del cine a eliminar\n"
                                     "nombre: ")
            listaCines = cineController.eliminar_Cine(listaCines, nombre_Cine)

        elif opcion == 5:

            menuGesteionarSalas()

        elif opcion == 6:

            print("asegurate de actualizar antes de extraer")
            print("1. Actualizar XML    2. Extraer data de XML")
            opcion_XLM = int(input("Tu respuesta: "))

            if opcion_XLM == 1:

                cineController.actualizar_XML(listaCines)



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

                    if userLoged.get_rol() == "cliente":

                        print("Se inicio sesión correctamente\n")
                        print(f"Bienvenido {userLoged.get_nombre()} {userLoged.get_apellido()}")
                        iniciar_Sesion = True

                        # -------- MENÚ DE USUARIO

                        opcion_Menu_Usuario: int = None

                        while opcion_Menu_Usuario != 4:

                            print("MENÚ DE USUARIO \n"
                                  "Este es el menú de usuario ¿Qué deseas hacer ahora? \n"
                                  "1. Ver listado de películas \n"
                                  "2. Ver mis peliculas favoritas \n"
                                  "3. Ver Historial de compras \n"
                                  "4. cerrar sesión")

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
                                        print("\n TU PELICULA FAVORITA SE GUARDO CON EXITO!!\n")

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
                                        validar_Sala: bool = False
                                        no_Asientos: int = 0

                                        while validar_Sala is not True:

                                            numero_Sala: str = input("Tu respuesta: ")
                                            no_Asientos = int(input("¿Cuántos asientos quieres?\n"
                                                                         "Tu resupuesta: "))
                                            validar_Sala = cineController.buscar_Sala_In_Cine(numero_Sala, no_Asientos, listaCines)

                                        monto_Total:int = no_Boletos * 42
                                        print(f"\n Monto total: Q{monto_Total}")
                                        datos_Facturacion: int = int(input("Desea ingresar datos de facturación\n"
                                                                           "1. Si   2. CF\n tu respuesta: "))
                                        if datos_Facturacion == 1:

                                            nombre:str = input("nombre: ")
                                            NIT:str = input("NIT: ")
                                            direccion:str = input("dirección: ")
                                            print(f"\n nombre: {nombre}\n NIT: {NIT}\n direccion: {direccion}")

                                            nombre_Pel:str = findedPelicula.get_titulo()
                                            fechaPel:str = findedPelicula.get_fecha()
                                            horaPel:str = findedPelicula.get_hora()
                                            act_Historial: [] = userLoged.get_historial()
                                            act_Historial = historialController.add_Historial(act_Historial, nombre_Pel, fechaPel, horaPel, no_Boletos, no_Asientos, monto_Total, incremental_Boletos)
                                            copiaUserLoged = userLoged
                                            copiaUserLoged.set_historial(act_Historial)
                                            lista.actualizar_Usuario(copiaUserLoged)
                                            incremental_Boletos = incremental_Boletos + no_Boletos
                                            print("\n Tu compra de boletos fue un exito!!!")

                                        if datos_Facturacion == 2:

                                            nombre_Pel: str = findedPelicula.get_titulo()
                                            fechaPel: str = findedPelicula.get_fecha()
                                            horaPel: str = findedPelicula.get_hora()
                                            act_Historial: [] = userLoged.get_historial()
                                            act_Historial = historialController.add_Historial(act_Historial, nombre_Pel,
                                                                                              fechaPel, horaPel, no_Boletos,
                                                                                              no_Asientos, monto_Total, incremental_Boletos)
                                            copiaUserLoged = userLoged
                                            copiaUserLoged.set_historial(act_Historial)
                                            lista.actualizar_Usuario(copiaUserLoged)
                                            incremental_Boletos = incremental_Boletos + no_Boletos
                                            print("\n Tu compra de boletos fue un exito!!!")

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

                                    print("\n Este es tu historial de boletos comprados\n")
                                    historialController.listar_Historial(userLoged.get_historial())

                                elif opcion_Menu_Usuario == 4:

                                    iniciar_Sesion = False
                                    print("La sesion se cerro con exito \n")

                                else:

                                    print("Esta opcion no es valida, por favor intanta de nuevo")

                            except ValueError:

                                print("La opción brindada no es un número, intenta de nuevo\n")

                    elif userLoged.get_rol() == "administrador":

                        print("Se inicio sesión correctamente\n")
                        print(f"Bienvenido {userLoged.get_nombre()} {userLoged.get_apellido()}")
                        iniciar_Sesion = True

                        # --------- MENU DE ADMINISTRADOR

                        opcion_Menu_Admin: int = None

                        while opcion_Menu_Admin != 10:

                            print("MENU DE ADMINISTRADOR\n"
                                  "Este es el menú de administrador ¿Qué deseas hacer ahora? \n"
                                  "1. Gestionar Usuarios \n"
                                  "2. Gestionar Categorias Y Peliculas \n"
                                  "3. Gestionar Cines y Salas\n"
                                  "10. cerrar sesión")

                            opcion_Menu_Admin = int(input("Tu respuesta: "))

                            if opcion_Menu_Admin == 1:

                                opcion:int = None
                                while opcion != 6:

                                    opcion = int(input("¿Qué deseas hacer?\n"
                                                           "1. Crear usuario\n"
                                                           "2. Modificar usuario\n"
                                                           "3. Listar usuario\n"
                                                           "4. Eliminar usuario\n"
                                                           "5. Archivo XML\n"
                                                           "6. Salir\n tu respuesta: "))

                                    if opcion == 1:

                                        print("Para crear un usuario nuevo, llena los datos que se te piden\n")
                                        rol:str = input("rol (cliente/administrador): ")
                                        nombre: str = input("nombre: ")
                                        apellido: str = input("apellido: ")
                                        telefono: int = int(input("teléfono: "))
                                        correo: str = input("correo electrónico: ")
                                        contrasena: str = input("contraseña: ")

                                        lista.Registrarse(rol, nombre, apellido, telefono, correo, contrasena)

                                    elif opcion == 2:

                                        print("\nPara poder actualizar un usuario, llena la información que a continuacíon se te pide\n")
                                        correo_Usuario_Actualizar:str = input("Correo del usuario que se actualizara: ")
                                        contrasena_Usuario_Actualizar:str = input("Contraseña del usuario que se actualizara: ")
                                        userFinded: Usuario = lista.Iniciar_Sesion(correo_Usuario_Actualizar, contrasena_Usuario_Actualizar)

                                        if userFinded == None:

                                            print("No se encontro ningun usuario con estos datos")

                                        else:

                                            print("\n Cambia solo la información que deseas editar, sino copia y pega lo del parentesis")

                                            userFinded.set_rol(input(f"rol ({userFinded.get_rol()}): "))
                                            userFinded.set_nombre(input(f"nombre ({userFinded.get_nombre()}): "))
                                            userFinded.set_apellido(input(f"apellido ({userFinded.get_apellido()}): "))
                                            userFinded.set_telefono(int(input(f"telefono ({userFinded.get_telefono()}): ")))
                                            userFinded.set_contrasena(input(f"contraseña({userFinded.get_contrasena()}): "))

                                            lista.actualizar_Usuario(userFinded)

                                    elif opcion == 3:

                                        lista.Listar_Usuarios()

                                    elif opcion == 4:

                                        print("\n Escribe el correo del usuario que deseas eliminar: ")
                                        corre_Eliminar: str = input("correo: ")
                                        lista.eliminar_Usuario(corre_Eliminar)
                                        print("El usuario se ha eliminado con exito")

                                    elif opcion == 5:

                                        print("asegurate de actualizar antes de extraer")
                                        print("1. Actualizar XML    2. Extraer data de XML")
                                        opcion_XLM = int(input("Tu respuesta: "))

                                        if opcion_XLM == 1:

                                            lista.actualizar_XML()

                                        elif opcion_XLM == 2:
                                            lista.CargarXML(1)
                                            print("Se han actualizado los datos con exito")

                            elif opcion_Menu_Admin == 2:

                                opcion:int = None

                                while opcion != 7:

                                    opcion = int(input("¿Qué deseas hacer?\n"
                                                       "1. Crear categoria\n"
                                                       "2. Modificar categoria\n"
                                                       "3. Listar categoria\n"
                                                       "4. Eliminar categoria\n"
                                                       "5. Archivo XML\n"
                                                       "6. Gestionar peliculas \n"
                                                       "7. Salir\n tu respuesta: "))


                                    if opcion == 1:

                                        print("LLena la información que se te pide")
                                        nombreCa:str = input("nombre de la categoría: ")
                                        categoria_Nueva:Categoria = Categoria(nombreCa)
                                        listaCategoria.add_Categoria(categoria_Nueva)
                                        print("La categoria se creo con exito\n")

                                    if opcion == 2:

                                        nombreCaFind:str = input("Escribe el nombre de la categoria que quieres modificar\n"
                                                                 "tu respuesta:")
                                        listaCategoria.update_Categoria(nombreCaFind, 1)
                                        print("Se ha modificado con exito todo!")

                                    elif opcion == 3:
                                        tipo_Lista:int
                                        tipo_Lista = int(input("Tipo lista:\n"
                                                                   "1. Categoria y pelicula \n"
                                                                   "2. Solo peliculas \n"
                                                                   "3. Solo categorias\n"
                                                                   "tu respuesta: "))
                                        listaCategoria.Listar_Categorias(tipo_Lista)
                                        print("")

                                    elif opcion == 4:

                                        nombreCa:str = input("Escribe el nombre de la categoria que deseas eliminar\n"
                                                             "tu respuesta:")
                                        listaCategoria.delete_Categoria(nombreCa)

                                    elif opcion == 5:
                                        print("asegurate de actualizar antes de extraer")
                                        print("1. Actualizar XML    2. Extraer data de XML")
                                        opcion_XLM:int = int(input("Tu respuesta: "))

                                        if opcion_XLM == 1:

                                            listaCategoria.actualiar_XML()

                                        elif opcion_XLM == 2:
                                            listaCategoria.CargarXML_Category()
                                            print("Se han actualizado los datos con exito")

                                    elif opcion == 6:

                                        menuGestionarPelis()

                            elif opcion_Menu_Admin == 3:

                                menuGestionCine()

                            elif opcion_Menu_Admin == 10:

                                iniciar_Sesion = False
                                print("La sesion se cerro con exito \n")

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
