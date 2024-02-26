from manim import *
import os
import random


class OpeningManim(Scene):
    def construct(self):

        # Erstellung - First Titel
        first_title = Text('Sortieralgorithmen', font="Sans", font_size=40, color=WHITE).center()

        # Einblenden - First Titel
        self.play(Write(first_title))
        self.wait(1)


        # Bild hinzufuegen 
        image1 = ImageMobject('Ralf.png')
        image1.scale(0.2) 
        image1.move_to(UP*3 + LEFT*6.5)
        self.add(image1)

        # Bild verschieben
        image2 = ImageMobject('mark.png')
        image2.scale(0.2) 
        image2.move_to(UP*3 + LEFT*5.5)
        self.add(image2)


        # Verwendung von animate für Skalierung und Bewegung
        self.play(first_title.animate.scale(0.5).to_edge(UP + RIGHT))
        self.wait(2)


        # Erstellung - Bubble Sort, Bucket Sort und Merge Sort
        bubble = Text('Bubble Sort', font="Sans", font_size=40, color=WHITE).to_edge(LEFT, buff=0.5)
        bucket = Text('Bucket Sort', font="Sans", font_size=40, color=WHITE).to_edge(RIGHT, buff=0.5)
        merge = Text('Merge Sort', font="Sans", font_size=40, color=WHITE).center()

        # Einblenden - Bubble Sort, Bucket Sort und Merge Sort
        self.play(Write(bubble), Write(bucket),Write(merge))
        self.wait(2)

        # Ausblenden - Bucket Sort und Merge Sort
        self.play(FadeOut(bucket), FadeOut(merge), run_time=1)
        

        # Verschiebung und Skalierung des Bubble Sort  
        self.play(bubble.animate.scale(2).move_to(ORIGIN), run_time=2)

        # Erstellung einer Box um Bubble Sort 
        bubble_box = SurroundingRectangle(bubble, corner_radius=0.2, color=RED)

        # Einblenden - Bubble Box
        self.play(Create(bubble_box))

        # Verschiebung nach oben von Bubble Sort
        self.play(bubble_box.animate.shift(UP),bubble.animate.shift(UP))

        # Erstellung - Bubble Sort Erklärung
        bubble_explanation = Text(
            "Bubble Sort vergleicht wiederholt benachbarte Elemente \nund tauscht sie aus, wenn sie in der falschen Reihenfolge sind.",
        font_size=24, font="Sans", line_spacing=1.5
        ).next_to(bubble, DOWN, buff=0.5)

        # Einblenden - Bubble Sort Erklärung
        self.play(Write(bubble_explanation), run_time=3)
        self.wait(8)


        # Ausblenden- Bubble Sort, Bubble Sort Erklärung und Bubble Box 
        self.play(FadeOut(bubble_explanation), FadeOut(bubble), FadeOut(bubble_box), run_time=1)
        self.wait(1)


        # Einbleden - Merge Sort
        self.play(FadeIn(merge), run_time=1) 

        # Verschiebung und Skalierung von Merge Sort 
        self.play(merge.animate.scale(2).move_to(ORIGIN), run_time=2)

        # Erstellung einer Box um Merge Sort 
        merge_box = SurroundingRectangle(merge, corner_radius=0.2, color=GREEN)

        # Einblenden - Merge Box 
        self.play(Create(merge_box))
    
        # Verschiebung nach oben von Merge Sort
        self.play(merge_box.animate.shift(UP), merge.animate.shift(UP))

        # Erstellung - Merge Sort Erklärung
        merge_explanation = Text(
            "Die grundlegende Idee von Merge Sort besteht darin, das zu sortierende \nArray in kleinere Arrays zu teilen, diese rekursiv zu sortieren und anschließend \ndie sortierten Arrays wieder zu einem einzigen sortierten Array zusammenzuführen.",
            font_size=24, font="Sans", line_spacing=1.5
        ).next_to(merge, DOWN, buff=0.5)

        # Einblenden- Merge Sort Erklärung
        self.play(Write(merge_explanation), run_time=3)
        self.wait(7)
        

        # Ausblenden - Merge Sort, Merge Sort Erklärung und Merge Box
        self.play(FadeOut(merge), FadeOut(merge_box), FadeOut(merge_explanation), run_time=1)
        self.wait(1)


        # Einblenden - Bucket Sort
        self.play(FadeIn(bucket), run_time=1)  

        # Verschiebung und Skalierung von Bucket Sort 
        self.play(bucket.animate.scale(2).move_to(ORIGIN), run_time=2)

        # Erstellung - Bucket Box
        bucket_box = SurroundingRectangle(bucket, corner_radius=0.2, color=BLUE)

        # Einblenden - Bucket Box 
        self.play(Create(bucket_box))

        # Verschiebung nach oben von Bucket Sort 
        self.play(bucket_box.animate.shift(UP), bucket.animate.shift(UP))

        # Erstellung - Bucket Sort Erklärung
        bucket_explanation = Text(
            "Bucket Sort verteilt die Array-Elemente in eine Reihe von Buckets. \nJeder Bucket wird dann einzeln sortiert, durch einen anderen Sortieralgorithmus.",
            font_size=24, font="Sans", line_spacing=1.5
        ).next_to(bucket, DOWN, buff=0.5)

        # Einblenden - Bucket Sort Erklärung
        self.play(Write(bucket_explanation), run_time=3)
        self.wait(7)


        # Ausblenden - Bucket Sort, Bucket Sort Erklärung und Bucket Box
        self.play(FadeOut(bucket), FadeOut(bucket_box), FadeOut(bucket_explanation), run_time=1)
        self.wait(1)


        # Erstellung - Vergleich und Nicht Vergleich
        vergleich = Text("Vergleichsbasierte\nAlgorithmen", line_spacing=1, font="Sans", font_size=40)
        not_vergleich = Text("Nicht Vergleichsbasierte\nAlgorithmen", line_spacing=1,font="Sans", font_size=40)
        not_vergleich.next_to(vergleich, RIGHT, buff=1)
        
        # Einblenden - Vergleich und Nicht Vergleich
        self.play(Write(vergleich), Write(not_vergleich))
        self.wait(4)

        # Ausblenden - Nicht Vergeleich
        self.play(FadeOut(not_vergleich), run_time=1)


        # Skalierung und Verschiebung von Vergleich
        self.play(vergleich.animate.scale(1).move_to(ORIGIN), run_time=2)
        self.wait(1)
        self.play(vergleich.animate.shift(UP))
        self.wait(1)

        # Erstellung - Vergleich Erklärung
        vergleich_explanation = Text(
            "Vergleichsbasierte Algorithmen sortieren Daten, indem sie Paare von Elementen\nvergleichen und auf Basis dieser Vergleiche Entscheidungen treffen.",
            font_size=24, font="Sans", line_spacing=1.5
        ).next_to(vergleich, DOWN, buff=0.5)

        # Einblenden - Vergleich Erklärung
        self.play(Write(vergleich_explanation), run_time=3)
        self.wait(4)

        # Ausblenden - Vergleich Erklärung
        self.play(FadeOut(vergleich_explanation))

        # Erstellung/Einblenden - Bubble Sort und Merge Sort + Bubble Box und Merge Box
        bubble = Text('Bubble Sort', font="Sans", font_size=40, color=WHITE).to_edge(LEFT, buff=0.5)
        bubble.shift(DOWN * 1)
        self.play(Write(bubble))
        bubble_box = SurroundingRectangle(bubble, corner_radius=0.2, color=RED)
        self.play(Create(bubble_box))
        self.wait(2)
        merge = Text('Merge Sort', font="Sans", font_size=40, color=WHITE).to_edge(RIGHT, buff=0.5)
        merge.shift(DOWN * 1)
        self.play(Write(merge))
        merge_box = SurroundingRectangle(merge, corner_radius=0.2, color=GREEN)
        self.play(Create(merge_box))
        self.wait(2)


        # Ausblenden - Vergleich, Bubble Sort, Merge Sort, Bubble Box und Merge Box
        self.play(FadeOut(vergleich), FadeOut(bubble), FadeOut(merge), FadeOut(bubble_box), FadeOut(merge_box), run_time=1)


        # Einblenden - Nicht vergleich
        self.play(FadeIn(not_vergleich,run_time=1))     

        # Skalierung und Verschiebung von Nicht Vergleich 
        self.play(not_vergleich.animate.scale(1).move_to(ORIGIN), run_time=2)
        self.wait(1)
        self.play(not_vergleich.animate.shift(UP))   
        self.wait(1)

        # Erstellung - Nicht Vergleich Erklärung
        not_vergleich_explanation = Text(
            "Nicht-vergleichsbasierte Algorithmen sortieren Daten nicht durch Vergleichen \nvon Elementpaaren, sondern nutzen die Struktur der Daten selbst, \num eine schnelle Sortierung zu erreichen.",
            font_size=24, font="Sans", line_spacing=1.5
        ).next_to(not_vergleich, DOWN, buff=0.5)

        # Einblenden - Nicht Vergleich
        self.play(Write(not_vergleich_explanation), run_time=3)
        self.wait(5)

        # Ausblenden - Nicht Vergleich
        self.play(FadeOut(not_vergleich_explanation))   

        # Erstellung/Einblenden - Bucket Sort + Bucket Box 
        bucket = Text('Bucket Sort', font="Sans", font_size=40, color=WHITE).center()
        bucket.shift(DOWN * 1)
        self.play(Write(bucket))
        bucket_box = SurroundingRectangle(bucket, corner_radius=0.2, color=BLUE)
        self.play(Create(bucket_box))
        self.wait(4)


        # Ausblenden - Not Vergleich, Bucket Sort und Bucket Box
        self.play(FadeOut(not_vergleich), FadeOut(bucket_box), FadeOut(bucket))



if __name__ == "__main__":
    os.system(f"manim -pqk {__file__} MainAnim")
    #os.system(f"manim -pql {__file__} MainAnim")
    #os.system(f"manim -qh {__file__} MainAnim")