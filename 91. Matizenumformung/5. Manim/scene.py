from manim import *
import numpy as np
from Resourcen.colors import *

""" Eine 4 x 4 Matrix in Zeilenstufenform
 """

class Thumbnail(Scene):
    def construct(self):
        self.camera.background_color = None
        Mobject.set_default(color=BLACK)
        MyTexTemplate = TexTemplate(
            tex_compiler="xelatex",
            output_format=".xdv",
        )
        Text.set_default(font="Poppins Light", color=BLACK)
        MyTexTemplate.add_to_preamble(
            r"\usepackage{fontspec}\setmainfont{Poppins-Light.ttf}"
        )

        matrix = MathTex(
            r"\begin{pmatrix}"
            r"  &   &   &   \\"
            r"   &   &   &   \\"
            r" * & \lambda & 1 & * \\"
            r" * & * & * & 1 \\"
            r"\end{pmatrix}"
        ).scale(1.5)

        self.add(matrix)

class Einheitsmatrix(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        Mobject.set_default(color=BLACK)
        MyTexTemplate = TexTemplate(
            tex_compiler="xelatex",
            output_format=".xdv",
        )
        Text.set_default(font="Poppins Light", color=BLACK)
        MyTexTemplate.add_to_preamble(
            r"\usepackage{fontspec}\setmainfont{Poppins-Light.ttf}"
        )

        # erste Zeilentransformation:
        # Addition des lambda-fachen der i-ten Zeile zur j-ten Zeile
        # i \neq j
        # A_{ij} (\lambda) = matrix

        matrix = MathTex(
            r"A_{i,j} (\lambda) = \begin{pmatrix}"
            r"1 & * & * & * \\"
            r" * & 1 & * & * \\"
            r" * & \lambda & 1 & * \\"
            r" * & * & * & 1 \\"
            r"\end{pmatrix}"
        ).shift(UP)

        text = Tex("für $i \\neq j$").next_to(matrix, RIGHT)

        # A \to A_{ij} (\lambda) A
        formula1 = MathTex(r"A \to A_{i,j} (\lambda) A").shift(DOWN)

        self.play(Write(matrix))
        self.play(Write(text))
        self.wait(2)

        # Füge Pfeile und Beschriftungen hinzu
        row_arrow = Arrow(start=LEFT*1, end=RIGHT*0.9, color=MMNMAINRED).shift(UP*0.7)
        col_arrow = Arrow(start=UP*2, end=UP*0, color=MMNMAINLIGHTBLUE).shift(RIGHT*0.8, UP*0.7)

        row_label = MathTex("i").next_to(row_arrow, LEFT).set_color(MMNMAINRED)
        col_label = MathTex("j").next_to(col_arrow, UP).set_color(MMNMAINLIGHTBLUE)


        # Animation
        self.wait()
        self.play(
            GrowArrow(row_arrow),
            Write(row_label),
            FadeToColor(matrix[0][1], MMNMAINRED),
        )
        self.wait()
        self.play(
            GrowArrow(col_arrow),
            Write(col_label),
            FadeToColor(matrix[0][3], MMNMAINLIGHTBLUE),
        )
        self.wait()
        self.play(Write(formula1))
        self.wait(2)
        self.play(Indicate(formula1[0][2:6], color=MMNMAINYELLOW))
        self.wait()

        invertierbar1 = MathTex(r"A_{i,j}(\lambda) A_{i,j}(-\lambda) = I").shift(DOWN)
        self.play(Transform(formula1, invertierbar1))
        self.wait()



        # zweite Zeilentransformation:
        # Multiplikation der i-ten Zeile mit my \in K^x mit my \neq 0

        matrix2 = MathTex(r"M_i (\mu) = \begin{pmatrix}"
            r"1 & * & * & * \\"
            r" * & 1 & * & * \\"
            r" * & * & \mu & * \\"
            r" * & * & * & 1 \\"
            r"\end{pmatrix}"
        ).shift(UP)

        self.play(
            Transform(matrix, matrix2),
            FadeOut(text),
            FadeOut(formula1),
            FadeOut(row_arrow),
            FadeOut(col_arrow),
            FadeOut(row_label),
            FadeOut(col_label),
            )
        self.wait(2)

        row_arrow2 = Arrow(start=LEFT*1, end=RIGHT*1.5, color=MMNMAINLIGHTBLUE).shift(UP*0.7)
        col_arrow2 = Arrow(start=UP*2, end=UP*0, color=MMNMAINLIGHTBLUE).shift(RIGHT*1.5, UP*0.7)

        row_label2 = MathTex("i").next_to(row_arrow2, LEFT).set_color(MMNMAINLIGHTBLUE)
        col_label2 = MathTex("i").next_to(col_arrow2, UP).set_color(MMNMAINLIGHTBLUE)

        self.play(
            GrowArrow(row_arrow2),
            Write(row_label2),
            GrowArrow(col_arrow2),
            Write(col_label2),
        )
        self.wait(2)
        self.play(
            FadeToColor(matrix2[0][20:21], MMNMAINYELLOW),
        )
        self.wait(2)
        self.play(
            FadeOut(matrix2[0][20:21]),
        )
        self.wait(2)
        self.play(
            FadeOut(row_arrow2),
            FadeOut(col_arrow2),
            FadeOut(row_label2),
            FadeOut(col_label2),
        )
        self.wait(2)

        invertierbar2 = MathTex(r"M_i(\mu) M_i(\mu^{-1}) = I").shift(1.5*DOWN)
        self.play(Write(invertierbar2))
        self.wait()


        # dritte Zeilentransformation:
        # vertauschen von zwei Zeilen
        matrix_5x5 = MathTex(
            r"S_{ij} = \begin{pmatrix}"
            r"1 & * & * & * & * \\"
            r" * & 0 & * & 1 & * \\"
            r" * & * & 1 & * & * \\"
            r" * & 1 & * & 0 & * \\"
            r" * & * & * & * & 1 \\"
            r"\end{pmatrix}"
        ).shift(UP)
        
        row_arrow3 = Arrow(start=LEFT*1, end=RIGHT*1, color=MMNMAINLIGHTBLUE).shift(UP*0.4, LEFT)
        col_arrow3 = Arrow(start=UP*2, end=UP*-0.2, color=MMNMAINLIGHTBLUE).shift(UP*0.7)

        row_label3 = MathTex("i").next_to(row_arrow3, LEFT).set_color(MMNMAINLIGHTBLUE)
        col_label3 = MathTex("j").next_to(col_arrow3, UP).set_color(MMNMAINLIGHTBLUE)

        row_arrow4 = Arrow(start=LEFT*1, end=RIGHT*2.5, color=MMNMAINGREEN).shift(UP*1.6, LEFT)
        col_arrow4 = Arrow(start=UP*2, end=UP*1, color=MMNMAINGREEN).shift(UP*0.7, RIGHT*1.5)

        row_label4 = MathTex("j").next_to(row_arrow4, LEFT).set_color(MMNMAINGREEN)
        col_label4 = MathTex("i").next_to(col_arrow4, UP).set_color(MMNMAINGREEN)

        # Add the 5x5 matrix to the scene
        self.play(Transform(matrix, matrix_5x5),
                  FadeOut(invertierbar2))
        self.wait(2)
        self.play(
            GrowArrow(row_arrow3),
            Write(row_label3),
            GrowArrow(col_arrow3),
            Write(col_label3),
        )
        self.wait(2)
        self.play(
            Transform(row_arrow3, row_arrow4),
            Transform(col_arrow3, col_arrow4),
            Transform(row_label3, row_label4),
            Transform(col_label3, col_label4),
        )
        self.wait(2)
        self.play(
            FadeOut(row_arrow3),
            FadeOut(col_arrow3),
            FadeOut(row_label3),
            FadeOut(col_label3),
        )
        self.wait()

        invertierbar3 = MathTex(r"S_{i,j}S_{i,j} = I").shift(1.5*DOWN)
        self.play(Write(invertierbar3))
        self.wait()
        self.play(Unwrite(invertierbar3))
        self.wait()


        
        # Example -------------------------------------
        matrix_2x2 = MathTex(
            r"\begin{pmatrix}"
            r"1 & 2 \\"
            r"3 & 1 \\"
            r"\end{pmatrix}"
        ).shift(UP)

        self.play(
            Transform(matrix, matrix_2x2)
        )
        self.play(
            FadeIn(matrix_2x2),
            FadeOut(matrix)
        )
        self.wait()

        matrix_2x2_erweitert = MathTex(
            r"\begin{pmatrix}"
            r"1 & 2 & 1 & 0 \\"
            r"3 & 1 & 0 & 1 \\"
            r"\end{pmatrix}"
        ).shift(UP)

        # Add the 2x2 matrix to the scene
        self.wait(2)

        # Extend the 2x2 matrix by adding new columns
        self.play(TransformMatchingShapes(matrix_2x2, matrix_2x2_erweitert))
        self.wait(2)

        trans_matrix = MathTex(
            r"\begin{pmatrix}"
            r"1 & 0\\"
            r"-3 & 1\\"
            r"\end{pmatrix}"
        ).next_to(matrix_2x2_erweitert, LEFT)

        self.play(Write(trans_matrix))
        self.wait()

        matrix = MathTex(
            r"A_{i,j} (\lambda) = \begin{pmatrix}"
            r"1 & * & * & * \\"
            r" * & 1 & * & * \\"
            r" * & \lambda & 1 & * \\"
            r" * & * & * & 1 \\"
            r"\end{pmatrix}"
        ).shift(2*DOWN)


        self.play(Write(matrix))
        self.wait(2)
        self.play(FadeToColor(matrix[0][3], MMNMAINLIGHTBLUE),
                  Wiggle(matrix[0][3]))
        self.wait()
        self.play(FadeToColor(matrix[0][1], MMNMAINBLUE),
                  Wiggle(matrix[0][1]))
        self.wait(2)


        # Create the new element to replace \lambda
        new_element = MathTex(r"\lambda").move_to(trans_matrix[0][3:5])

        # Transform \lambda to the new element
        self.play(Transform(trans_matrix[0][4], new_element),
                  FadeOut(trans_matrix[0][3]))
        self.wait()

        arrowshowcolum = Arrow(start=RIGHT*1, end=LEFT*1, color=MMNMAINBLUE).move_to(matrix_2x2, RIGHT).shift(RIGHT*2.5, UP*0.3)
        arrowshowcolum.generate_target()
        arrowshowcolum.target.shift(DOWN*0.6)

        new_element2 = MathTex(r"-3").move_to(trans_matrix[0][3:5])

        self.play(Create(arrowshowcolum))
        self.wait()
        self.play(MoveToTarget(arrowshowcolum))
        self.wait()
        self.play(Uncreate(arrowshowcolum))
        self.wait()

        self.play(Indicate(trans_matrix[0][4], color=MMNMAINYELLOW))
        self.wait(2)
        self.play(Transform(trans_matrix[0][4], new_element2))
        self.wait()
        self.play(Unwrite(matrix))
        self.wait()

        equalssymbol = MathTex("=").next_to(matrix_2x2_erweitert, RIGHT)
        equals = MathTex(
            r"\begin{pmatrix}"
            r"1 & 2 & 1 & 0 \\"
            r"0 & -5 & -3 & 1 \\"
            r"\end{pmatrix}").next_to(equalssymbol, RIGHT)
        
        equals.generate_target()
        equals.target.shift(LEFT*4.5)
        
        self.play(
            Write(equalssymbol),
            Write(equals))
        self.wait()
        self.play(Uncreate(trans_matrix),
                  Uncreate(matrix_2x2_erweitert))
        self.play(MoveToTarget(equals))
        self.wait()

        matrix_2x2_multi = MathTex(
            r"\begin{pmatrix}"
            r"1 & 0 \\"
            r"0 & -\frac{1}{5} \\"
            r"\end{pmatrix}"
        ).next_to(equals,LEFT)
        
        self.play(Write(matrix_2x2_multi))
        self.wait()

        equals2 = MathTex(
            r"\begin{pmatrix}"
            r"1 & 2 & 1 & 0 \\"
            r"0 & 1 & \frac{3}{5} & -\frac{1}{5} \\"
            r"\end{pmatrix}").next_to(equalssymbol, RIGHT)
        
        equals2.generate_target()
        equals2.target.shift(LEFT*4.5)

        self.play(Write(equals2))
        self.wait()
        self.play(Uncreate(matrix_2x2_multi),
                  Uncreate(equals))
        self.play(MoveToTarget(equals2))
        self.wait()

        self.play(Indicate(equals2[0][2:3], color=MMNMAINYELLOW))
        self.wait()

        matrix_2x2_multi2 = MathTex(
            r"\begin{pmatrix}"
            r"1 & -2 \\"
            r"0 & 1 \\"
            r"\end{pmatrix}"
        ).next_to(equals2,LEFT)

        self.play(Write(matrix_2x2_multi2))
        self.wait()

        equals3 = MathTex(
            r"\begin{pmatrix}"
            r"1 & 0 & -\frac{1}{5} & \frac{2}{5} \\"
            r"0 & 1 & \frac{3}{5} & -\frac{1}{5} \\"
            r"\end{pmatrix}").next_to(equalssymbol, RIGHT)
        
        self.play(Write(equals3))
        self.wait()
        self.play(FadeToColor(equals3[0][3:10], MMNMAINBLUE),
                    FadeToColor(equals3[0][12:19], MMNMAINBLUE))
        self.wait(2)

        equals3.generate_target()
        equals3.target.shift(LEFT*5)

        self.play(Uncreate(matrix_2x2_multi2),
                    Uncreate(equals2))
        self.play(MoveToTarget(equals3))
        self.wait()

        equals4 = MathTex(
            r"\begin{pmatrix}"
            r"1 & 2 \\"
            r"3 & 1 \\"
            r"\end{pmatrix}"
            r"\begin{pmatrix}"
            r"-\frac{1}{5} & \frac{2}{5} \\"
            r"\frac{3}{5} & -\frac{1}{5} \\"
            r"\end{pmatrix}").next_to(equalssymbol, RIGHT).shift(LEFT*5)
        
        equals4[0][7:21].set_color(MMNMAINBLUE)
        
        self.play(TransformMatchingShapes(equals3, equals4))
        self.wait()

        equals5 = MathTex(
            r"\begin{pmatrix}"
            r"1 & 0 \\"
            r"0 & 1 \\"
            r"\end{pmatrix}"
        ).next_to(equalssymbol, RIGHT)

        self.play(Write(equals5[0][0:2]),
                  Write(equals5[0][5:6]),
                  )
        self.play(Write(equals5[0][1:2]))
        self.wait()
        self.play(Write(equals5[0][2:3]))
        self.wait()
        self.play(Write(equals5[0][3:4]))
        self.wait()
        self.play(Write(equals5[0][4:5]))

        self.wait(2)





