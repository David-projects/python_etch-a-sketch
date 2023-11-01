class EtchASketch:
    def __init__(self, sam_the_turtle):
        self.sam = sam_the_turtle

    def move_forward(self):
        self.sam.forward(10)

    def move_backwards(self):
        self.sam.backward(10)

    def turn_right(self):
        self.sam.right(10)

    def turn_left(self):
        self.sam.left(10)

    def clear_screen(self):
        self.sam.home()
        self.sam.clear()
