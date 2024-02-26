# Dieser Python/Manim-Code erstellt eine Szene, welche eine grobe Einleitung in den Mergesort Algorithmus gibt
from manim import *


class SortFunction(Scene):
    def construct(self):
        # Es wird eine beschreibende Überschrift erstellt
        überschrift = Text('Merge Sort', color=GREEN, font='Sans', font_size=40)
        überschrift.center()
        self.play(AddTextLetterByLetter(überschrift, time_per_char = 0.2))

        boxx = SurroundingRectangle(überschrift, corner_radius=0.2, color=BLUE)
        self.play(Create(boxx))
        self.play(boxx.animate.shift(UP),überschrift.animate.shift(UP))

        sub = Text('Nun wird der Merge-Sort-Algorithmus vorgestellt', color=WHITE, font='Sans', font_size=30)
        self.play(AddTextLetterByLetter(sub, time_per_char = 0.01))
        self.wait(2)
        self.play(FadeOut(sub))

        self.play(boxx.animate.shift(UP*2),überschrift.animate.shift(UP*2))
        ablauf = Text('Ablauf', color=WHITE, font='Sans', font_size=30)
        ablauf.move_to([0, 2.3, 0])
        self.play(FadeIn(ablauf))

        schritt1 = Text('Schritt 1', color=BLUE, font='Sans', font_size = 20)
        schritt1.move_to([-2.5,1.8,0])
        schritt2 = Text('Schritt 2', color=BLUE, font='Sans', font_size = 20)
        schritt2.move_to([-2.5,0.3,0])
        schritt3 = Text('Schritt 3', color=BLUE, font='Sans', font_size = 20)
        schritt3.move_to([-2.5,-1.2,0])
        self.play(FadeIn(schritt1, schritt2, schritt3))

        # Hier werden nun die einzelnen Schritte des Algorithmus skizziert
        satz = Text('Teile das Array in der Mitte', color=WHITE, font='Sans', font_size = 20)
        satz.move_to([2.5, 1.85,0])
        satz3 = Text('Sortiere die Hälften rekursiv', color=WHITE, font='Sans', font_size = 20)
        satz3.move_to([2.5, 0.3,0])
        satz4 = Text('Füge die Hälften zusammen', color=WHITE, font='Sans', font_size = 20)
        satz4.move_to([2.5, -1.2,0])
        self.play(FadeIn(satz))
        self.wait(3)
        self.play(FadeIn(satz3))
        self.wait(3)
        self.play(FadeIn(satz4))
        self.wait(15)

        self.play(FadeOut(überschrift, boxx, schritt1, schritt2, schritt3, satz, satz3, satz4, ablauf))
