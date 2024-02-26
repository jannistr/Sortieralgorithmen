# Dieser Python/Manim-Code erstellt eine Szene, welche die Komplexität des Merge Sort Algorithmus darstellt
from manim import *

class complexity(Scene):
    def construct(self):
        self.wait(1)
        text = Text('Zeitkomplexität', color=WHITE)
        text.center()
        self.play(AddTextLetterByLetter(text, time_per_char = 0.2))

        box = SurroundingRectangle(text, corner_radius=0.2, color=GREEN)
        self.play(Create(box))
        self.play(box.animate.shift(UP*3),text.animate.shift(UP*3))
        self.wait(2)

        image1 = ImageMobject('clock.png')
        image1.scale(0.2) 
        image1.move_to(UP*0+LEFT*0)
        self.add(image1)

        # Es wird jeweils für Best Case, Average Case und Worst Case die Zeitkomplexität des Algorithmus beschrieben
        text2 = Text('Best Case', color=WHITE, font_size=24)
        text2.move_to([-3.5,1.85,0])
        box2 = SurroundingRectangle(text2, corner_radius=0.2, color=GREEN)
        self.add(text2)
        self.add(box2)
        self.play(Create(box2))
        self.wait(1)

        text4 = Text('O(n log (n))', color=RED, font_size=24)
        text4.move_to([3,1.85,0])
        self.add(text4)
        self.wait(2)

        text6 = Text('Average Case', color=WHITE, font_size=24)
        text6.move_to([-3.3,0.3,0])
        box4 = SurroundingRectangle(text6, corner_radius=0.2, color=GREEN)
        self.add(text6)
        self.add(box4)
        self.play(Create(box4))
        self.wait(1)

        text7 = Text('O(n log (n))', color=RED, font_size=24)
        text7.move_to([3,0.3,0])
        self.add(text7)
        self.wait(2)

        text3 = Text('Worst Case', color=WHITE, font_size=24)
        text3.move_to([-3.4,-1.2,0])
        box3 = SurroundingRectangle(text3, corner_radius=0.2, color=GREEN)
        self.add(text3)
        self.add(box3)
        self.play(Create(box3))
        self.wait(1)

        text5 = Text('O(n log (n))', color=RED, font_size=24)
        text5.move_to([3,-1.2,0])
        self.add(text5,)
        self.wait(7)

        self.play(FadeOut(text6, box4, text7, box3, text5, text3, text4, text2, text, box2, box), image1.animate.move_to(DOWN*3+RIGHT*6))
        