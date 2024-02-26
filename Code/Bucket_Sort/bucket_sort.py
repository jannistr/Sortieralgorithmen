from manim import *
import os


class SortFunction(Scene):
    def construct(self):

        # Einleitung in Bucket Sort Algorithmus Vorstellung            
        überschrift = Text('Bucket Sort', color=BLUE, font='Sans', font_size=40)
        überschrift.center()
        self.play(AddTextLetterByLetter(überschrift, time_per_char = 0.2))

        boxx = SurroundingRectangle(überschrift, corner_radius=0.2, color=BLUE)
        self.play(Create(boxx))
        self.play(boxx.animate.shift(UP),überschrift.animate.shift(UP))

        sub = Text('Als Letztes wird der Bucket Sort vorgestellt!', color=WHITE, font='Sans', font_size=30)
        self.play(AddTextLetterByLetter(sub, time_per_char = 0.01))
        self.wait(2)
        self.play(FadeOut(sub))

        # Beschreibung des Algorithmus, Schritte vorgestellt 
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

        satz = Text('Buckets werden erstellt', color=WHITE, font='Sans', font_size = 20)
        satz.move_to([2.5, 1.85,0])
        satz2 = Text('Liste wird verteilt', color=WHITE, font='Sans', font_size = 20)
        satz2.move_to([2.5, 1.6,0])
        satz3 = Text('Buckets werden sortiert', color=WHITE, font='Sans', font_size = 20)
        satz3.move_to([2.5, 0.3,0])
        satz4 = Text('Array wird wieder verknüpft', color=WHITE, font='Sans', font_size = 20)
        satz4.move_to([2.5, -1.2,0])
        self.play(FadeIn(satz))
        self.wait(2)
        self.play(FadeIn(satz2))
        self.wait(2)
        self.play(FadeIn(satz3))
        self.wait(2)
        self.play(FadeIn(satz4))
        self.wait(5)
        # Alle Objekte aus Szene entfernen
        self.play(FadeOut(überschrift, boxx, schritt1, schritt2, schritt3, satz, satz2, satz3, satz4, ablauf))

        # Funktion zum Erstellen der Boxen mit Zahlen, die sortiert werden sollen 
        def square_text_box(number1, square_color, text_color): # Angeben der Zahl, Quadratfarbe und Textfarbe
            square = Square(side_length=0.9)    # Größe Quadrat
            square.set_stroke(color=square_color)   # Farbe des Quadrats 
            text = MarkupText(number1, color=text_color)    # Farbe der Zahl
            text.scale(0.6) # Textgröße
            squ_text = VGroup()
            squ_text.add(square, text)  # Zusammenfügen Quadrat und Zahl
            return squ_text

        
        # Erstellen der 10 Boxen mit den zu sortierenden Werten
        text41 = square_text_box('0.41', BLUE_D, WHITE)
        text41.shift( 2*UP, 4 * LEFT)
        text90 = square_text_box('0.9', BLUE_D, WHITE)
        text90.next_to(text41, buff=0)
        text03 = square_text_box('0.03', BLUE_D, WHITE)
        text03.next_to(text90, buff=0)
        text84 = square_text_box('0.84', BLUE_D, WHITE)
        text84.next_to(text03, buff=0)
        text28 = square_text_box('0.28', BLUE_D, WHITE)
        text28.next_to(text84, buff=0)
        text81 = square_text_box('0.81', BLUE_D, WHITE)
        text81.next_to(text28, buff=0)
        text19 = square_text_box('0.19', BLUE_D, WHITE)
        text19.next_to(text81, buff=0)
        text47 = square_text_box('0.47', BLUE_D, WHITE)
        text47.next_to(text19, buff=0)
        text04 = square_text_box('0.04', BLUE_D, WHITE)
        text04.next_to(text47, buff=0)
        text50 = square_text_box('0.50', BLUE_D, WHITE)
        text50.next_to(text04, buff=0)

        # Funktion um die Farbe eines Objektes zu ändern
        def change_text_color(text_obj, new_color): # Angeben des Objekts und die neue Farbe
            text_obj.set_color(new_color)   


       # Einblenden der Boxen
        self.play(GrowFromCenter(text41), GrowFromCenter(text90), GrowFromCenter(text03),
                  GrowFromCenter(text84),
                  GrowFromCenter(text47), GrowFromCenter(text19), GrowFromCenter(text81),
                  GrowFromCenter(text28),
                  GrowFromCenter(text04), GrowFromCenter(text50))
        self.wait(7)

        # Aufrufen der Funktion zum Erstellen der Buckets
        self.construct_buckets()

        # Beschriften der Buckets von 0 bis 9
        numbers = VGroup()
        for i in range(10):
            number_text = Text(str(i), font_size=18)  
            number_text.move_to([i * 1 - 4.5, -3.5, 0])  
            numbers.add(number_text)
        
        self.add(numbers)
        self.wait(2)

        # Ändern der Farbe der zu sortierenden Box mit der Funktion change_text_color
        change_text_color (text41, GREEN)
        self.wait(1)   
 
        # Erstellen der zu sortierenden Zahl in gesplittete Werte
        num_0 = Text('0.', color=WHITE)
        num_4 = Text('4', color=WHITE)
        num_1 = Text('1', color=WHITE)
        num =  VGroup(num_0,num_4,num_1)
        for i in range(1,len(num)):
            num[i].next_to(num[i-1])   
        
        # Einfügen des Objekts num
        num.move_to(text41.get_center())    # Plazieren des Objekts auf Box text41
        self.play(FadeIn(num),num.animate.shift(DOWN, LEFT))    # Einblenden Objekt, in neue Position bewegen 
        self.wait(3)
        change_text_color (num_4, RED)  # Farbe eines Wertes ändern
        self.wait(4)
        self.play(FadeOut(num))
        
        # Verschieben der Box text41 in den passenden Bucket
        self.play(text41.animate.shift([3.5, -4.5, 0]))
        self.wait(5)

        # Ändern der Farbe von Objekt text90
        change_text_color (text90, GREEN)
        self.wait(1)   
 
        # Erstellen der zu sortierenden Zahl in gesplittete Werte
        num_02 = Text('0.', color=WHITE)
        num_9 = Text('9', color=WHITE)
        num2 =  VGroup(num_02,num_9)
        for i in range(1,len(num2)):
            num2[i].next_to(num2[i-1])   
        
        # Einfügen des Objekts num2
        num2.move_to(text90.get_center()) 
        self.play(FadeIn(num2),num2.animate.shift(DOWN)) 
        self.wait(2)
        change_text_color (num_9, RED)
        self.wait(3)
        self.play(FadeOut(num2))
        
        # Verschieben der Box text90 in den passenden Bucket
        self.play(text90.animate.move_to([4.5, -2.5, 0]))
        self.wait(2)

        # die restlichen 8 Boxen in die jeweils passenden Buckets sortieren
        change_text_color (text03, GREEN) 
        self.play(text03.animate.move_to([-4.5, -2.5, 0])) 
        change_text_color (text84, GREEN) 
        self.play(text84.animate.move_to([3.5, -2.5, 0]))
        change_text_color (text28, GREEN)
        self.play(text28.animate.move_to([-2.5, -2.5, 0]))
        change_text_color (text81, GREEN)
        self.play(text81.animate.move_to([3.5, -1.5, 0]))
        change_text_color (text19, GREEN)
        self.play(text19.animate.move_to([-3.5, -2.5, 0]))
        change_text_color (text47, GREEN) 
        self.play(text47.animate.move_to([-0.5, -1.5, 0]))
        change_text_color (text04, GREEN)
        self.play(text04.animate.move_to([-4.5, -1.5, 0]))
        change_text_color (text50, GREEN)
        self.play(text50.animate.move_to([0.5, -2.5, 0]))
        
        # Umrahmen der Boxen die in einem Bucket zusammen sortiert wurden 
        sorting3 =  VGroup(text03,text04)
        box3 = SurroundingRectangle(sorting3, corner_radius=0.2, color=RED)
        self.play(Create(box3))
        sorting2 =  VGroup(text41,text47)
        box2 = SurroundingRectangle(sorting2, corner_radius=0.2, color=RED)
        self.play(Create(box2))
        sorting =  VGroup(text84,text81)
        box = SurroundingRectangle(sorting, corner_radius=0.2, color=RED)
        self.play(Create(box))
        self.wait(2)
 
        # Erstellen Pfeile   
        arrow = Arrow(start=[-5, 3, 0], end=[5, 3, 0])
        arrow.set_color(RED)
        arrow2 = Arrow(start=[-5.2, -1, 0], end=[-5.2, -3, 0])
        arrow2.set_color(RED)
        arrow3 = Arrow(start=[-1.2, -1, 0], end=[-1.2, -3, 0])
        arrow3.set_color(RED)
        arrow4 = Arrow(start=[2.8, -1, 0], end=[2.8, -3, 0])
        arrow4.set_color(RED)
        self.add(arrow)
        self.add(arrow2, arrow3, arrow4)
        self.wait(3)
        self.play(FadeOut(arrow, arrow2, arrow3, arrow4))
        self.wait(1)

        # Boxen text 84 und text81 werden nochmal vertauscht
        change_text_color (text84, YELLOW)   
        change_text_color (text81, YELLOW)
        self.wait(2)   
        num_03 = Text('0.', color=WHITE)
        num_84 = Text('84', color=WHITE)
        num3 =  VGroup(num_03,num_84)
        for i in range(1,len(num3)):
            num3[i].next_to(num3[i-1])   
        num3.move_to(text84.get_center()) 
        self.play(FadeIn(num3),num3.animate.shift(UP*2,LEFT)) 
        self.wait(1)
        num_04 = Text('0.', color=WHITE)
        num_81 = Text('81', color=WHITE)
        num4 =  VGroup(num_04,num_81)
        for i in range(1,len(num4)):
            num4[i].next_to(num4[i-1])   
        
        num4.move_to(text81.get_center()) 
        self.play(FadeIn(num4),num4.animate.shift(UP,RIGHT)) 
        self.wait(1)
        change_text_color (num_84, RED)
        change_text_color (num_81, RED)
        self.wait(1)
        self.play(num3.animate.shift(RIGHT*2),num4.animate.shift(LEFT*2))
        self.wait(1)
        self.play(FadeOut(num3,num4))
        
        self.play(text81.animate.shift(DOWN))
        self.play(text84.animate.shift(UP))
        self.wait(1)
        change_text_color (text84, GREEN)   
        change_text_color (text81, GREEN)
        self.wait(1)
        change_text_color (text47, YELLOW)   
        change_text_color (text41, YELLOW)
        self.wait(1)
        change_text_color (text47, GREEN)   
        change_text_color (text41, GREEN)
        self.wait(1)
        change_text_color (text03, YELLOW)   
        change_text_color (text04, YELLOW)
        self.wait(1)
        change_text_color (text03, GREEN)   
        change_text_color (text04, GREEN)
        self.wait(1)
        self.remove(box, box2, box3)
        self.play(text03.animate.move_to([-4.5, 0, 0]), text04.animate.move_to([-3.5, 0, 0]), text19.animate.move_to([-2.5, 0, 0]),
                  text28.animate.move_to([-1.5, 0, 0]), text41.animate.move_to([-0.5, 0, 0]), text47.animate.move_to([0.5, 0, 0]),
                  text50.animate.move_to([1.5, 0, 0]), text81.animate.move_to([2.5, 0, 0]), text84.animate.move_to([3.5, 0, 0]),
                  text90.animate.move_to([4.5, 0, 0]))  # Zusammenfügen der Boxen in der richtigen Reihenfolge
        self.wait(6)
        
# Erstellen der Buckets
    def construct_buckets(self):
        l= Line([-5, -3, 0], [5, -3, 0])
        l1= Line([-5, -3, 0], [-5, -1, 0])
        l2= Line([-4, -3, 0], [-4, -1, 0])
        l3= Line([-3, -3, 0], [-3, -1, 0])
        l4= Line([-2, -3, 0], [-2, -1, 0])
        l5= Line([-1, -3, 0], [-1, -1, 0])
        l6= Line([0, -3, 0], [0, -1, 0])
        l7= Line([1, -3, 0], [1, -1, 0])
        l8= Line([2, -3, 0], [2, -1, 0])
        l9= Line([3, -3, 0], [3, -1, 0])
        l10= Line([4, -3, 0], [4, -1, 0])
        l11= Line([5, -3, 0], [5, -1, 0])
        self.add(l,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11)
        self.wait(2)
        
if __name__ == "__main__":
    # os.system(f"manim -pql {__file__} MainAnim")
    os.system(f"manim -pqk {__file__} MainAnim")