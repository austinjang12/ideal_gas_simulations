import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter

#constants
R = 0.0821  # ideal gas constant (L·atm / mol·K)
T = 273.15  # temperature in Kelvin
n = 1.0  # moles

#nitial volume and pressure 
initial_volume = 1.0  
initial_pressure = (n * R * T) / initial_volume  

fig, ax = plt.subplots(figsize=(6, 8))

container = plt.Rectangle((-1.5, 0), 3, 4, edgecolor="black", facecolor="none", linewidth=2)
ax.add_patch(container)

#initial position of piston
piston = plt.Rectangle((-1.5, 4), 3, 0.3, color="blue")
ax.add_patch(piston)

#molecules manipulation
num_molecules = 100
molecule_positions = np.random.uniform(low=[-1.4, 0.1], high=[1.4, 3.9], size=(num_molecules, 2))
molecules = ax.scatter(molecule_positions[:, 0], molecule_positions[:, 1], color="yellow", s=20)

#volume and pressure labels
volume_text = ax.text(-1.8, 4.5, f"V = {initial_volume:.2f} L", fontsize=12, ha="left")
pressure_text = ax.text(0.5, 4.5, f"P = {initial_pressure:.2f} atm", fontsize=12, ha="right")

def update(frame):
    global molecule_positions

    piston_y = 4 - (4 - 0.2) * (np.sin(frame * np.pi / 100) + 1) / 2
    piston.set_y(piston_y) 

    molecule_positions[:, 1] = np.random.uniform(0.1, piston_y - 0.2, size=num_molecules)
    molecule_positions[:, 0] = np.random.uniform(-1.4, 1.4, size=num_molecules)

    molecules.set_offsets(molecule_positions)

    current_volume = initial_volume * (piston_y - 0) / 4  
    current_pressure = (n * R * T) / current_volume  
    volume_text.set_text(f"V = {current_volume:.2f} L")
    pressure_text.set_text(f"P = {current_pressure:.2f} atm")

    return [piston, molecules, volume_text, pressure_text]

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)

writer = FFMpegWriter(fps=20, metadata={"title": "Boyle's Law Animation"}, bitrate=1800)
ani.save("boyles_law_animation.mp4", writer=writer)

plt.xlim(-2, 2)
plt.ylim(0, 5)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.show()

