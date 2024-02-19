# Working with latex and Manim
from manim import *

class MovingFrameBox(Scene):
    def construct(self):

        # Create an Example Function
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        #line_label = axes.get_graph_label(
         #   cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        #)

        plot = VGroup( cos_graph, cos_label)
        labels = VGroup(axes,axes_labels) #, line_label)
        # Introducing the plot and labels
        self.add(labels)
        self.wait()
        self.play(FadeIn(plot))
        self.wait()
        self.play(FadeOut(plot,labels))
        

        
        # Hardy Operator Text
        text=MathTex(
            "H(f)(x)=","\\frac{1}{x}\\int\\limits_{0}^{x}f(t)dt"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        #framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        #self.play(
       #     ReplacementTransform(framebox1,framebox2),
       # )
        self.wait()