# This example show how we can modify the speed of the animations.
# Taken from: https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed
from manim import *

class SpeedModifierUpdaterExample2(Scene):
    def construct(self):
        a = Dot().shift(LEFT * 4)
        self.add(a)

        ChangeSpeed.add_updater(a, lambda x, dt: x.shift(RIGHT * 4 * dt))
        self.wait()
        self.play(
            ChangeSpeed(
                Wait(),
                speedinfo={1: 0},
                affects_speed_updaters=True,
            )
        )