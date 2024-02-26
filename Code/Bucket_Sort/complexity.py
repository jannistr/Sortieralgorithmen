from manim import *
import os

class complexity(Scene):
    def construct(self):
        self.wait(1)

        # Erstellen der Szene für die Zeitkomplexität des Bucket Sort
        text = Text('Zeitkomplexität', color=WHITE)
        text.center()
        self.play(AddTextLetterByLetter(text, time_per_char = 0.2))
        box = SurroundingRectangle(text, corner_radius=0.2, color=BLUE)
        self.play(Create(box))
        self.play(box.animate.shift(UP*3),text.animate.shift(UP*3))
        self.wait(2)
        image1 = ImageMobject('clock.png')
        image1.scale(0.2) 
        image1.move_to(UP*0+LEFT*0)
        self.add(image1)

        # Erstellen des Best Case Szenarios Zeitkomplexität
        text2 = Text('Best Case', color=WHITE, font_size=24)
        text2.move_to([-3.5,1.85,0])
        box2 = SurroundingRectangle(text2, corner_radius=0.2, color=BLUE)
        self.add(text2)
        self.add(box2)
        self.play(Create(box2))
        self.wait(1)
        text4 = Text('O(n)', color=RED, font_size=24)
        text4.move_to([3,1.85,0])
        self.add(text4)
        self.wait(2)

        # Erstellen des Average Case Szenarios Zeitkomplexität
        text6 = Text('Average Case', color=WHITE, font_size=24)
        text6.move_to([-3.3,0.3,0])
        box4 = SurroundingRectangle(text6, corner_radius=0.2, color=BLUE)
        self.add(text6)
        self.add(box4)
        self.play(Create(box4))
        self.wait(1)
        text7 = Text('O(n*n)', color=RED, font_size=24)
        text7.move_to([3,0.3,0])
        self.add(text7)
        self.wait(2)

        # Erstellen des Worst Case Szenarios Zeitkomplexität
        text3 = Text('Worst Case', color=WHITE, font_size=24)
        text3.move_to([-3.4,-1.2,0])
        box3 = SurroundingRectangle(text3, corner_radius=0.2, color=BLUE)
        self.add(text3)
        self.add(box3)
        self.play(Create(box3))
        self.wait(1)
        text5 = Text('von O(n) über O(n*n)', color=RED, font_size=24)
        text8 = Text('bis zu O(n log(n))', color=RED, font_size=24)
        text5.move_to([3,-1.2,0])
        text8.move_to([3,-1.5,0])
        self.add(text5, text8)
        self.wait(7)

        # Entfernen der Informationen zu den Zeitkomplexitäten Szenarios
        self.play(FadeOut(text6, box4, text7, box3, text5, text8, text3, text4), image1.animate.move_to(DOWN*3+RIGHT*6))
        self.play(text4.animate.move_to([ -3.5, 1, 0]))
        self.wait(1)

        # Erstellen von drei Sternen für worst case bis best case Szenario
        star1 = Star(n=5, outer_radius=0.3, inner_radius=0.2, fill_color=YELLOW_D, 
                    fill_opacity=1, stroke_color=YELLOW, stroke_width=0.5) 
        star2 = Star(n=5, outer_radius=0.3, inner_radius=0.2, fill_color=YELLOW_D, 
                    fill_opacity=1, stroke_color=YELLOW, stroke_width=0.5) 
        star3 = Star(n=5, outer_radius=0.3, inner_radius=0.2, fill_color=YELLOW_D, 
                    fill_opacity=1, stroke_color=YELLOW, stroke_width=0.5) 
        
        star1.move_to([1.7,0.9,0]) 
        self.play(FadeIn(star1),star1.animate.shift(UP)) 
        star2.move_to([2.4,0.9,0]) 
        self.play(FadeIn(star2),star2.animate.shift(UP))
        star3.move_to([3.1,0.9,0]) 
        self.play(FadeIn(star3),star3.animate.shift(UP))
        self.wait(2)

        # Informationen zu Best Case Szenario
        TEXT_SPEED = 0.001
        sub = Text('Der Best Case tritt ein, wenn die Elemente gleichmäßig \nim Eimer verteilt sind und sich in jedem Eimer die \ngleiche Anzahl von Elementen befindet.', color=WHITE, font="Sans", font_size=20)
        sub.move_to([0, -0.3, 0])
        self.wait(1)
        bsp_sub = Text('Bsp: 10     20      30      40      50      60      70', color=WHITE, font="Sans", font_size=20)
        bsp_sub.move_to([0,-1.5,0])
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.add(bsp_sub)
        self.wait(5)

        # Entfernen der Informationen zum Best Case Szenario, Vorbereitung Objektplazierungen Average Case
        text6.move_to([-3.3, 1.84, 0])
        box4.move_to([-3.3, 1.84, 0])
        self.play(FadeOut(sub, text4, text2, box2, bsp_sub), FadeIn(text6, box4))
        self.play(star3.animate.set_fill(opacity=0))
        text7.move_to([-3.5, 1, 0])
        self.play(FadeIn(text7))

        # Erstellern der Informationen zu Average Case Szenario
        sub2 = Text('Der Average Case tritt ein, wenn die Elemente gleichmäßig zufällig verteilt sind', color=WHITE, font="Sans", font_size=20)
        sub2.move_to([0, -0.3, 0])
        self.wait(1)
        bsp_sub2 = Text('Bsp: 30    10      50      20      40      70      60', color=WHITE, font="Sans", font_size=20)
        self.play(AddTextLetterByLetter(sub2, time_per_char=TEXT_SPEED))
        bsp_sub2.move_to([0,-1.5,0])
        self.add(bsp_sub2)
        self.wait(5)
        
        # Entfernen der Informationen zum Average Case Szenario, Vorbereitung Objektplazierungen Worst Case
        text3.move_to([-3.4, 1.84, 0])
        box3.move_to([-3.4, 1.84, 0])
        self.play(FadeOut(sub2, text6, box4, text7, bsp_sub2),FadeIn(text3, box3))
        self.play(star2.animate.set_fill(opacity=0))
        text5.move_to([-3.5, 1, 0])
        text8.move_to([-3.5, 0.7, 0])
        self.play(FadeIn(text5, text8))

        # Erstellern der Informationen zu Average Case Szenario
        sub3 = Text('Der Worst Case tritt ein, wenn sich alle Elemente in einem Bucket befinden. \nDie Leistung entspricht der des Algorithmus, der die Bereiche einzeln sortiert.', color=WHITE, font="Sans", font_size=20)
        sub3.move_to([0, -0.3, 0])
        self.play(AddTextLetterByLetter(sub3, time_per_char=TEXT_SPEED))
        self.wait(12)

if __name__ == "__main__":
    #  os.system(f"manim -pql {__file__} MainAnim")
    os.system(f"manim -pqk {__file__} MainAnim")