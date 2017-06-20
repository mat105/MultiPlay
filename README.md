Reproductor de historias multimedia.

Requiere:
- Python 3.x
- Pyglet (pip install pyglet)
- AVBin

El contenido se divide en paginas.

Cada pagina contiene texto, imagenes, sonidos, musica y video (los dos últimos pendientes de implementacion)

Al acceder a una pagina se reproduce el sonido y se dibuja el texto y la imagen en pantalla.

Solo acepta formatos texto .txt, sonido .ogg, imagen .png

El archivo config.txt permite modificar ancho y alto de la ventana y cantidad total de paginas.

Para agregar contenido a una pagina debe agregarse ya sea un texto, una imagen o un sonido en su respectiva carpeta de proyecto.

Ejemplo:

Pagina1:

Crear un archivo de texto y escribir algo alli, luego, guardar ese archivo como 1.txt en la carpeta textos.
Para crear un sonido que se reproducira al entrar a la pagina 2, guardar un archivo de sonido como 2.ogg en la carpeta sonidos.


Para pasar de pagina apretar enter dentro del reproductor.
