import PIL.Image as pillow
import PIL.ImageFilter as ImageFilter
img = pillow.open("C:\\Users\\HP\\Downloads\\The Rookies.png")
print(img)
print(img.size)
print(img.format)
print(img.mode)

filtered_img = img.filter(ImageFilter.BoxBlur(10))
filtered_img.save("blue.png","png")

convert_img = img.convert("L")
convert_img.save('gray.png','png')