# Basic Manim Example 
# To use this code run: manim -pql file_name.py file_name
# Example 1:
from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        
        # show the circle on screen
        self.play(Create(circle))  