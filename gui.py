import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random

# WINDOW SETUP
window = tk.Tk()
window.title("PCSS Project - Lukas")
window.geometry("1200x700")

playerCards, shopCards, boardArray, shopArray = [], [], [["", "", "", "", ""], ["", "", "", "", "", "", "", "", "", ""]],["","","","",""]

# LOADING IMAGES
bg1 = Image.open("Assets/backgroundBoard3.jpg")
bgPT = ImageTk.PhotoImage(bg1)
backgroundL = Label(image=bgPT)

textBut = Image.open("Assets/testButtonTexture.jpg")
textButPT = ImageTk.PhotoImage(textBut)

CDviking1 = Image.open("Assets/viking1low.jpg")
CDviking1PT = ImageTk.PhotoImage(CDviking1)

SPviking1 = Image.open("Assets/viking1shop.jpg")
SPviking1PT = ImageTk.PhotoImage(SPviking1)

CDroman1 = Image.open("Assets/roman1lowUI.jpg")
CDroman1PT = ImageTk.PhotoImage(CDroman1)

SProman1 = Image.open("Assets/roman1shop.jpg")
SProman1PT = ImageTk.PhotoImage(SProman1)

CDchinese1 = Image.open("Assets/chinese1lowUI.jpg")
CDchinese1PT = ImageTk.PhotoImage(CDchinese1)

SPchinese1 = Image.open("Assets/chinese1shop.jpg")
SPchinese1PT = ImageTk.PhotoImage(SPchinese1)

CDunknown = Image.open("Assets/unknown1low.jpg")
CDunknownPT = ImageTk.PhotoImage(CDunknown)

runCheck = False


def shopBuy(shopNumber):
    if shopArray[shopNumber]==0:
        for i in range(5):
            if (boardArray[1][i + 5] == ""):
                playerCards[i + 5].configure(image=CDviking1PT)
                boardArray[1][i + 5] = "Thor"
                return ()
    if shopArray[shopNumber]==1:
        for i in range(5):
            if (boardArray[1][i + 5] == ""):
                playerCards[i + 5].configure(image=CDroman1PT)
                boardArray[1][i + 5] = "Roman"
                return ()
    if shopArray[shopNumber]==2:
        for i in range(5):
            if (boardArray[1][i + 5] == ""):
                playerCards[i + 5].configure(image=CDchinese1PT)
                boardArray[1][i + 5] = "Chinese"
                return ()
    print("Shop: " + str(shopNumber))

def shopRandom():
    for i in range(5):
        rand = random.randint(0, 2)
        if rand == 0:
            shopCards[i].configure(image=SPviking1PT)
            shopArray[i]=0
        if rand == 1:
            shopCards[i].configure(image=SProman1PT)
            shopArray[i]=1
        if rand == 2:
            shopCards[i].configure(image=SPchinese1PT)
            shopArray[i]=2
        print("Shop numbers: "+ str(rand))


def cardSelect(PlayerSelect, cardNumber):
    boardArray[PlayerSelect - 1][cardNumber] = ""
    playerCards[cardNumber].configure(image=CDunknownPT)
    print("Card: " + str(cardNumber) + " Player: " + str(PlayerSelect))
    print(boardArray[0][0] + " " + boardArray[0][1] + " " + boardArray[0][2] + " " + boardArray[0][3] + " " +
          boardArray[0][4])
    print(boardArray[1][5] + " " + boardArray[1][6] + " " + boardArray[1][7] + " " + boardArray[1][8] + " " +
          boardArray[1][9])


class displayGUI():
    # GUI Set-up made with help from: https://www.geeksforgeeks.org/python-gui-tkinter/
    def __init__(self, runcheck: bool):
        runCheck = runcheck

        for i in range(10):
            if i < 5:
                playerCards[i].place(relx=1, x=-80 - (i * 120), y=100, anchor=NE)
            if i >= 5:
                playerCards[i].place(relx=1, x=-80 - ((i - 5) * 120), y=350, anchor=NE)

        for i in range(5):
            shopCards[i].place(relx=1, x=-1150, y=110 + (i * 95), anchor=NW)

        sceneUpdateButton = tk.Button(window, width=250, height=50, image=textButPT, compound=LEFT, command=shopRandom)
        sceneUpdateButton.place(relx=1, x=-500, y=620, anchor=NE)

        backgroundL.grid(row=0, column=0)
        window.mainloop()
        # threading.Thread.__init__(target=w.mainloop()).start

    def setup(self):
        for i in range(10):
            stringHolder = "cardHolder" + str(i)

            if i < 5:
                stringHolder = tk.Button(window, width=105, height=185, image=CDunknownPT, compound=LEFT,
                                         command=lambda holder=i: cardSelect(1, holder))
                playerCards.append(stringHolder)
            else:
                stringHolder = tk.Button(window, width=105, height=185, image=CDunknownPT, compound=LEFT,
                                         command=lambda holder=i: cardSelect(2, holder))
                playerCards.append(stringHolder)

        for i in range(5):
            stringHolder = "ShopCard" + str(i)
            stringHolder = tk.Button(window, width=290, height=95, image=SPviking1PT,
                                     command=lambda holder=i: shopBuy(holder))
            shopCards.append(stringHolder)
        shopRandom()
