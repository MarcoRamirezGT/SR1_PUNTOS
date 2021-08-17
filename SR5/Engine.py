# Programa principal
from libraryGame import Renderer, V3, _color

from obj import Texture


width = 1920
height = 1080

rend = Renderer(width, height)

modelTexture = Texture("models/model.bmp")

modelPosition = V3(0, 0, -10)

rend.glLookAt(modelPosition, V3(-5, 5, 0))

rend.glLoadModel("models/dragon.obj",
                 modelTexture,
                 translate=modelPosition,
                 scale=V3(1, 1, 1),
                 rotate=V3(0, 0, 0))


rend.glFinish("sr5.bmp")
