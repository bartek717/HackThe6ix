from PIL import Image
import pytesseract

ingredients = pytesseract.image_to_string(Image.open('sample.jpg')) # string of entire picture

new = ingredients.split("\n")

items = []
total = 0

for item in new:
    if "total" in item.lower():
        break

    if "." in item and "/" not in item:
        items.append(item)
        price = float(item.split(" ")[-1])
        total += price

print("Items:")
for item in items:
    print(item)

print(f"Total: {total}")
print(f"Total w/ Ontario Tax: {total*1.13}")