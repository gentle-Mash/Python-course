from PIL import Image, ImageEnhance, ImageFilter
import os

# changing the image extention

img = Image.open('car.jpg')
img.save("car.png")

# opening an image
# img.show()

# resizing the image

new_size = (250,250)
img.thumbnail(new_size)
img.save("resize car.png")
# img.show()

# looping 

for item in os.listdir():
    if item.endswith(".jpg"):
        img2 = Image.open(item)
        image_name , extension = os.path.splitext(item)
        img2.save(f"{image_name}2.png")

img3 = Image.open("vector.jpg")
enhancer = ImageEnhance.Sharpness(img3)
enhancer.enhance(5).save("vector edited.jpg")
# 0 = little blury image
# 1 = original image
# >1 = increased shrpness

img4 =  Image.open("skeliton.jpg")
enhancer2 = ImageEnhance.Color(img4)
enhancer2.enhance(0).save("b&w.jpg")

enhancer3 = ImageEnhance.Brightness(img2)
enhancer3.enhance(5).save("brightened.jpg")

# same goes for contrast just write ImageEnhance.Contrast(your picture)

img4.filter(ImageFilter.GaussianBlur(radius=5)).save("blured.jpg")

