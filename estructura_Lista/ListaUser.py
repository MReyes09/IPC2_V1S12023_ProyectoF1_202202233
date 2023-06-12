import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

from model.Usuario import Usuario
from node.NodoUser import NodoUser


class ListaUser:

    def __init__(self):
        self.cabeza = None

    def Listar_Usuarios(self):
        actual: NodoUser = self.cabeza
        while actual is not None:
            usuario: Usuario = actual.dato
            print(f"Rol: {usuario.get_rol()} nombre: {usuario.get_nombre()} telefono: {usuario.get_telefono()} correo: {usuario.get_correo()} contraseña: {usuario.get_contrasena()}")
            actual = actual.siguiente

    def CargarXML(self, operacion: int):
        # indico el nombre de mi archivo XML y su posicion
        tree = ET.parse('usuarios.xml')
        root = tree.getroot()

        for usuarios in root.findall('usuario'):
            rol: str = usuarios.find('rol').text
            nombre: str = usuarios.find('nombre').text
            apellido: str = usuarios.find('apellido').text
            telefono: int = int(usuarios.find('telefono').text)
            correo: str = usuarios.find('correo').text
            contrasena: str = usuarios.find('contrasena').text

            cargar_User = Usuario(rol, nombre, apellido, telefono, correo, contrasena)

            if operacion == 1:
                self.add_User(cargar_User)

    def get_Nodo_Cabeza(self) -> NodoUser:
        return self.cabeza

    def add_User(self, user: Usuario):
        nuevo_User = NodoUser(user)

        if self.cabeza is None:
            self.cabeza = nuevo_User
        else:
            actual: NodoUser = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_User

    def Iniciar_Sesion(self,  correo_Rec: str, contrasena_Rec: str) -> Usuario:
        actual: NodoUser = self.cabeza
        while actual is not None:
            usuario: Usuario = actual.dato
            if usuario.get_correo() == correo_Rec and usuario.get_contrasena() == contrasena_Rec:
                return usuario
            actual = actual.siguiente
        return None

    def Registrarse(self, rol:str, nombre:str, apellido:str, telefono:int, correo:str, contrasena:str):

         """
         #Guardar el usuario en el XML
         usuario_Nuevo = ET.Element("usuario")

         ET.SubElement(usuario_Nuevo, "rol").text = rol
         ET.SubElement(usuario_Nuevo, "nombre").text = nombre
         ET.SubElement(usuario_Nuevo, "apellido").text = apellido
         ET.SubElement(usuario_Nuevo, "telefono").text = str(telefono)
         ET.SubElement(usuario_Nuevo, "correo").text = correo
         ET.SubElement(usuario_Nuevo, "contrasena").text = contrasena

         tree = ET.parse("usuarios.xml")
         root = tree.getroot()
         root.append(usuario_Nuevo)
         tree.write("usuarios.xml")
         """

         #Guardar el usuario en la lista simple enlazada
         usuario_Nuevo_En_Lista:Usuario = Usuario(rol, nombre, apellido, telefono, correo, contrasena)

         self.add_User(usuario_Nuevo_En_Lista)

         print("El usuario se ha registrado exitosamente \n")

    def actualizar_Usuario(self, userLoged: Usuario):

        actual: NodoUser = self.cabeza

        while actual is not None:

            usuario: Usuario = actual.dato

            if usuario.get_correo() == userLoged.get_correo():

                actual.dato = userLoged
                return userLoged

            actual = actual.siguiente

        print("No se encontro coincidencias")

    def eliminar_Usuario(self, correo: str):

        actual:NodoUser = self.cabeza
        anterior:NodoUser = None
        encontrado = False

        while actual and not encontrado:

            if actual.dato.get_correo() == correo:

                encontrado = True

            else:

                anterior = actual
                actual = actual.siguiente

        if actual is None:

            print("El dato no se encuentra en la lista.")
            return

        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

    def actualizar_XML(self):

        root = ET.Element("usuarios")
        actual: NodoUser = self.cabeza

        while actual is not None:

            usuario: Usuario = actual.dato
            nuevo_Usuario = ET.SubElement(root, "usuario")

            rol = ET.SubElement(nuevo_Usuario, "rol")
            rol.text = usuario.get_rol()

            nombre = ET.SubElement(nuevo_Usuario, "nombre")
            nombre.text = usuario.get_nombre()

            apellido = ET.SubElement(nuevo_Usuario, "apellido")
            apellido.text = usuario.get_apellido()

            telefono = ET.SubElement(nuevo_Usuario, "telefono")
            telefono.text = str(usuario.get_telefono())

            correo = ET.SubElement(nuevo_Usuario, "correo")
            correo.text = usuario.get_correo()

            contrasena = ET.SubElement(nuevo_Usuario, "contrasena")
            contrasena.text = usuario.get_contrasena()

            actual = actual.siguiente

        arbol_xml = ET.ElementTree(root)
        xml_str = ET.tostring(root, encoding="utf-8")
        dom = minidom.parseString(xml_str)
        with open("usuarios.xml", "w") as archivo:
            archivo.write(dom.toprettyxml(indent="   "))
        print("\n Se ha actualiado todos los datos exitosamente en el XML")