import sys
from PIL import Image, ImageOps
import os

def main():
    extensions = [".jpg", ".png", ".jpeg"]
    path1 = os.path.splitext(sys.argv[1])
    path2 = os.path.splitext(sys.argv[2])
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if path1[1] not in extensions or path2[1] not in extensions:
        sys.exit("Invalid output")
    if path1[1] != path2[1]:
        sys.exit("Input and output have different extensions")
    shirt_image = shirt(sys.argv[1], sys.argv[2])

def shirt(input, output):
    try:
        shirt = Image.open("shirt.png")
        person = Image.open(input)

        size = shirt.size

        person = ImageOps.fit(person, size)

        shirt = shirt.convert("RGBA")
        person = person.convert("RGB")


        final_image = Image.new("RGB", size)
        final_image.paste(person)
        final_image.paste(shirt, shirt)
        final_image.save(output)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()