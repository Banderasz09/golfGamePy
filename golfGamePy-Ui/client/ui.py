from display import *

class UI(object):
    def __init__(self):
        Display.add_button("UI.conn()", 430, 410, 420 120, "Play")
        Display.add_button("UI.mymaps()", 430, 550, 420, 120, "My Maps")
        Display.add_button("Game.connect()")

    def main(self):
        Hide_buttons()

        show_button("Ui.conn()")
        show_button("Ui.mymaps()")
        
    def conn(self):
        pass

    def end(self):
        pass

    def license_screen(self):
        pass

