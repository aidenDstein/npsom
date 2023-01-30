import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import time

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Draw the hippie astronaut
astro = patches.Rectangle((0,0), 2, 4, linewidth=1, edgecolor='black', facecolor='yellow')
astro_head = patches.Circle((1,5), 1, linewidth=1, edgecolor='black', facecolor='red')
astro_left_eye = patches.Circle((0.5, 4.5), 0.2, color='black')
astro_right_eye = patches.Circle((1.5, 4.5), 0.2, color='black')

ax.add_patch(astro)
ax.add_patch(astro_head)
ax.add_patch(astro_left_eye)
ax.add_patch(astro_right_eye)

# Define the animation update function
def update(frame):
    astro.set_xy((frame,0))
    astro_head.set_center((frame+1, 5))
    astro_left_eye.center = (frame+0.5, 4.5)
    astro_right_eye.center = (frame+1.5, 4.5)
    return astro, astro_head, astro_left_eye, astro_right_eye

# Animate for 10 seconds
start_time = time.time()
while time.time() - start_time <= 10:
    for x in np.linspace(-10, 10, 100):
        update(x)
        plt.pause(0.01)

plt.show()