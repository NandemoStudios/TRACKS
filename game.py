import Engine
import Engine.Input

game = Engine.StartEngine(1280, 720)

# Defining player variables
PlayerX = 640
PlayerY = 360

move_up = Engine.Input.NewInput('w')
move_down = Engine.Input.NewInput('s')
move_left = Engine.Input.NewInput('a')
move_right = Engine.Input.NewInput('d')

# Game Loop
while game.running:

    if move_up.is_pressed():
        PlayerY -= 2
    elif move_down.is_pressed():
        PlayerY += 2

    if move_left.is_pressed():
        PlayerX -= 2
    elif move_right.is_pressed():
        PlayerX += 2

    game.ClearScreen()
    game.Graphics.draw_circle(PlayerX, PlayerY, 10, color="Blue")
    game.Tick()