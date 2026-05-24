from PIL import Image, ImageFilter

for i in range(1, 6):
    img = Image.open(f"{i}.jpg")
    img = img.filter(ImageFilter.EMBOSS)
    img.save(f"new{i}.jpg")