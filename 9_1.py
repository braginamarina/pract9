from PIL import Image

img = Image.open("image.jpg")
img.show()

print(img.size)
print(img.format)
print(img.mode)