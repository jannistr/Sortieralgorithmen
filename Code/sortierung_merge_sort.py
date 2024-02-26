# Dieser Python/Manim-Code erstellt eine Szene, welche den Sortierungsalgorithmus näher veranschaulicht. 

from manim import *

class BalkenDiagramm(Scene):
    def construct(self):
        # Es werden 8 Balken mit unterschiedlichen Höhen erstellt, die aktuell noch unsortiert vorliegen
        balken_hoehen = [2.5, 1.5, 3, 2, 4, 1, 1.5, 3.5]
        balken = []
        
        # Diese Balken werden nun auf dem Bildschirm sichtbar gemacht und gruppiert
        for i, hoehe in enumerate(balken_hoehen):
            bar = Rectangle(width=0.4, height=hoehe, fill_color=BLUE, fill_opacity=1, stroke_width=1)
            bar.set_bottom(0)
            bar.move_to(i * 0.5 * RIGHT)
            balken.append(bar)
        balken_gruppe = VGroup(*balken)
        balken_gruppe.arrange(RIGHT, buff=0.1, aligned_edge=DOWN).to_edge(DOWN)
        self.play(AnimationGroup(*[Create(balken) for balken in balken_gruppe], lag_ratio=0.1))
        self.wait(6)

        # Nun läuft der Algorithmus Schritt für Schritt ab und es gibt jeweils einen Text am oberen Bildschirmrand, der bschreibt, was genau passiert.
        # Es finden ebenfalls Visualisierungen passend zu dem jeweilligen Schritt statt (z.B. dass die entsprechenden Balken rot markiert werden o. ä.)
        teilung_nachricht = Text("Datenmenge wird in zwei Hälften aufgeteilt", font_size=24)
        teilung_nachricht.to_edge(UP)
        self.play(Write(teilung_nachricht))        
        # Färbe die linken 4 Balken rot ein
        self.play(*[balken.animate.set_color(RED) for balken in balken_gruppe[:4]], run_time=1)
        self.wait(4)

        weitere_teilung_nachricht = Text("Diese ebenfalls in Hälften", font_size=24)
        weitere_teilung_nachricht.next_to(teilung_nachricht, DOWN)
        self.play(Write(weitere_teilung_nachricht))
        
        # Färbe die ersten beiden Balken grün ein
        self.play(balken_gruppe[0].animate.set_color(GREEN), balken_gruppe[1].animate.set_color(GREEN), run_time=1)
        self.wait(8)

        vergleich_nachricht = Text("Sortiere Elemente der ersten Teilmenge", font_size=24)
        vergleich_nachricht.next_to(weitere_teilung_nachricht, DOWN)
        self.play(Write(vergleich_nachricht))
        self.wait(20)
        
        # Ab hier beginnt der eigentliche Algorithmus, es wird nun bei den ersten beiden Balken überprüft, ob diese getauscht werden müssen
        if balken_hoehen[0] > balken_hoehen[1]:
            untere_pos1 = balken_gruppe[0].get_bottom()
            untere_pos2 = balken_gruppe[1].get_bottom()
            self.play(
                balken_gruppe[0].animate.move_to(untere_pos2 + UP * balken_gruppe[0].height / 2),
                balken_gruppe[1].animate.move_to(untere_pos1 + UP * balken_gruppe[1].height / 2),
                run_time=1
            )
            balken[0], balken[1] = balken[1], balken[0]
            balken_gruppe[0], balken_gruppe[1] = balken_gruppe[1], balken_gruppe[0]

        self.wait(2)


        # Das gleiche geschieht nun mit der zweiten Teilmenge:
        vergleich_nachricht2 = Text("Sortiere Elemente der zweiten Teilmenge", font_size=24)
        vergleich_nachricht2.next_to(vergleich_nachricht, DOWN)
        self.play(Write(vergleich_nachricht2))
        self.wait(10)

        if balken_hoehen[2] > balken_hoehen[3]:
            untere_pos1 = balken_gruppe[2].get_bottom()
            untere_pos2 = balken_gruppe[3].get_bottom()
            self.play(
                balken_gruppe[2].animate.move_to(untere_pos2 + UP * balken_gruppe[2].height / 2),
                balken_gruppe[3].animate.move_to(untere_pos1 + UP * balken_gruppe[3].height / 2),
                run_time=1
            )
            balken[2], balken[2] = balken[3], balken[2]
            balken_gruppe[2], balken_gruppe[3] = balken_gruppe[3], balken_gruppe[2]


        # Nun kann die komplette erste Hälfte sortiert werden
        ersteH_nachricht = Text("Sortiere erste Hälfte", font_size=24)
        ersteH_nachricht.next_to(vergleich_nachricht2, DOWN)
        self.play(Write(ersteH_nachricht))
        untere_pos1 = balken_gruppe[1].get_bottom()
        untere_pos2 = balken_gruppe[2].get_bottom()
        self.play(
            balken_gruppe[1].animate.move_to(untere_pos2 + UP * balken_gruppe[1].height / 2),
            balken_gruppe[2].animate.move_to(untere_pos1 + UP * balken_gruppe[2].height / 2),
            run_time=1
        )
        balken[1], balken[2] = balken[2], balken[1]
        balken_gruppe[1], balken_gruppe[2] = balken_gruppe[2], balken_gruppe[1]
      
        self.wait(1)
        self.play(
            FadeOut(teilung_nachricht),
            FadeOut(weitere_teilung_nachricht),
            FadeOut(vergleich_nachricht),
            FadeOut(vergleich_nachricht2),
            FadeOut(ersteH_nachricht)            
            )
        
        fertigH1 = Text("Erste Hälfte ist fertig sortiert", font_size=24)
        fertigH1.to_edge(UP)
        self.play(Write(fertigH1))
        self.wait(1)
        self.play(*[balken.animate.set_color(GREY) for balken in balken_gruppe[:4]], run_time=1)


        # Ende der Sortierung der ersten Hälfte, nun wird das gleiche mit der zweiten Hälfte wiederholt
        self.play(*[balken.animate.set_color(RED) for balken in balken_gruppe[4:8]], run_time=1)
        self.wait(1)
        teilung_nachricht = Text("Gleicher Ablauf wie bei der ersten Hälfte", font_size=24)
        teilung_nachricht.next_to(fertigH1, DOWN)
        self.play(Write(teilung_nachricht))

        if balken_hoehen[4] > balken_hoehen[5]:
            untere_pos1 = balken_gruppe[4].get_bottom()
            untere_pos2 = balken_gruppe[5].get_bottom()
            self.play(
                balken_gruppe[4].animate.move_to(untere_pos2 + UP * balken_gruppe[4].height / 2),
                balken_gruppe[5].animate.move_to(untere_pos1 + UP * balken_gruppe[5].height / 2),
                run_time=1
            )
            balken[4], balken[5] = balken[5], balken[4]
            balken_gruppe[4], balken_gruppe[5] = balken_gruppe[5], balken_gruppe[4]
        
        if balken_hoehen[6] > balken_hoehen[7]:
            untere_pos1 = balken_gruppe[6].get_bottom()
            untere_pos2 = balken_gruppe[7].get_bottom()
            self.play(
                balken_gruppe[6].animate.move_to(untere_pos2 + UP * balken_gruppe[6].height / 2),
                balken_gruppe[7].animate.move_to(untere_pos1 + UP * balken_gruppe[7].height / 2),
                run_time=1
            )
            balken[6], balken[7] = balken[6], balken[7]
            balken_gruppe[6], balken_gruppe[7] = balken_gruppe[6], balken_gruppe[7]

        # 5 und 6 tauschen
        untere_pos1 = balken_gruppe[5].get_bottom()
        untere_pos2 = balken_gruppe[6].get_bottom()
        self.play(
            balken_gruppe[5].animate.move_to(untere_pos2 + UP * balken_gruppe[5].height / 2),
            balken_gruppe[6].animate.move_to(untere_pos1 + UP * balken_gruppe[6].height / 2),
            run_time=1
        )
        balken[5], balken[6] = balken[6], balken[5]
        balken_gruppe[5], balken_gruppe[6] = balken_gruppe[6], balken_gruppe[5]
        self.wait(1)
        # 6 und 7 tauschen
        untere_pos1 = balken_gruppe[6].get_bottom()
        untere_pos2 = balken_gruppe[7].get_bottom()
        self.play(
            balken_gruppe[6].animate.move_to(untere_pos2 + UP * balken_gruppe[6].height / 2),
            balken_gruppe[7].animate.move_to(untere_pos1 + UP * balken_gruppe[7].height / 2),
            run_time=1
        )
        balken[6], balken[7] = balken[7], balken[6]
        balken_gruppe[6], balken_gruppe[7] = balken_gruppe[7], balken_gruppe[6]

        self.wait(1)

        self.play(*[balken.animate.set_color(GREY) for balken in balken_gruppe[4:8]], run_time=1)
        self.wait(3)
        self.play(
            FadeOut(fertigH1),
            FadeOut(teilung_nachricht),
        )

    # Visualisierung der Zusammenführung beider Hälften
        hZusammen = Text("Die beiden Hälften zusammenführen", font_size=24)
        hZusammen.to_edge(UP)
        self.play(Write(hZusammen))
        ziel_position = ORIGIN + LEFT * 2
        aktuelle_position_rechtester_balken = balken_gruppe[-1].get_center()
        verschiebung = ziel_position - aktuelle_position_rechtester_balken
        self.play(balken_gruppe.animate.shift(verschiebung))
        verschiebungs_distanz = RIGHT * 4
        balken_obj = balken_gruppe[4]
        
        self.play(balken_obj.animate.shift(verschiebungs_distanz).set_color(GREEN))

        balken_0 = balken_gruppe[0]
        balken_1 = balken_gruppe[1]
        balken_2 = balken_gruppe[2]
        balken_3 = balken_gruppe[3]
        balken_4 = balken_gruppe[4]
        balken_5 = balken_gruppe[5]
        balken_6 = balken_gruppe[6]
        balken_7 = balken_gruppe[7]

        verschiebung_nach_rechts1 = balken_4.get_center()[0] + balken_4.width + 0.1 - balken_5.get_center()[0]
        verschiebung_nach_rechts2 = balken_4.get_center()[0] + 2*(balken_4.width + 0.1) - balken_0.get_center()[0]
        verschiebung_nach_rechts3 = balken_4.get_center()[0] + 3*(balken_4.width + 0.1) - balken_1.get_center()[0]
        verschiebung_nach_rechts4 = balken_4.get_center()[0] + 4*(balken_4.width + 0.1) - balken_2.get_center()[0]
        verschiebung_nach_rechts5 = balken_4.get_center()[0] + 5*(balken_4.width + 0.1) - balken_3.get_center()[0]
        verschiebung_nach_rechts6 = balken_4.get_center()[0] + 6*(balken_4.width + 0.1) - balken_6.get_center()[0]
        verschiebung_nach_rechts7 = balken_4.get_center()[0] + 7*(balken_4.width + 0.1) - balken_7.get_center()[0]

        # Verschiebe Balken 5 nach rechts neben Balken 4
        self.play(balken_5.animate.shift(RIGHT * verschiebung_nach_rechts1).set_color(GREEN))
        self.wait(0.5)
        self.play(balken_0.animate.shift(RIGHT * verschiebung_nach_rechts2).set_color(GREEN))
        self.wait(0.5)
        self.play(balken_1.animate.shift(RIGHT * verschiebung_nach_rechts3).set_color(GREEN))
        self.wait(0.5)
        self.play(balken_2.animate.shift(RIGHT * verschiebung_nach_rechts4).set_color(GREEN))
        self.wait(0.5)
        self.play(balken_3.animate.shift(RIGHT * verschiebung_nach_rechts5).set_color(GREEN))
        self.wait(0.5)
        self.play(balken_6.animate.shift(RIGHT * verschiebung_nach_rechts6).set_color(GREEN))
        self.wait(0.5)
        self.play(balken_7.animate.shift(RIGHT * verschiebung_nach_rechts7).set_color(GREEN))
        self.wait(0.5)
        
        self.wait(10)



        self.play(
            FadeOut(balken_gruppe),
            FadeOut(hZusammen)
        )

