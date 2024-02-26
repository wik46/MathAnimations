# ##########################################################################################################
# Filename: Demo1_VisComplValFunc.py
# Description: This file is intended to visual numerious complex valued functions and see how they transfrom
#               the complex plane, or the open disk
# Usage: Run the following command in your terminal after Manim Community version is installed
#                   manim -pql input_file_name.py output_file_name 
# Manim Community: https://docs.manim.community/en/stable/index.html

from manim import *

# This creates one scene.
class ComplexTransformationScene(Scene):
    def construct(self):
        pass

class Square_Function(ComplexTransformationScene):
    #def construct(self):
    def construct(self):
        # Adding an axis 
        grid =  Axes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
         #   x_length=5,
         #   y_length=5,
            tips=False,
            axis_config={"include_numbers": False},
        )

        # Creating a Number plane that will be transformed. 
        number_plane = ComplexPlane(
        x_range=(-1, 1, 0.5), ## Specifies the (left endpoint, right endpoint, width)
        y_range=(-1, 1, 0.5),## Specifies the (left endpoint, right endpoint, width)
        x_length=10,
        y_length=10,
        background_line_style={
            "stroke_color": TEAL,
            "stroke_width": 1,
            "stroke_opacity": 0.6
        }
        )
        # Creating Dots on the complex plane
        d1 = Dot(number_plane.n2p(-0.5 + 1j), color=YELLOW)
        d2 = Dot(number_plane.n2p(-3 - 2j), color=YELLOW)
        # Creating unit Circle
        circ = Circle()#.scale(1.5)
        circ_stationary = circ.copy()
        # Grouping together the dots, complex plane, and unit circle.
        number_plane_w_dots = VGroup(number_plane, d1, d2, circ)
        
        # Defining a complex valued function that will transform the space.
        def f(z):
            return np.square(z)
            
        # Adding the grid to the scene.
        self.add(grid, circ_stationary)
        
        
        self.play(
            FadeIn(number_plane_w_dots), 
            runtime=5
        )
        self.wait()
        # We add the change speed method to make the scene go slower.
        self.play(
            ChangeSpeed(
                ApplyComplexFunction(f,number_plane_w_dots),
                speedinfo={0.1: 0.1}, # 0.4: 0.1, 0.6: 0.1, 1: 1},
                #rate_func=linear,
            )    
        )


class Mobius_Transforms(ComplexTransformationScene):
    def construct(self):
        def f(z):
            a = 0.9+0*1j # Must be inside the disk
            b = 0+1*1j  # Must be on the cirlce
            return np.divide(3*z+1j,2*z+1)
        circ = Circle(radius=1, color=GREEN)
        circ_ref = circ.copy()

        self.add(circ_ref)
        self.play(
            ApplyComplexFunction(f,circ_ref.copy()),
             run_time=3
        )
        
class Test(ComplexTransformationScene):
    def construct(self):
        grid =  Axes(
            x_range=(-2, 2, 0.5),
            y_range=(-2, 2, 0.5),
            x_length=10,
            y_length=10,
            tips=False,
            axis_config={"include_numbers": True, "unit_size": 1},
        )
        def f(z):
            return np.divide(1+z,1-z)
        def g(z):
            return np.square(z)
        dot_axes = Dot(grid.coords_to_point(1, 1), color=GREEN)
        #circ = Circle(radius=1,color=GREEN)
        circ_1 = Circle.from_three_points(grid.coords_to_point(1, 0), grid.coords_to_point(0, 1), grid.coords_to_point(-1, 0), color=GREEN)
        circ_99 = Circle.from_three_points(grid.coords_to_point(0.99, 0), grid.coords_to_point(0, 0.99), grid.coords_to_point(-0.99, 0), color=RED)
        circ_08 = Circle.from_three_points(grid.coords_to_point(0.8, 0), grid.coords_to_point(0, 0.8), grid.coords_to_point(-0.8, 0), color=RED)
        circ_05 = Circle.from_three_points(grid.coords_to_point(0.5, 0), grid.coords_to_point(0, 0.5), grid.coords_to_point(-0.5, 0), color=BLUE)
        circ_03 = Circle.from_three_points(grid.coords_to_point(0.3, 0), grid.coords_to_point(0, 0.3), grid.coords_to_point(-0.3, 0), color=YELLOW)
        #############################################
        # Printing Diagnostic Info To Kernel
        print("\nOrigin of grid:", grid.coords_to_point(1, 1))
        print("\nLeft: ",LEFT, " and (-1,0)", grid.coords_to_point(-1,0), " and (0,1)", grid.coords_to_point(0,1))
        #############################################
        grid_and_circ = VGroup(grid,circ_1, dot_axes)
        disk = VGroup(circ_99,circ_08,circ_05, circ_03)
        self.add(grid_and_circ)
        self.wait()
        self.play(
            FadeIn(disk, runtime=2)
        )
        # Tranforming
        self.play(
            ChangeSpeed(
                ApplyComplexFunction(f,disk),
                speedinfo={0.1: 0.1}, # 0.4: 0.1, 0.6: 0.1, 1: 1},
                rate_func=linear,
            )   
        )
        self.add(disk)
        
        self.wait()


class Test_W_Cplane(ComplexTransformationScene):
    def construct(self):
        grid =  Axes(
            x_range=(-2, 2, 0.5),
            y_range=(-2, 2, 0.5),
            x_length=10,
            y_length=10,
            tips=False,
            axis_config={"include_numbers": True, "unit_size": 1},
        )
        c_plane =  ComplexPlane(
            x_range=(-2, 2, 0.2),
            y_range=(-2, 2, 0.2),
            x_length=10,
            y_length=10,
        ).move_to(grid.coords_to_point(0, 0))
        def f(z):
            return np.divide(1+z,1-z)
        def g(z):
            return np.square(z)
        dot_axes = Dot(grid.coords_to_point(1, 1), color=GREEN)
        d1 = Dot(grid.coords_to_point(0.2, 0.2), color=GREEN)
        #circ = Circle(radius=1,color=GREEN)
        circ_1 = Circle.from_three_points(grid.coords_to_point(1, 0), grid.coords_to_point(0, 1), grid.coords_to_point(-1, 0), color=GREEN)
        circ_99 = Circle.from_three_points(grid.coords_to_point(0.99, 0), grid.coords_to_point(0, 0.99), grid.coords_to_point(-0.99, 0), color=RED)
        circ_08 = Circle.from_three_points(grid.coords_to_point(0.8, 0), grid.coords_to_point(0, 0.8), grid.coords_to_point(-0.8, 0), color=RED)
        circ_05 = Circle.from_three_points(grid.coords_to_point(0.5, 0), grid.coords_to_point(0, 0.5), grid.coords_to_point(-0.5, 0), color=BLUE)
        circ_03 = Circle.from_three_points(grid.coords_to_point(0.3, 0), grid.coords_to_point(0, 0.3), grid.coords_to_point(-0.3, 0), color=YELLOW)
        #############################################
        # Printing Diagnostic Info To Kernel
        print("\nOrigin of grid:", grid.coords_to_point(1, 1))
        print("\nLeft: ",LEFT, " and (-1,0)", grid.coords_to_point(-1,0), " and (0,1)", grid.coords_to_point(0,1))
        #############################################
        grid_and_circ = VGroup(grid,circ_1, dot_axes,d1)
        disk = VGroup(circ_99,circ_08,circ_05, circ_03)
        self.add(grid_and_circ)
        self.wait()

        
        self.wait()



class ApplyFuncExample(Scene):
    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(
            lambda x: np.exp(x*1j)
        )
        t = ValueTracker(0)
        circ.add_updater(
            lambda x: x.become(circ_ref.copy().apply_complex_function(
                lambda x: np.exp(x+t.get_value()*1j)
            )).set_color(BLUE)
        )
        self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        #self.play(t.animate.set_value(TAU), run_time=3)


class ApplyFuncExampleCustom1(Scene):
    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(
            lambda x: np.square(x)
        )
        t = ValueTracker(0)
        circ.add_updater(
            lambda x: x.become(circ_ref.copy().apply_complex_function(
                lambda x: np.square(x+t.get_value()*1j)
            )).set_color(BLUE)
        )
        self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        #self.play(t.animate.set_value(TAU), run_time=3)

class ApplyFuncExampleCustom2(Scene):
    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(
            lambda x: np.divide(1+x,1-x)
        )
        t = ValueTracker(0)
        circ.add_updater(
            lambda x: x.become(circ_ref.copy().apply_complex_function(
                lambda x: np.divide(1+x+t.get_value()*1j,1-(x+t.get_value()*1j)) 
            )).set_color(BLUE)
        )
        self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        #self.play(t.animate.set_value(TAU), run_time=3)
