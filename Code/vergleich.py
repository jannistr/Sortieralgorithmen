from manim import *
import os

class CreateTableExample(Scene):
    def construct(self):

        # Erstellen Überschrift für den Vergleich    
        überschrift = Text('Vergleich', color=WHITE, font='Sans', font_size=40)
        überschrift.center()
        self.play(AddTextLetterByLetter(überschrift, time_per_char = 0.2))

        boxx = SurroundingRectangle(überschrift, corner_radius=0.2, color=YELLOW)
        self.play(Create(boxx))
        self.play(boxx.animate.shift(UP*3),überschrift.animate.shift(UP*3))

        # Erstellen der Beschreibung für die Bewertungskriterien Typ, Komplexität und Stabilität
        schritt1 = Text('Typ', color=YELLOW, font='Sans', font_size = 20)
        schritt1.move_to([-3.5,1.8,0])
        schritt2 = Text('Komplexität', color=YELLOW, font='Sans', font_size = 20)
        schritt2.move_to([-3.5,0.3,0])
        schritt3 = Text('Stabiliät', color=YELLOW, font='Sans', font_size = 20)
        schritt3.move_to([-3.5,-1.2,0])
        self.play(FadeIn(schritt1, schritt2, schritt3))

        satz = Text('vergleichsbasiert oder nicht vergleichsbasiert?', color=WHITE, font='Sans', font_size = 20)
        satz.move_to([2, 1.85,0])
        satz3 = Text('Worst Case Senario', color=WHITE, font='Sans', font_size = 20)
        satz3.move_to([2, 0.3,0])
        satz4 = Text('Stabile Sortierverfahren haben den Fokus, \ndass die Reihenfolge der Datensätze gleichbleibt, \nderen Sortierschlüssel auch gleich sind', color=WHITE, font='Sans', font_size = 20)
        satz4.move_to([2, -1.2,0])
        self.play(FadeIn(satz))
        self.wait(1)
        self.play(FadeIn(satz3))
        self.wait(1)
        self.play(FadeIn(satz4))
        self.wait(3)
        # Ausblenden der Einführung
        self.play(FadeOut(schritt1, schritt2, schritt3, satz, satz3, satz4))

        # Erstellen der Tabelle für den Vergleich
        table = Table(
            [[" ", " ", " "],
            [" "," ", " "],
            [" "," ", " "]],
            row_labels=[Text("Typ", font_size=20), Text("Komplexität \n(Worst Case)", font_size=20), Text("Stabilität", font_size=20)], # Beschriftung der Zeilen
            col_labels=[Text("Bubble Sort", color=ORANGE, font_size=20), Text("Merge Sort", color=GREEN, font_size=20), Text('Bucket Sort', color=BLUE, font_size=20)], # Beschriftung der Spalten
            include_outer_lines=True)
        table.move_to([0, -1, 0])
        self.play(table.create())
        self.wait(1)
        
        # Ausfüllen der Zellen
        vergleich1 = Text("vergleichsbasiert", color=WHITE, font= 'Sans', font_size=20)
        vergleich2 = Text("vergleichsbasiert", color=WHITE, font= 'Sans', font_size=20)
        vergleich3 = Text("nicht \nvergleichsbasiert", color=WHITE, font= 'Sans', font_size=20)
        vergleich1.move_to([-1.2, -0.4, 0])
        vergleich2.move_to([1.5, -0.4, 0])
        vergleich3.move_to([4, -0.4, 0])
        self.play(FadeIn(vergleich1, vergleich2, vergleich3))
        self.wait(3)

        worstcase1 = Text("O(n*n)", color=WHITE, font= 'Sans', font_size=20)
        worstcase2 = Text("O(n*log(n))", color=WHITE, font= 'Sans', font_size=20)
        worstcase3 = Text("abhänig von Worst \nCase des verwen-\ndeten Algorithmus", color=WHITE, font= 'Sans', font_size=20)
        worstcase1.move_to([-1.2, -1.6, 0])
        worstcase2.move_to([1.5, -1.6, 0])
        worstcase3.move_to([4.2, -1.6, 0])
        self.play(FadeIn(worstcase1, worstcase2, worstcase3))
        self.wait(3)

        stabilität1 = Text("Ja", color=WHITE, font= 'Sans', font_size=20)
        stabilität2 = Text("Ja", color=WHITE, font= 'Sans', font_size=20)
        stabilität3 = Text("Ja", color=WHITE, font= 'Sans', font_size=20)
        stabilität1.move_to([-1.2, -2.8, 0])
        stabilität2.move_to([1.5, -2.8, 0])
        stabilität3.move_to([4, -2.8, 0])
        self.play(FadeIn(stabilität1, stabilität2, stabilität3))
        self.wait(3)

        # Einfügen des Bildes der Eule und Glühbirne
        image1 = ImageMobject('ralf.png')
        image1.scale(0.2) 
        image1.move_to(UP*3+LEFT*6)
        self.play(FadeIn(image1))
        self.wait(2)
        image2 = ImageMobject('die-gluhbirne.png')
        image2.scale(0.2) 
        image2.move_to(UP*3+LEFT*5)
        self.play(FadeIn(image2))
        self.wait(2)

if __name__ == "__main__":
     os.system(f"manim -pql {__file__} MainAnim")