from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

# def random_font(text):
#     fonts = figlet.getFonts()
#     font_name = fonts[0]
#     figlet.setFont(font = font_name)
#     print(figlet.renderText(text))


# def specific_font(text, font_name):
#     fonts = figlet.getFonts()
#     if font_name not in fonts:
#         print("Ivalid usage")
#         sys.exit(1)
#     figlet.setFont(font = font_name)
#     print(figlet.renderText(text))


if len(sys.argv) == 1:
    has_font = False
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    has_font = True
else:
    print("Ivalid usage")
    sys.exit(1)

fonts = figlet.getFonts()

if has_font == True:
    if sys.argv[2] in fonts:
        figlet.setFont(font = sys.argv[2])
    else:
        print("Ivalid usage")
        sys.exit(1)
else:
    figlet.setFont(font = random.choice(fonts))

text = input("Input: ")

print(f"Output: \n{figlet.renderText(text)}")