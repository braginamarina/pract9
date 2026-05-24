from PIL import Image

img = Image.open("image.jpg")

w, h = img.size

small = img.resize((w // 3, h // 3))
small.save("small.jpg")

horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontal.save("horizontal.jpg")

vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical.save("vertical.jpg")