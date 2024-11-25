from manim import *
import numpy as np
from Resourcen.colors import *

""" Eine 4 x 4 Matrix in Zeilenstufenform
 """
class Einheitsmatrix(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        Mobject.set_default(color=MMNMAINBLUE)
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
        self.play(Write(formula1))
        self.wait(2)

        # Füge Pfeile und Beschriftungen hinzu
        row_arrow = Arrow(start=RIGHT*4, end=LEFT*1, color=RED).shift(UP*0.2)
        col_arrow = Arrow(start=UP*2, end=DOWN*1, color=BLUE).shift(LEFT*0.5, RIGHT*1.5)

        row_label = MathTex("i").next_to(row_arrow, RIGHT)
        col_label = MathTex("j").next_to(col_arrow, UP)

        # Animation
        self.wait()
        self.play(
            GrowArrow(row_arrow),
            GrowArrow(col_arrow),
            Write(row_label),
            Write(col_label)
        )
        self.wait()

        # zweite Zeilentransformation:
        # Multiplikation der i-ten Zeile mit my \in K^x mit my \neq 0

        matrix2 = MathTex(r"M_i (\mu) = \begin{pmatrix}"
            r"1 & * & * & * \\"
            r" * & 1 & * & * \\"
            r" * & * & \lambda & * \\"
            r" * & * & * & 1 \\"
            r"\end{pmatrix}"
        ).shift(UP)

        """ self.play(Transform(matrix, matrix2),
                  FadeOut(text),
                  FadeOut(formula1))
        self.wait(2) """



        # dritte Zeilentransformation:
        # vertauschen von zweier Zeilen
        matrix_5x5 = MathTex(
            r"S_{ij} = \begin{pmatrix}"
            r"1 & * & * & * & * \\"
            r" * & 0 & * & 1 & * \\"
            r" * & * & 1 & * & * \\"
            r" * & 1 & * & 0 & * \\"
            r" * & * & * & * & 1 \\"
            r"\end{pmatrix}"
        ).shift(UP)

        # Add the 5x5 matrix to the scene
        """ self.play(Transform(matrix, matrix_5x5))
        self.wait(2) """
        
        # Add the matrix to the scene