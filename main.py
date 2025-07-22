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

    center_x = -15 + t * 0.3

    Z_bubble = alcubierre_shape(X, Y, center_x)

    # Overlay warp distortion
    ax.plot_surface(X, Y, Z_bubble, cmap='inferno', alpha=0.85, edgecolor='none')

    # View settings
    ax.view_init(elev=30, azim=45)
    ax.set_box_aspect([1, 1, 0.5])
    ax.set_title("Warp Bubble Traversing Spacetime Grid", pad=20)

    # Enable axis labels and numbers
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Warp Curvature")

    ax.set_xticks(np.arange(-10, 11, 5))
    ax.set_yticks(np.arange(-10, 11, 5))
    ax.set_zticks(np.arange(-4, 5, 2))

ani = animation.FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
