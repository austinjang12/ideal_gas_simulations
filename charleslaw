import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FuncAnimation, FFMpegWriter

#initial conditiosn
R = 0.0821  # Ideal gas constant (L*atm / mol*K)
initial_temperature = 273.15  #
n = 1.0 
initial_volume = 1.0 

fig, ax = plt.subplots(figsize=(6, 8))

container = plt.Rectangle((-1.5, 0), 3, 4, edgecolor="black", facecolor="none", linewidth=2)
ax.add_patch(container)

piston = plt.Rectangle((-1.5, 4), 3, 0.3, color="blue")
ax.add_patch(piston)

num_molecules = 100
molecule_positions = np.random.uniform(low=[-1.4, 0.1], high=[1.4, 3.9], size=(num_molecules, 2))
molecule_velocities = np.random.uniform(-0.05, 0.05, size=(num_molecules, 2))
molecules = ax.scatter(molecule_positions[:, 0], molecule_positions[:, 1], color="yellow", s=20)

volume_text = ax.text(-1.8, 4.5, f"V = {initial_volume:.2f} L", fontsize=12, ha="left")
temperature_text = ax.text(0.5, 4.5, f"T = {initial_temperature:.2f} K", fontsize=12, ha="right")

thermometer_x = 1.6  
thermometer_width = 0.1
max_height = 4  
thermometer = plt.Rectangle((thermometer_x, 0), thermometer_width, 0, color="red")
ax.add_patch(thermometer)

visibility_scaling_factor = 0.5 

def update(frame):
    global molecule_positions, molecule_velocities

    piston_y = 4 - (4 - 0.2) * (np.sin(frame * np.pi / 100) + 1) / 2
    piston.set_y(piston_y)  

    current_volume = initial_volume * (piston_y - 0) / 4
    current_temperature = initial_temperature * (current_volume / initial_volume) 

    velocity_scale = np.sqrt(current_temperature / initial_temperature) * visibility_scaling_factor
    molecule_velocities *= velocity_scale / np.linalg.norm(molecule_velocities, axis=1, keepdims=True)

    thermometer_base = plt.Rectangle((1.6, 0), 0.2, 4, edgecolor="black", facecolor="white", linewidth=2)
    thermometer_fill = plt.Rectangle((1.6, 0), 0.2, 0, color="red")
    ax.add_patch(thermometer_base)
    thermometer_patch = ax.add_patch(thermometer_fill)

    molecule_positions += molecule_velocities

    for i, pos in enumerate(molecule_positions):
        if pos[0] <= -1.4 or pos[0] >= 1.4:
            molecule_velocities[i, 0] *= -1

        if pos[1] <= 0.1 or pos[1] >= piston_y - 0.2:
            molecule_velocities[i, 1] *= -1

    molecule_positions[:, 0] = np.clip(molecule_positions[:, 0], -1.4, 1.4) 
    molecule_positions[:, 1] = np.clip(molecule_positions[:, 1], 0.1, piston_y - 0.2) 
    molecules.set_offsets(molecule_positions)

    volume_text.set_text(f"V = {current_volume:.2f} L")
    temperature_text.set_text(f"T = {current_temperature:.2f} K")

    thermometer_height = (current_temperature - initial_temperature) / (max_height - initial_temperature) * max_height
    thermometer.set_height(thermometer_height)  
    thermometer_patch.set_height(5* (current_temperature / (initial_temperature + 100)))

    return [piston, molecules, volume_text, temperature_text, thermometer_patch]

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)

writer = FFMpegWriter(fps=20, metadata={"title": "Charles's Law Animation"}, bitrate=1800)
ani.save("charles_law_animation.mp4", writer=writer)

plt.xlim(-2, 2)
plt.ylim(0, 5)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.show()
