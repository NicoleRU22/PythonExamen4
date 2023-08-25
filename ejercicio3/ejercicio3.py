import requests

url = "https://unsplash.com/es/s/fotos/perrito"
response = requests.get(url)
if response.status_code == 200:
    with open("imagen.jpg", "wb") as f:
        f.write(response.content)
    print("Imagen descargada exitosamente como imagen.jpg")
else:
    print("No se pudo descargar la imagen")
