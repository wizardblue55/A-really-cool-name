import math
import tkinter as tk
from tkinter.font import BOLD
#figuring out importing

root = tk.Tk()
stump = tk.Tk()
print("Hello, World!")
x = 0
sevenSix = ["Oliver", "Eliot"]
#basic varibles, trying things i know from java and c#
while x<100:
    print(x)
    print(sevenSix[x % 2])
    x += 1

def hide(x):
    x.withdraw()
    x.update()

def show(x):
    x.deiconif()
    x.update()

def onClick():
    label.config(text="clicked motherfucker!!!!!!")

print(math.pi)
cunt = int(input())
chatGPT = math.sqrt(cunt)
chatGPT = int(chatGPT)
print(chatGPT)
#trying out the math class I imported earlier



#make a window i hope
#FUCK YEAH BABY IT WORKS


width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.title("Dih Destroyer")
root.geometry(f"{width-10}x{height-10}")
root.config(bg = "lightblue")


label = tk.Label(root, text="Click the button?", font=("Comic Sans", 12))
label.pack(pady=20)
button = tk.Button(
    root,
    text="click me UwU",
    command=onClick,
    bg="gray",
    fg="white",
    font=("papyrus", 10, "bold")
)

button.pack(pady=20)

root.mainloop()