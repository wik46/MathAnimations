## Example Mobject: Number Planes

# Manim has a notion of Number Planes. This is different than a coordinate system 
# because it can be used to transform with functions. These number planes are the basis for
# the complex number systems.
from manim import *

class NumberPlaneExample(Scene):
    def construct(self):
        # 1. Creating a very dense plane
        number_plane_dense = NumberPlane(
            x_range=(-10, 10, 0.5), ## Specifies the (left endpoint, right endpoint, width)
            y_range=(-8, 8, 0.5),## Specifies the (left endpoint, right endpoint, width)
            #x_length=10,
            #y_length=2,
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        # 2. Lets create another number plane
        number_plane_sparse = NumberPlane(
            x_range=(-10, 10, 0.5), ## Specifies the (left endpoint, right endpoint, width)
            y_range=(-8, 8, 0.5),## Specifies the (left endpoint, right endpoint, width)
            x_length=5,
            y_length=2,
            background_line_style={
                "stroke_color": GREEN,
                "stroke_width": 1,
                "stroke_opacity": 1
            }
        )
        # 2. Lets create another number plane
        number_plane_prop = NumberPlane(
            x_range=(-1.5, 1.5, 0.5), ## Specifies the (left endpoint, right endpoint, width)
            y_range=(-1.5, 1.5, 0.5),## Specifies the (left endpoint, right endpoint, width)
            x_length=5,
            y_length=2,
            background_line_style={
                "stroke_color": GREEN,
                "stroke_width": 1,
                "stroke_opacity": 1
            }
        )
        self.add(number_plane_dense)
        self.play(
            FadeOut(number_plane_dense),
            run_time=2
        )
        self.play(
            FadeIn(number_plane_dense),
            run_time=2
        )
        self.play(
            FadeOut(number_plane_dense),
            run_time=0.8
        )
        self.play(
            FadeIn(number_plane_sparse),
            run_time=2
        )
        self.play(
            FadeOut(number_plane_sparse),
            run_time=0.8
        )
        self.wait()
                
        self.play(
            FadeIn(number_plane_prop),
            run_time=2
        )
        self.wait()
        # Now we can Work with Number planes
