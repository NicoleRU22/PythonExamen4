from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()

    fuentesDisponibles = figlet.getFonts()
    print("Estas son las fuentes disponibles:")
    for fuente in fuentesDisponibles:
        print(fuente)

    fuenteSeleccionada = str(input("Ingresar el nombre de la fuente seleccionada: "))
    if not fuenteSeleccionada:
        fuenteSeleccionada = random.choice(fuentesDisponibles)
    
    texto_imprimir = input("Ingresar el texto que desea imprimir: ")
    
    figlet.setFont(font=fuenteSeleccionada)
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()
