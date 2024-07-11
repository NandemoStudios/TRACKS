import requests
from customtkinter import *
import os
import zipfile

set_appearance_mode("Dark")


class Window:

    def __init__(self):

        self.CurrentScreen = "Home"

        self.root = CTk()
        self.root.geometry("1280x720")
        self.root.attributes('-fullscreen', True)
        self.showStartPage()
        self.root.mainloop()

    def StartGame(self):
        print("Starting the game")

    def ClearScreen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def showStartPage(self):
        self.CurrentScreen = "Home"
        self.ClearScreen()
        self.StartButton = CTkButton(self.root, text="Start Game", command=self.StartEngine)
        self.SettingsButton = CTkButton(self.root, text="Settings", command=self.showSettingsPage)
        self.QuitButton = CTkButton(self.root, text="Quit", command=self.quitgame)

        self.StartButton.pack()
        self.SettingsButton.pack()
        self.QuitButton.pack()

    def showSettingsPage(self):
        self.CurrentScreen = "Settings"
        self.ClearScreen()
        self.DarkModeButton = CTkButton(self.root, text="Toggle Dark Mode", command=self.ToggleDarkMode)
        self.BackButton = CTkButton(self.root, text="Go Back", command=self.showStartPage)
        self.DarkModeButton.pack()
        self.BackButton.pack()

    def ToggleDarkMode(self):
        if get_appearance_mode() == "Dark":
            set_appearance_mode("Light")
        else:
            set_appearance_mode("Dark")
        self.RefreshPage()

    def RefreshPage(self):
        match self.CurrentScreen:
            case "Home":
                self.showStartPage()
            case "Settings":
                self.showSettingsPage()
            case _:
                print("An error has occurred, please reload the game")
                quit()

    def quitgame(self):
        self.root.destroy()

    def StartEngine(self):
        if os.path.exists(".\dist\game.exe"):
            os.startfile(".\dist\game.exe")
        else:
            r = requests.get('https://github.com/NandemoStudios/TRACKS/releases/download/testRelease/TRACKS.zip')
            file = open("TRACKS.zip", 'wb')
            file.write(r.content)
            file.close()
            with zipfile.ZipFile("TRACKS.zip", 'r') as zip_ref:
                zip_ref.extractall('./')


startWindow = Window()
