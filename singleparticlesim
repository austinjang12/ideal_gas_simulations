from manim import *
import numpy as np

class VisualizingVariables(Scene):
    def construct(self):
        container = Rectangle(width=6, height=4).set_color(WHITE)
        self.add(container)
        
        molecule = Dot(point=ORIGIN, color=BLUE).scale(1.5)
        velocity = np.array([0.3, 0.4, 0])  
        molecule_vector = Arrow(start=ORIGIN, end=velocity, color=RED, buff=0).scale(0.5)
        molecule_group = VGroup(molecule, molecule_vector)
        self.add(molecule_group)

        boundary_limits = {
            "left": -container.width / 2,
            "right": container.width / 2,
            "bottom": -container.height / 2,
            "top": container.height / 2
        }

        def confine_molecule():
            nonlocal boundary_limits
            x, y, _ = molecule.get_center()
            if x - molecule.radius < boundary_limits["left"]:
                molecule.move_to(np.array([boundary_limits["left"] + molecule.radius, y, 0]))
                velocity[0] *= -1 
            if x + molecule.radius > boundary_limits["right"]:
                molecule.move_to(np.array([boundary_limits["right"] - molecule.radius, y, 0]))
                velocity[0] *= -1 
            if y - molecule.radius < boundary_limits["bottom"]:
                molecule.move_to(np.array([x, boundary_limits["bottom"] + molecule.radius, 0]))
                velocity[1] *= -1 
            if y + molecule.radius > boundary_limits["top"]:
                molecule.move_to(np.array([x, boundary_limits["top"] - molecule.radius, 0]))
                velocity[1] *= -1  

        def update_molecule(mob, dt):
            nonlocal velocity, boundary_limits
            molecule, molecule_vector = mob[0], mob[1]
            molecule.shift(velocity * dt)
            molecule_vector.shift(velocity * dt)
            confine_molecule()

            molecule_vector.put_start_and_end_on(molecule.get_center(), molecule.get_center() + velocity)

        molecule_group.add_updater(update_molecule)

        self.add(molecule_group)
        self.wait(5) 

        new_width = 4
        new_height = 2.5
        self.play(
            container.animate.set(width=new_width, height=new_height),
            run_time=2
        )
        boundary_limits["left"] = -new_width / 2
        boundary_limits["right"] = new_width / 2
        boundary_limits["bottom"] = -new_height / 2
        boundary_limits["top"] = new_height / 2
        confine_molecule()  
        self.wait(5)

        expanded_width = 8
        expanded_height = 5
        self.play(
            container.animate.set(width=expanded_width, height=expanded_height),
            run_time=2
        )
        boundary_limits["left"] = -expanded_width / 2
        boundary_limits["right"] = expanded_width / 2
        boundary_limits["bottom"] = -expanded_height / 2
        boundary_limits["top"] = expanded_height / 2
        confine_molecule()  
        self.wait(5)



if __name__ == "__main__":
    scene = VisualizingVariables()
    scene.render() 
