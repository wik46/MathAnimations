# Trying to learn how Manim Works

# Example Code
from manim import *

class SinAndCosFunctionPlot(Scene):
    def construct(self):
        # 1. Create an Axis
        xmin = 0
        axes = Axes(
            x_range=[xmin, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-xmin, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-xmin, 10.01, 2),
            },
            tips=False,
        )
        # 2. Create Labels for The axis
        axes_labels = axes.get_axis_labels()
        # 3. Create Sine Graph
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        # 4. Creat Cosine Graph
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)
        # 5. Create the sine-graph label
        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        # 6. Create the cosine-graph label
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")
        # 7. Creates that vertical line.
        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        # 8. Labels the vertical line.
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        # This is where we plot everything.
        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)

        # This is where we add the plot to the figure.
        #self.add(plot, labels)
        