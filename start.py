import pyglet

pyglet.lib.load_library('avbin')
pyglet.have_avbin = True

class Config():

    def read(self):
        try:
            with open("config.txt") as f:
                lines = f.readlines()

                for k in lines:
                    if "ANCHO" in k:
                        self.width = int(str.split(k, "=")[1])
                    elif "ALTO" in k:
                        self.height = int(str.split(k, "=")[1])
                    elif "PAGINAS" in k:
                        self.tot_pages = int(str.split(k, "=")[1])
                    else:
                        print("ERROR")
        except OSError:
            print("UNABLE TO RUN WITHOUT config.txt FILE IN PROJECT DIRECTORY.")
            exit()

    def __init__(self):
        self.width = 800
        self.height = 600
        self.tot_pages = 0

        self.read()



config = Config()
window = pyglet.window.Window( config.width, config.height )

paginas = []

numero_pagina = 0


class Pagina():

    def _parse_file(self):
        lines = ""
        self.texto = ""
        self.label = None
        self.imagen = None
        self.music = None
        self.sound = None

        try:
            with open("textos/{}.txt".format(self.numero)) as myfile:
                lines = myfile.readlines()

            self.texto = ''.join(lines)
            self.label = pyglet.text.Label(self.texto,
                                           font_name='Times New Roman',
                                           font_size=16,
                                           x=0, y=0,
                                           width=window.width, multiline=True,
                                           anchor_x='left', anchor_y='bottom')
        except OSError:
            pass


        try:
            self.imagen = pyglet.resource.image("imagenes/{}.png".format(self.numero))
        except Exception:
            pass

        try:
                self.sound = pyglet.resource.media("sonidos/{}.ogg".format(self.numero), False)
        except Exception:
            pass

        try:
            self.music = pyglet.resource.media("musica/{}.ogg".format(self.numero), True)
        except Exception:
            pass

        try:
            self.video = pyglet.resource.media("videos/{}.mp4".format(self.numero), True)
        except Exception:
            pass


    def on_enter(self):
        if self.music:
            self.music.play()
        if self.sound:
            self.sound.play()
        if self.video:
            self.video.play()

    def draw(self):
        if self.imagen:
            self.imagen.blit(0, 0)
        if self.label:
            self.label.draw()

    def __init__(self, numero):
        self.numero = numero
        self._parse_file()





@window.event
def on_key_press(symbol, modifiers):
    global numero_pagina

    if symbol == pyglet.window.key.ENTER:
        if numero_pagina+1 < config.tot_pages:
            numero_pagina += 1
            paginas[numero_pagina].on_enter()


@window.event
def on_draw():
    window.clear()
    paginas[numero_pagina].draw()


def start():
    global paginas

    paginas = [ Pagina(k+1) for k in range(config.tot_pages) ]

    if config.tot_pages > 0:
        pyglet.app.run()
    else:
        print("UNABLE TO PLAY WITHOUT PAGES")


start()