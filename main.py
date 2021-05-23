from PIL import Image
import math

rgb_values = [
    (233, 236, 236), #white
    (248, 198, 39), #ye
    (237, 141, 172), #pink 
    (112, 185, 25), #lime
    (58, 175, 217), #lblue
    (240, 118, 19), #orange
    (142, 142, 134), #lgray
    (189, 68, 179), #magenta
    (21, 137, 145),  #cyan
    (84, 109, 27),  #green
    (121, 42, 172),  #purple
    (114, 71, 40),  #brown
    (161, 39, 34),  #red
    (62, 68, 71), #gray
    (53, 57, 157),   #blue
    (20, 21, 25)   #black
]

greyscale_values = [
    235, #white
    195, #yellow
    173, #pink
    145, #lime
    144, #light blue
    143, #orange
    141, #light gray
    116, #magenta
    103, #cyan
    92, #green
    89, #purple
    80, #brown
    75, #red
    66, #gray
    56, #blue
    21 #black
]

blocks = [
    "white_wool",
    "yellow_wool",
    "pink_wool",
    "lime_wool",
    "light_blue_wool",
    "orange_wool",
    "light_gray_wool",
    "magenta_wool",
    "cyan_wool",
    "green_wool",
    "purple_wool",
    "brown_wool",
    "red_wool",
    "gray_wool",
    "blue_wool",
    "black_wool"
]

code = []

def process_image():
    im = Image.open("victor.png").convert("RGBA")
    im.thumbnail((50, 50))
    im.save("output.png")
    width, height = im.size
    for y in range(height): 
        for x in range(width):
            pixel = im.getpixel((x, y))
            if pixel[3] != 0:            
                i = 0         
                index = 0   
                minimumDist = 255*255 + 255*255 + 255*255 + 1
                for color in rgb_values:
                    rDiff = pixel[0] - color[0]
                    gDiff = pixel[1] - color[1]
                    bDiff = pixel[2] - color[2]
                    distance = rDiff*rDiff + gDiff*gDiff + bDiff*bDiff

                    if distance < minimumDist:
                        minimumDist = distance
                        index = i
                    i += 1
                block = blocks[index]
                code.append("setB(<{}, {}, 5>, {}, rel)\n".format(width-x, height-y, block))



def main():
    rgb_values.reverse()
    blocks.reverse()
    code.append("var rel:bool = true\n")

    for string in blocks:
        code.append("var {}:block = #{}\n".format(string, string))

    process_image()

    with open("output.txt", "a") as f:
        for string in code:
            f.write(string)

if __name__ == "__main__":
    main()