import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.pyplot import cm
from matplotlib.cbook import get_sample_data

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
xmin, xmax = 0, 3
ymin, ymax = 0, 210
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))

# Add rainbow lines
dy = float(ymax-ymin)/100
rainbow_lines = []
n_colors = 5
for i in range(n_colors):
    rainbow_lines.append(ax.plot([], [], c=cm.rainbow(float(i)/(n_colors-1)), lw=10)[0])

# Add nyan cat
im = plt.imread(get_sample_data(os.getcwd()+'/nyan_cat.png'))
nyan_ax = fig.add_axes([0., 0.5, 0.2, 0.2], zorder=1)
nyan_ax.axis('off')
image = nyan_ax.imshow(im)

# Add trace data
data = np.loadtxt('trace.dat')
xs = data[:,0]
ys = data[:,1]

# Initialization function: plot the background of each frame
def init():
    for line in rainbow_lines:
        line.set_data([], [])
    return [rainbow_lines, image]

# Animation function.  This is called sequentially
def animate(i):
    for j,line in enumerate(rainbow_lines):
        #x = xs[i:10+i]
        x = np.linspace(0, 0.75*xmax, 10)
        y = dy*j + ys[i:10+i]
        line.set_data(x, y)
    nyan_x = 0.65
    nyan_y = (ys[10+i-1] - ymin)/(ymax - ymin)
    nyan_ax.set_position([nyan_x, nyan_y, 0.1, 0.1])
    return [rainbow_lines, image]

# Call animation
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=100, blit=False)
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
