from Engine import *
import threading

class Game:

    def __init__(self):
        print("Game Script Loaded")

    def StartGame(self):
        self.Engine = StartEngine(1280, 720)
        self.GameThread = threading.Thread(target=self.GameLoop)
        self.GameThread.start()

    def GameLoop(self):
        while self.Engine.running:
            self.Engine.ClearScreen()
            self.Engine.Graphics.draw_circle(640, 360, 10)
            self.Engine.Tick()