# Import para tesseract, responsable de pasar imagen a texto y PIL, libreria que pernite abrir imagenes
import pytesseract 
from PIL import Image

import os
import getpass

user = getpass.getuser()


pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

class get_image_text:
    # dir_path = os.path.dirname(os.path.realpath())
    dir_path = os.getcwd()
    print('Path: ' + dir_path)
    # Abrir imagen
    # Encontrar una manera mas elegante de buscar la ruta
    img = Image.open(f'{dir_path}/script/files/large.png')

    text = pytesseract.image_to_string(img)

    print('Texto ->' +  text)

    f = open(f'{dir_path}/script/demo.txt', "w")

    f.write(text)

    f.close()

get_image_text()