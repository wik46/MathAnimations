## Example Mobject: Number Planes

# Manim has a notion of Number Planes. This is different than a coordinate system 
# because it can be used to transform with functions. These number planes are the basis for
# the complex number systems.
from manim import *

class NumberPlaneExample(Scene):
    def construct(self):

        # Lets create another number plane
        number_plane_prop = NumberPlane(
            x_range=(-1.5, 1.5, 0.5), ## Specifies the (left endpoint, right endpoint, width)
            y_range=(-1.5, 1.5, 0.5),## Specifies the (left endpoint, right endpoint, width)
            x_length=5,
            y_length=5,
            axis_config={"include_numbers": True},
            background_line_style={
                "stroke_color": GREEN,
                "stroke_width": 1,
                "stroke_opacity": 1
            }
        )
        self.add(number_plane_prop)

        self.wait()
        # Now we can Work with Number planes
