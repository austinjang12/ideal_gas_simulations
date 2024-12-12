import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Constants 
R = 0.0821  #ideal gas constant (L*atm / mol*K)
V = 1.00  
n = 1.0  

#Initial conditions
initial_temperature = 273.15  
initial_pressure = n * R * initial_temperature / V  

fig, ax = plt.subplots(figsize=(8, 8))
container = plt.Rectangle((-1.5, 0), 3, 4, edgecolor="black", facecolor="none", linewidth=2)
ax.add_patch(container)

#molecule manipulation
num_molecules = 50
molecule_positions = np.random.uniform(low=[-1.4, 0.1], high=[1.4, 3.9], size=(num_molecules, 2))
molecule_velocities = np.random.uniform(-0.05, 0.05, size=(num_molecules, 2))
molecules = ax.scatter(molecule_positions[:, 0], molecule_positions[:, 1], color="yellow", s=20)

#thermometer stuff
thermometer_base = plt.Rectangle((1.6, 0), 0.2, 4, edgecolor="black", facecolor="white", linewidth=2)
thermometer_fill = plt.Rectangle((1.6, 0), 0.2, 0, color="red")
ax.add_patch(thermometer_base)
thermometer_patch = ax.add_patch(thermometer_fill)

#volume and temperature labels
pressure_text = ax.text(-1.8, 4.5, f"P = {initial_pressure:.2f} atm", fontsize=12, ha="left")
temperature_text = ax.text(0.5, 4.5, f"T = {initial_temperature:.2f} K", fontsize=12, ha="right")

def update(frame):
    global molecule_positions, molecule_velocities

    for i, pos in enumerate(molecule_positions):
        if pos[0] <= -1.4 or pos[0] >= 1.4:
            molecule_velocities[i, 0] *= -1
        if pos[1] <= 0.1 or pos[1] >= 3.9:
            molecule_velocities[i, 1] *= -1

    current_temperature = initial_temperature + 100 * np.sin(frame * np.pi / 100)
    current_pressure = initial_pressure * (current_temperature / initial_temperature)

    velocity_scale = np.sqrt(current_temperature / initial_temperature)
    molecule_velocities *= velocity_scale / np.linalg.norm(molecule_velocities, axis=1, keepdims=True)

    molecule_positions += molecule_velocities

    molecule_positions[:, 0] = np.clip(molecule_positions[:, 0], -1.4, 1.4)
    molecule_positions[:, 1] = np.clip(molecule_positions[:, 1], 0.1, 3.9)

    molecules.set_offsets(molecule_positions)

    pressure_text.set_text(f"P = {current_pressure:.2f} atm")
    temperature_text.set_text(f"T = {current_temperature:.2f} K")

    thermometer_patch.set_height(4 * (current_temperature / (initial_temperature + 100)))

    return [molecules, pressure_text, temperature_text, thermometer_patch]

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)

writer = FFMpegWriter(fps=20, metadata={"title": "Boyle's Law Animation"}, bitrate=1800)
ani.save("gaylussac_law_animation.mp4", writer=writer)

plt.xlim(-2, 2)
plt.ylim(0, 5)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.show()

