from PIL import Image, ImageDraw

img = Image.open("image.jpg")
draw = ImageDraw.Draw(img)
draw.text((150, 150), "туц", fill="red")
img.save("watermark.jpg")