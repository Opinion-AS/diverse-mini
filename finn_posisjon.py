from pynput import mouse
from pynput.mouse import Listener
import keyboard

file = open("pekerkoordinater.txt", "w")

def on_click(x, y, button, pressed):
    file.write(f"{x}, {y}, {pressed}\n")
    return True

listener = mouse.Listener(on_click=on_click)
listener.start()

# Stopper skriptet når man trykker Esc
while True:
    if keyboard.is_pressed("Esc"):
        listener.stop()
        file.close()
        break
