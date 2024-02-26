from manim import *
import os
import random


class BubbleSortVisual(Scene):
    def construct(self):

        title = Text("Bubble Sort", font_size=40, font="Sans", color="orange").center()
        self.play(Write(title))

        #Box and Sub-Title
        box = SurroundingRectangle(title, corner_radius=0.2, color=ORANGE)
        self.play(Create(box))
        self.play(box.animate.shift(UP),title.animate.shift(UP))
        sub = Text('Im Folgenden wird die Funktionsweise des Bubble Sort ALG erklärt.\n', color=WHITE, font="Sans", font_size=30)
        sub.next_to(box, DOWN, buff=0.5)
        self.play(Write(sub))
        self.wait(1)

        # Change to the next scene
        self.play(FadeOut(title), FadeOut(box), FadeOut(sub))
        self.wait(1)

        init = Text("Zuerst betrachten wir neun verschiedene Zahlen, die nicht sortiert sind.",color=WHITE, font="Sans", font_size=30).center()
        self.play(Write(init))
        self.wait(1)
        self.play(FadeOut(init))

        # Initialisiere die Zahlen, die sortiert werden sollen
        numbers = [5, 9, 1, 3, 8, 2, 7, 4, 6]

        # Erstelle Balken und Beschriftungen
        bars = []
        start_x = -len(numbers) * 0.4 / 2  # Startposition für die Zentralisierung der Balken
        for i, num in enumerate(numbers):
            bar = Rectangle(height=num*0.5, width=0.4, fill_color=BLUE, fill_opacity=0.8)
            bar_text = Text(str(num), font_size=24, color=BLACK).move_to(bar.get_center())
            bar.add(bar_text)
            bar.move_to(RIGHT * (i * 0.5 + start_x))  # Anpassung für die zentrale Positionierung
            bars.append(bar)
        
        # Zeige die initialen Balken
        self.play(AnimationGroup(*[FadeIn(bar) for bar in bars], lag_ratio=0.5))
        self.wait(2)
    
        n = len(numbers)
        for i in range(n):
            for j in range(0, n-i-1):
                # Einfärben der Balken, die verglichen werden
                self.play(
                    bars[j].animate.set_fill(GREEN),
                    bars[j+1].animate.set_fill(GREEN),
                    run_time=0.3
                )
                
                # Berechne die Position für den Vergleichstext, um ihn unter den Balken zu platzieren
                middle_point = (bars[j].get_center() + bars[j+1].get_center()) / 2
                compare_text = Text("<" if numbers[j] < numbers[j+1] else ">", font_size=28, color=WHITE)
                compare_text.move_to(middle_point + DOWN * (max(bars[j].height, bars[j+1].height) / 2 + 0.75))
                
                # Zeige den Vergleichstext an
                self.play(Write(compare_text), run_time=0.3)
                
                if numbers[j] > numbers[j+1]:
                    # Tausche Zahlen im Array
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    
                    # Tausche Balken
                    bars[j], bars[j+1] = bars[j+1], bars[j]
                    # Führe den Tausch aus und lasse den Vergleichstext währenddessen sichtbar
                    self.play(Swap(bars[j], bars[j+1]), run_time=0.3)
                
                # Entferne den Vergleichstext nach dem Tauschvorgang
                self.play(FadeOut(compare_text), run_time=0.3)
                
                # Balken zurückfärben nach dem Vergleich/Tausch
                self.play(
                    bars[j].animate.set_fill(BLUE),
                    bars[j+1].animate.set_fill(BLUE),
                    run_time=0.3
                )


        self.play(AnimationGroup(*[FadeOut(bar) for bar in bars]))
        self.wait(2)


        self.wait(1)
        text = Text('Zeitkomplexität', font="Sans", font_size=30, color=WHITE)
        text.center()
        self.play(AddTextLetterByLetter(text, time_per_char = 0.2))

        box = SurroundingRectangle(text, corner_radius=0.2, color=ORANGE)
        self.play(Create(box))
        self.play(box.animate.shift(UP*3),text.animate.shift(UP*3))
        self.wait(2)

        image1 = ImageMobject('clock.png')
        image1.scale(0.2) 

        image1.move_to(UP*0+LEFT*0)

        self.add(image1)
        self.wait(12)


        text2 = Text('best case', color=WHITE, font_size=24, font="Sans")
        text2.move_to([-3.5,1.85,0])
        box2 = SurroundingRectangle(text2, corner_radius=0.2, color=ORANGE)
        self.add(text2)
        self.add(box2)
        self.play(Create(box2))
        self.wait(2)

        text4 = Text('O(n)', color=RED, font_size=24)
        text4.move_to([3,1.85,0])
        self.add(text4)
        self.wait(8)

        text6 = Text('average case', color=WHITE, font_size=24)
        text6.move_to([-3.3,0.3,0])
        box4 = SurroundingRectangle(text6, corner_radius=0.2, color=ORANGE)
        self.add(text6)
        self.add(box4)
        self.play(Create(box4))
        self.wait(2)

        text7 = Text('O(n*n)', color=RED, font_size=24)
        text7.move_to([3,0.3,0])
        self.add(text7)
        self.wait(8)

        text3 = Text('worst case', color=WHITE, font_size=24)
        text3.move_to([-3.4,-1.2,0])
        box3 = SurroundingRectangle(text3, corner_radius=0.2, color=ORANGE)
        self.add(text3)
        self.add(box3)
        self.play(Create(box3))
        self.wait(8)

        text5 = Text('O(n*n)', color=RED, font_size=24)
        text5.move_to([3,-1.2,0])
        self.add(text5)
        self.wait(5)

        self.play(FadeOut(text6, box4, text7, box3, text5, text3, text4), image1.animate.move_to(DOWN*3+RIGHT*6))
        self.play(text4.animate.move_to([ -3.5, 1, 0]))
        self.wait(1)

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
        self.wait(1)

        TEXT_SPEED = 0.001
        sub = Text('Der Best Case beim Bubble Sort Algorithmus tritt ein, wenn die Liste \nbereits sortiert ist und keine Vertauschungen erforderlich sind.', color=WHITE, font="Sans", font_size=20)
        sub.move_to([0, -0.3, 0])
        self.wait(2)
        bsp_sub = Text('Bsp: 1     2      3      4      5      6      7', color=WHITE, font="Sans", font_size=20)
        bsp_sub.move_to([0,-1.5,0])
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.add(bsp_sub)
        self.wait(3)

        text6.move_to([-3.3, 1.84, 0])
        box4.move_to([-3.3, 1.84, 0])
        self.play(FadeOut(sub, text4, text2, box2, bsp_sub), FadeIn(text6, box4))
        self.play(star3.animate.set_fill(opacity=0))
        text7.move_to([-3.5, 1, 0])
        self.play(FadeIn(text7))
        self.wait(1)

        sub2 = Text('Der Average Case reflektiert eine zufällig sortierte Liste mit einer durchschnittlichen\nAnzahl von Vertauschungen.', color=WHITE, font="Sans", font_size=20)
        sub2.move_to([0, -0.3, 0])
        self.wait(3)
        bsp_sub2 = Text('Bsp: 3    1      5      2      4      7      6', color=WHITE, font="Sans", font_size=20)
        self.play(AddTextLetterByLetter(sub2, time_per_char=TEXT_SPEED))
        bsp_sub2.move_to([0,-1.5,0])
        self.add(bsp_sub2)
        self.wait(4)
        
        text3.move_to([-3.4, 1.84, 0])
        box3.move_to([-3.4, 1.84, 0])
        self.play(FadeOut(sub2, text6, box4, text7, bsp_sub2),FadeIn(text3, box3))
        self.play(star2.animate.set_fill(opacity=0))
        text5.move_to([-3.5, 1, 0])
        self.play(FadeIn(text5))
        self.wait(1)

        sub3 = Text('Der Worst Case tritt ein, wenn die Liste in umgekehrter Reihenfolge sortiert ist, \nwas die maximale Anzahl von Vertauschungen erfordert.', color=WHITE, font="Sans", font_size=20)
        sub3.move_to([0, -0.3, 0])
        self.wait(3)
        bsp_sub3 = Text('Bsp: 7      6      5      4      3      2      1', color=WHITE, font="Sans", font_size=20)
        self.play(AddTextLetterByLetter(sub3, time_per_char=TEXT_SPEED))
        bsp_sub3.move_to([0,-1.5,0])
        self.add(bsp_sub3)
        self.wait(5)


if __name__ == "__main__":
    os.system(f"manim -pqk {__file__} MainAnim")
    #os.system(f"manim -qh {__file__} MainAnim")
    #os.system(f"manim -pqk {__file__} MainAnim")