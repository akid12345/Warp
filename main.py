import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Create spatial grid
x = np.linspace(-10, 10, 80)
y = np.linspace(-10, 10, 80)
X, Y = np.meshgrid(x, y)

# Define Alcubierre warp shape
def alcubierre_shape(X, Y, center_x):
    z_compress = -2 * np.exp(-((X - center_x - 3)**2 + Y**2) / 5)
    z_expand   =  2 * np.exp(-((X - center_x + 3)**2 + Y**2) / 5)
    return z_compress + z_expand

# Plot setup
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Animation update function
def update(t):
    ax.clear()

    # Move bubble smoothly across the grid
    center_x = -15 + t * 0.3

    # Calculate moving warp field
    Z_bubble = alcubierre_shape(X, Y, center_x)

    # Draw static flat grid
    ax.plot_wireframe(X, Y, np.zeros_like(X), rstride=2, cstride=2, color='gray', linewidth=0.3)

    # Overlay moving curvature on top
    ax.plot_surface(X, Y, Z_bubble, cmap='inferno', alpha=0.8, edgecolor='none')

    # View settings
    ax.view_init(elev=30, azim=45)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_box_aspect([1, 1, 0.5])

# Animate the full traversal
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)
plt.show()

