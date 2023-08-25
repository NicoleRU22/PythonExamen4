class TablaMultiplicar:
    def __init__(self):
        self.opcion = 0

    def mostrar_menu(self):
        print("Menú:")
        print("1. Guardar tabla")
        print("2. Mostrar tabla")
        print("3. Mostrar línea de la tabla de multiplicar")

    def guardar_tabla(self, numero):
        if 1 <= numero <= 10:
            with open(f"tabla-{numero}.txt", "w") as file:
                for i in range(1, 11):
                    resultado = numero * i
                    file.write(f"{numero} x {i} = {resultado}\n")
            print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")
        else:
            print("El número debe estar entre 1 y 10.")

    def mostrar_tabla(self, numero):
        try:
            with open(f"tabla-{numero}.txt", "r") as file:
                contenido = file.read()
                print(contenido)
        except FileNotFoundError:
            print(f"No se encontró el archivo tabla-{numero}.txt")

    def mostrar_linea(self, numero, linea):
        try:
            with open(f"tabla-{numero}.txt", "r") as file:
                lineas = file.readlines()
                if 1 <= linea <= len(lineas):
                    print(lineas[linea - 1].strip())
                else:
                    print(f"No hay línea {linea} en la tabla.")
        except FileNotFoundError:
            print(f"No se encontró el archivo tabla-{numero}.txt")

    def ejecutar(self):
        while self.opcion != 3:
            self.mostrar_menu()
            self.opcion = input("Seleccione una opción (1/2/3): ")

            if self.opcion == 1:
                numero_ingresado = int(input("Ingrese un número entre 1 y 10: "))
                self.guardar_tabla(numero_ingresado)
            elif self.opcion == 2:
                numero_ingresado = int(input("Ingrese un número entre 1 y 10: "))
                self.mostrar_tabla(numero_ingresado)
            elif self.opcion == 3:
                numero_ingresado= int(input("Ingrese un número entre 1 y 10: "))
                linea = int(input("Ingrese el número de línea a mostrar: "))
                self.mostrar_linea(numero_ingresado, linea)
            else:
                print("Error")

if __name__ == "__main__":
    programa = TablaMultiplicar()
    programa.ejecutar()
