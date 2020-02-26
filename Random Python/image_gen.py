import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image

def create_image():
    img = Image.new('RGB', [800,800], 255)
    data = img.load()

    bg_color = [0, 0, 255]

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if draw_square(x, y, 300, 100):
                data[x,y] = (
                    x % 255,
                    y % 255,
                    (x + y) % 255
                )
            else:
                data[x,y] = draw_curve_repeat(x, y, img, bg_color)
    path = 'images/'
    name = 'image.png'
    img.save(path + name)
    display_image(path + name)

def is_line(grid_value: int, line_value, pixel_width=5):
    line_val_true = line_value + pixel_width > grid_value > line_value - pixel_width
    return line_val_true

def draw_square(x, y, side_length: int, pixel_width=5):
    x_true = is_line(x, side_length, pixel_width) or is_line(x, side_length * 2, pixel_width)
    y_true = is_line(y, side_length, pixel_width) or is_line(y, side_length * 2, pixel_width)
    x_position_true = side_length + pixel_width/4 > x - side_length > 0
    y_position_true = side_length + pixel_width/4 > y - side_length > 0
    return (x_true or y_true) and y_position_true and x_position_true

def draw_curve_repeat(x, y, img, color: list):
    for count, each in enumerate(color):
        if each < 1:
            color[count] = 1
    curve_options = (((x * y) // img.size[0]) % color[0], ((x * y) // img.size[0]) % color[1], ((x * y) // img.size[0]) % color[2])
    return curve_options

def display_image(filename):
    img=mpimg.imread(filename)
    imgplot = plt.imshow(img)
    plt.show()

create_image()