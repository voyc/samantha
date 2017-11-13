from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

dim = 10

# plane 1
X, Y = np.meshgrid([-dim, dim], [-dim, dim])
Z = np.zeros((2, 2))
Z = Y + 1
Z = Z * [.6,1.5]
ax.plot_surface(X, Y, Z, color='red', alpha=.5, linewidth=0, zorder=1)

# plane 2
angle = .5
X2, Y2 = np.meshgrid([-dim, dim], [-dim, dim])
Z2 = np.zeros((2, 2))
Z2 = Y2 + 1
Z2 = Z2 * [3,-2]
ax.plot_surface(X2, Y2, Z2, color='blue', alpha=.5, linewidth=0, zorder=-1)

#a·x+ b·y + c·z  + d  = 0



#r = 7
#M = 1000
#th = np.linspace(0, 2 * np.pi, M)
#
#x, y, z = r * np.cos(th),  r * np.sin(th), angle * r * np.sin(th)

#ax.plot_surface(X2, Y3, Z3, color='blue', alpha=.5, linewidth=0, zorder=-1)
#ax.plot(x[y < 0], y[y < 0], z[y < 0], lw=5, linestyle='--', color='green', zorder=0)

#ax.plot_surface(X, Y, Z, color='red', alpha=.5, linewidth=0, zorder=1)
#ax.plot(r * np.sin(th), r * np.cos(th), np.zeros(M), lw=5, linestyle='--', color='k', zorder=2)

#ax.plot_surface(X2, Y2, Z2, color='blue', alpha=.5, linewidth=0, zorder=3)
#ax.plot(x[y > 0], y[y > 0], z[y > 0], lw=5, linestyle='--', color='green', zorder=4)

#plt.axis('off')
#ax = plt.gca();

# Get rid of the panes                          
#ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0)) 
#ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0)) 
#ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0)) 

# Get rid of the spines                         
#ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0)) 
#ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0)) 
#ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

# Get rid of the ticks                          
#ax.set_xticks([])                               
#ax.set_yticks([])                               
#ax.set_zticks([])

plt.show()


