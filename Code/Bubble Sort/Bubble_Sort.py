from manim import *
import os
import random


class BubbleSortVisual(Scene):
    def construct(self):

        # Erstellung - Titel
        title = Text("Bubble Sort", font_size=40, font="Sans", color="orange").center()

        # Einblenden - Titel
        self.play(Write(title))

        # Erstellung einer Box um Titel
        box = SurroundingRectangle(title, corner_radius=0.2, color=ORANGE)

        # Einblenden - Box + Verschiebung - Box und Title
        self.play(Create(box))
        self.play(box.animate.shift(UP),title.animate.shift(UP))


        # Erstellung - Sub Erklärung 
        sub = Text('Im Folgenden wird die Funktionsweise des Bubble Sort ALG erklärt.\n', color=WHITE, font="Sans", font_size=30)
        sub.next_to(box, DOWN, buff=0.5)

        # Einblenden - Sub Erklärung
        self.play(Write(sub))
        self.wait(1)

        # Ausblenden - Titel, Box und Sub Erklärung
        self.play(FadeOut(title), FadeOut(box), FadeOut(sub))
        self.wait(1)


        # Erstellung - Erklärung Initialisierung der Zahlen (init)
        init = Text("Zuerst betrachten wir neun verschiedene Zahlen, die nicht sortiert sind.",color=WHITE, font="Sans", font_size=30).center()

        # Einblenden - Erklärung Initialisierung der Zahlen (init)
        self.play(Write(init))
        self.wait(1)

        # Ausblenden - Erklärung Initialisierung der Zahlen (init)
        self.play(FadeOut(init))

        # Initialisierung der Zahlen, die sortiert werden sollen
        numbers = [5, 9, 1, 3, 8, 2, 7, 4, 6]

        # Erstellung - Balken und Beschriftungen
        bars = []
        start_x = -len(numbers) * 0.4 / 2  # Startposition 
        for i, num in enumerate(numbers):
            bar = Rectangle(height=num*0.5, width=0.4, fill_color=BLUE, fill_opacity=0.8)
            bar_text = Text(str(num), font_size=24, color=BLACK).move_to(bar.get_center())
            bar.add(bar_text)
            bar.move_to(RIGHT * (i * 0.5 + start_x))  
            bars.append(bar)
        
        # Einlenden - Balken 
        self.play(AnimationGroup(*[FadeIn(bar) for bar in bars], lag_ratio=0.5))
        self.wait(2)
    
        n = len(numbers)
        for i in range(n):
            for j in range(0, n-i-1):
                # Einfärben der Balken, die verglichen werden sollen
                self.play(
                    bars[j].animate.set_fill(GREEN),
                    bars[j+1].animate.set_fill(GREEN),
                    run_time=0.3
                )
                
                # Berechnung derPosition für den Vergleichstext, um ihn unter den Balken zu platzieren
                middle_point = (bars[j].get_center() + bars[j+1].get_center()) / 2
                compare_text = Text("<" if numbers[j] < numbers[j+1] else ">", font_size=28, color=WHITE)
                compare_text.move_to(middle_point + DOWN * (max(bars[j].height, bars[j+1].height) / 2 + 0.75))
                
                #Einbelenden - Vergleichstext 
                self.play(Write(compare_text), run_time=0.3)
                
                if numbers[j] > numbers[j+1]:
                    # Tausch der Zahlen im Array
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    
                    # Tausch der Balken
                    bars[j], bars[j+1] = bars[j+1], bars[j]
                    # Tausch ausführen
                    self.play(Swap(bars[j], bars[j+1]), run_time=0.3)
                
                # Entfernung des Vergleichstext nach dem Tauschvorgang
                self.play(FadeOut(compare_text), run_time=0.3)
                
                # Balken zurückfärben nach dem Vergleich/Tausch
                self.play(
                    bars[j].animate.set_fill(BLUE),
                    bars[j+1].animate.set_fill(BLUE),
                    run_time=0.3
                )

        # Ausblenden - Balken 
        self.play(AnimationGroup(*[FadeOut(bar) for bar in bars]))
        self.wait(3)


        # Erstellung - Zeitkomplexität
        text = Text('Zeitkomplexität', font="Sans", font_size=30, color=WHITE)
        text.center()

        #Einblenden - Zeitkomplexität
        self.play(AddTextLetterByLetter(text, time_per_char = 0.2))

        # Erstellung - Zeitkomplexität Box
        box = SurroundingRectangle(text, corner_radius=0.2, color=ORANGE)
        self.play(Create(box))

        #Einblednden - Zeitkomplexität Box
        self.play(box.animate.shift(UP*3),text.animate.shift(UP*3))
        self.wait(2)

        # Erstellung/Einblenden - Bild
        image1 = ImageMobject('clock.png')
        image1.scale(0.2) 
        image1.move_to(UP*0+LEFT*0)
        self.add(image1)
        self.wait(12)

    	# Erstellung - Best Case und Best Case Box 
        text2 = Text('best case', color=WHITE, font_size=24, font="Sans")
        text2.move_to([-3.5,1.85,0])
        box2 = SurroundingRectangle(text2, corner_radius=0.2, color=ORANGE)

        # Einblenden - Best Case und Best Case Box
        self.add(text2)
        self.add(box2)
        self.play(Create(box2))
        self.wait(2)

        # Erstellung - Best Case Result
        text4 = Text('O(n)', color=RED, font_size=24)
        text4.move_to([3,1.85,0])

        # Einblenden - Best Case Result
        self.add(text4)
        self.wait(8)

        # Erstellung - Average Case und Average Case Box 
        text6 = Text('average case', color=WHITE, font_size=24)
        text6.move_to([-3.3,0.3,0])
        box4 = SurroundingRectangle(text6, corner_radius=0.2, color=ORANGE)

        # Einblenden - Average Case und Average Case Box 
        self.add(text6)
        self.add(box4)
        self.play(Create(box4))
        self.wait(2)

        # Erstellung - Average Case Result
        text7 = Text('O(n*n)', color=RED, font_size=24)
        text7.move_to([3,0.3,0])

        # Einblenden - Average Case Result
        self.add(text7)
        self.wait(8)

        # Erstellung - Worst Case und Worst Case Box 
        text3 = Text('worst case', color=WHITE, font_size=24)
        text3.move_to([-3.4,-1.2,0])
        box3 = SurroundingRectangle(text3, corner_radius=0.2, color=ORANGE)

        # Einblenden - Worst Case und Worst Case Box 
        self.add(text3)
        self.add(box3)
        self.play(Create(box3))
        self.wait(8)

        # Erstellung - Worst Case Result
        text5 = Text('O(n*n)', color=RED, font_size=24)
        text5.move_to([3,-1.2,0])

        # Einblenden - Worst Case Result
        self.add(text5)
        self.wait(5)


        # Ausblenden - Average Case, Average Case Box, Average Case Result, Worst Case, Worst Case Box und Worst Case Result
        # Verschiebung - Bild
        self.play(FadeOut(text6, box4, text7, box3, text5, text3, text4), image1.animate.move_to(DOWN*3+RIGHT*6))
        self.play(text4.animate.move_to([ -3.5, 1, 0]))
        self.wait(1)

        # Erstellung des Rankings - Sterne
        star1 = Star(n=5, outer_radius=0.3, inner_radius=0.2, fill_color=YELLOW_D, 
                    fill_opacity=1, stroke_color=YELLOW, stroke_width=0.5) 
        star2 = Star(n=5, outer_radius=0.3, inner_radius=0.2, fill_color=YELLOW_D, 
                    fill_opacity=1, stroke_color=YELLOW, stroke_width=0.5) 
        star3 = Star(n=5, outer_radius=0.3, inner_radius=0.2, fill_color=YELLOW_D, 
                    fill_opacity=1, stroke_color=YELLOW, stroke_width=0.5) 
        
        # Einblenden der Sterne 1, 2 und 3
        star1.move_to([1.7,0.9,0]) 
        self.play(FadeIn(star1),star1.animate.shift(UP)) 
        star2.move_to([2.4,0.9,0]) 
        self.play(FadeIn(star2),star2.animate.shift(UP))
        star3.move_to([3.1,0.9,0]) 
        self.play(FadeIn(star3),star3.animate.shift(UP))
        self.wait(1)

        # Erstellung/Einblenden - Best Case Erklärung
        TEXT_SPEED = 0.001
        sub = Text('Der Best Case beim Bubble Sort Algorithmus tritt ein, wenn die Liste \nbereits sortiert ist und keine Vertauschungen erforderlich sind.', color=WHITE, font="Sans", font_size=20)
        sub.move_to([0, -0.3, 0])
        self.wait(2)
        bsp_sub = Text('Bsp: 1     2      3      4      5      6      7', color=WHITE, font="Sans", font_size=20)

        # Erstellung/Einblenden - Best Case Beispiel
        bsp_sub.move_to([0,-1.5,0])
        self.play(AddTextLetterByLetter(sub, time_per_char=TEXT_SPEED))
        self.add(bsp_sub)
        self.wait(3)

        # Verschiebung - Average Case und Average Case Box
        text6.move_to([-3.3, 1.84, 0])
        box4.move_to([-3.3, 1.84, 0])

        # Ausblenden - Best Case, Best Case Box, Best Case Result, Best Case Beispiel und Best Case Erklärung
        self.play(FadeOut(sub, text4, text2, box2, bsp_sub), FadeIn(text6, box4))

        # Ausblenden - Stern 3 
        self.play(star3.animate.set_fill(opacity=0))

        # verschieben/Einblenden - Average Case Result
        text7.move_to([-3.5, 1, 0])
        self.play(FadeIn(text7))
        self.wait(1)

        # Erstellung/Einblenden - Average Case Erklärung
        sub2 = Text('Der Average Case reflektiert eine zufällig sortierte Liste mit einer durchschnittlichen\nAnzahl von Vertauschungen.', color=WHITE, font="Sans", font_size=20)
        sub2.move_to([0, -0.3, 0])
        self.wait(3)

        # Erstellung/Einblenden - Average Case Beispiel 
        bsp_sub2 = Text('Bsp: 3    1      5      2      4      7      6', color=WHITE, font="Sans", font_size=20)
        self.play(AddTextLetterByLetter(sub2, time_per_char=TEXT_SPEED))
        bsp_sub2.move_to([0,-1.5,0])
        self.add(bsp_sub2)
        self.wait(4)
        
        # Verschiebung - Worst Case und Worst Case Box
        text3.move_to([-3.4, 1.84, 0])
        box3.move_to([-3.4, 1.84, 0])

        # Ausblenden - Average Case, Average Case Box, Average Case Result, Average Case Beispiel und Average Case Erklärung
        self.play(FadeOut(sub2, text6, box4, text7, bsp_sub2),FadeIn(text3, box3))

        # Ausblenden - Stern 2
        self.play(star2.animate.set_fill(opacity=0))

        # Verschiebung/Einblenden - Worst Case Result 
        text5.move_to([-3.5, 1, 0])
        self.play(FadeIn(text5))
        self.wait(1)

        # Erstellung/Einbleden - Worst Case Erklärung
        sub3 = Text('Der Worst Case tritt ein, wenn die Liste in umgekehrter Reihenfolge sortiert ist, \nwas die maximale Anzahl von Vertauschungen erfordert.', color=WHITE, font="Sans", font_size=20)
        sub3.move_to([0, -0.3, 0])
        self.wait(3)

        # Erstellung/Einbleden - Worst Case Beispiel
        bsp_sub3 = Text('Bsp: 7      6      5      4      3      2      1', color=WHITE, font="Sans", font_size=20)
        self.play(AddTextLetterByLetter(sub3, time_per_char=TEXT_SPEED))
        bsp_sub3.move_to([0,-1.5,0])
        self.add(bsp_sub3)
        self.wait(5)


if __name__ == "__main__":
    os.system(f"manim -pqk {__file__} MainAnim")
    #os.system(f"manim -qh {__file__} MainAnim")
    #os.system(f"manim -pqk {__file__} MainAnim")