from PIL import Image
import pytesseract

def getReciptData(imageName):
    ingredients = pytesseract.image_to_string(Image.open(imageName)) # string of entire picture
    stripped = ingredients[ 0 : ingredients.lower().index("total")]     # delete  everything after total

    itemize = stripped.split("\n")

    items = []
    total = 0

    def has_numbers(inputString):
        return any(char.isdigit() for char in inputString)

    groupedItemData = []
    total = 0

    for item in itemize:
        if "." in item and "%" not in item:

            groupedItemData.append(item)

            itemParts = item.split()
            for item in itemParts:
                if has_numbers(item) and "." in item and "$" in item:
                    total += float(item[1:])
                
    subtotal = round(total,2)
    total = round(subtotal*1.13,2)
    taxes = round(total - subtotal,2)
    
    return subtotal, total, taxes, groupedItemData

subtotal, total, taxes, groupedItemData = getReciptData("sample.jpg")

print(f"Total value of goods: {subtotal}")
print(f"Total value of goods with taxes: {total}")
print(f"Taxes: {taxes}")
print("Items:")
for item in groupedItemData:
    print(item)