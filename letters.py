import sys
import pyfiglet

figlet=pyfiglet.Figlet()




if sys.argv[1] == "-f" or sys.argv[1] == "--font":
    figlet.setFont(font = sys.argv[2])
else:
    print("Invalid usage")
    sys.exit()

text=input("text: ")
print(figlet.renderText(text))

