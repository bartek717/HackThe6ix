from PIL import Image
import pytesseract

ingredients = pytesseract.image_to_string(Image.open('testing2.jpeg')) # string of entire picture

new = ingredients.split("\n")

items = []

for item in new:
    if "$" in item and "/" not in item:
        items.append(item)
    
for item in items:
    print(item)   
    
   
   
    