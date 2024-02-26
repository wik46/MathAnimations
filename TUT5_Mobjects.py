# The purpose of this file is to visualize different complex variable functions
# using the community version of manim.

from manim import *

def f(z):
    return z**2

class ComplexPlaneExample(Scene):
    def construct(self):
        # Mobject: Creating Complex Plane that will stay fixed in the Background
        fixed_plane = ComplexPlane().add_coordinates()
        # Creating a Plane that will be transformed by complex valued functions.
        transf_plane = ComplexPlane()
        # Add the plane tot the scene
        self.add(fixed_plane)
        # Create points
        d1 = Dot(fixed_plane.n2p(2 + 1j), color=YELLOW)
        d2 = Dot(fixed_plane.n2p(-3 - 2j), color=YELLOW)
        # Create labels
        label1 = MathTex("2+i").next_to(d1, UR, 0.1)
        label2 = MathTex("-3-2i").next_to(d2, UR, 0.1)
        # Add labels to the scene
        self.add(
            d1,
            label1,
            d2,
            label2,
        )
        matrix = [[1,1],[1,0]]
        #Now we can do stuff the Mobject
        self.play(FadeIn(transf_plane))
        self.wait()
        self.play(ApplyComplexFunction(f,transf_plane))
        #self.play(ApplyMatrix(matrix, plane))