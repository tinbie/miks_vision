#python2.7 utf8

import pyglet
import numpy
import sys

def load_img_into_array(path):
    global img_height
    global img_width

    img = pyglet.image.load(path)
    imgdata = img.get_image_data()
    img_width = imgdata.width
    img_height = imgdata.height
    img_array = numpy.full((img_height, img_width, 3), 0)
    px_str = imgdata.get_data('RGB', img_width*3)

    i=0
    for row in range(0, img_height):
        for column in range(0, img_width):
            img_array[row][column][0] = ord(px_str[i])
            img_array[row][column][1] = ord(px_str[i+1])
            img_array[row][column][2] = ord(px_str[i+2])
            i=i+3
    return img_array

def convert_rgb_sw(img_array):
    new_image_array = numpy.full((img_height, img_width), 0)
    for row in range(0, img_height):
        for column in range(0, img_width):
             new_image_array[row][column] = (img_array[row][column][0]+img_array[row][column][1]+img_array[row][column][2])//3
    return new_image_array

def filter_img(img_array):
    new_image_array = numpy.full((img_height, img_width), 0)
    for row in range(0, img_height):
        for column in range(0, img_width-3):
            if abs(img_array[row][column]-img_array[row][column+1]) > 20:
                new_image_array[row][column] = 255
            else:
                new_image_array[row][column] = 0
    return new_image_array
            
    
#####################################START

if __name__ == '__main__':
    img_path = sys.argv[1]
    img_array = load_img_into_array(img_path)

    ord_array = convert_rgb_sw(img_array)
    filtered_img_array = filter_img(ord_array)

    filtered_img_array.shape = -1
    img_data = (pyglet.gl.GLubyte * filtered_img_array.size)(*filtered_img_array.astype('uint8'))
    rendered_img = pyglet.image.ImageData(img_width,img_height,"I",img_data,pitch=img_width)
    myspr = pyglet.sprite.Sprite(rendered_img)

    window = pyglet.window.Window(width=400,height=400,resizable=True,caption='dithered image')
    
    @window.event
    def on_draw():
       window.clear()
       myspr.draw()
    
    pyglet.app.run()
