# Example: This demonstrates how we position objects

from manim import *

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        # Creating two Square Objects    
        square = Square()  # create a square
        square1 = Square() # create another square
        
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        square1.set_fill(GREEN, opacity=0.8)
        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        square1.next_to(circle, LEFT, buff=0.5) # Adding another square to the left of the circle
        # Playing the Scene
        self.play(Create(circle), Create(square), Create(square1))  # show the shapes on screen
        
        self.play(FadeOut(circle))
        # Let's transform the one square to a circle
        self.play(Transform(square, circle))
        # You can do multiple things at once
        self.play(
            square.animate.rotate(PI/4), Rotate(square1, angle=PI), run_time=2
        )

        # This makde the sqaure go small then big.
        self.play(square1.animate.rotate(PI))
        # The square is fading out
        self.play(FadeOut(square))

        # Lets makes the square go 
        self.play(square1.animate.rotate(PI / 4))  # rotate the square

        # This pauses the scene
        self.wait()