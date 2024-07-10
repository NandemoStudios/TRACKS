from customtkinter import *

import Engine
import game

set_appearance_mode("Dark")


class Window:

    def __init__(self):

        self.CurrentScreen = "Home"

        self.Game = game.Game()

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
        self.QuitButton = CTkButton(self.root, text="Quit", command=quit)

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

    def StartEngine(self):
        self.Game.StartGame()
        self.root.destroy()


startWindow = Window()
