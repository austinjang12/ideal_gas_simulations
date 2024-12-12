from manim import *

class Intro(Scene):
    def construct(self):
        title = MathTex(r"PV=nRT")
        basel = Tex(r"This is the Ideal Gas Law")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait(10)
        self.play(FadeOut(title,basel))

        title2 = Tex(r"Why ideal?")
        base2 = Tex(r"There are a few assumptions")
        VGroup(title2, base2).arrange(DOWN)
        self.play(
            Write(title2),
            FadeIn(base2, shift=DOWN),
        )
        self.wait(2)
        transform_title2 = Tex(r"Assumptions")
        transform_title2.to_corner(UP + LEFT)
        self.play(
            Transform(title2, transform_title2),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in base2]),
        )
        self.wait(5)
        description1 = Tex(r"Gas particles are equally sized")
        description3 = Tex(r"Gas particles have negigible volume ")
        description2 = Tex(r"No intermolecular forces")
        description4 = Tex(r"Gas molecules have perfect elastic collisions")
        VGroup(description1, description2, description3, description4).arrange(DOWN)
        self.play(
            FadeIn(description1, shift=DOWN),
            FadeIn(description2, shift=DOWN),
            FadeIn(description3, shift=DOWN),
            FadeIn(description4, shift=DOWN),
        )
        self.wait(15)
        self.play(FadeOut(title2, transform_title2,description1, description2, description3, description4))

        title3 = MathTex(r"PV=nRT")
        VGroup(title3).arrange(DOWN)
        self.play(
            Write(title3),
        )
        self.wait(3)
        transform_title3 = MathTex(r"PV=nRT")
        transform_title3.to_corner(UP + LEFT)
        self.play(
            Transform(title3, transform_title3), 
        )
        self.wait(2)

        description1 = Tex(r"P: Pressure")
        description2 = Tex(r"V: Volume")
        description3 = Tex(r"n: moles")
        description4 = Tex(r"R: Gas Constant")
        description5 = Tex(r"T: Temperature")
        VGroup(description1, description2, description3, description4, description5).arrange(DOWN)
        self.play(
            FadeIn(description1, shift=DOWN),
            FadeIn(description2, shift=DOWN),
            FadeIn(description3, shift=DOWN),
            FadeIn(description4, shift=DOWN),
            FadeIn(description5, shift=DOWN),
        )
        self.wait(15)

        boyles_law = MathTex(r"P \propto \frac{1}{V}")
        boyles_law_label = Tex(r"Boyle's Law")
        VGroup(boyles_law, boyles_law_label).arrange(DOWN)
        self.play(
            FadeOut(VGroup(description1, description2, description3, description4, description5)),
            FadeIn(boyles_law, shift=UP),
            FadeIn(boyles_law_label, shift=UP),
        )
        self.wait(3)

        charles_law = MathTex(r"V \propto T")
        charles_law_label = Tex(r"Charles' Law")
        VGroup(charles_law, charles_law_label).arrange(DOWN)
        self.play(
            FadeOut(boyles_law),
            FadeOut(boyles_law_label),
            FadeIn(charles_law, shift=UP),
            FadeIn(charles_law_label, shift=UP),
        )
        self.wait(3)

        gay_lussac_law = MathTex(r"P \propto T")
        gay_lussac_law_label = Tex(r"Gay-Lussac's Law")
        VGroup(gay_lussac_law, gay_lussac_law_label).arrange(DOWN)
        self.play(
            FadeOut(charles_law),
            FadeOut(charles_law_label),
            FadeIn(gay_lussac_law, shift=UP),
            FadeIn(gay_lussac_law_label, shift=UP),
        )
        self.wait(3)


if __name__ == "__main__":
    scene = Intro()
    scene.render()
