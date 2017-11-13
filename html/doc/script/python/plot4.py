
# legend loc
# per https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
# 0 = best
# 9 = upper-center
# 4 = lower-right

# points only
x = [1,3,6,9]
y = [4,4,7,8]
plt.scatter(x,y)
formatgraph('Four Data Points')
ax = plt.gca();
ax.set_xlim([0,10])
ax.set_ylim([0,10])
savegraph('Four Data Points')
plt.show()

# start over

# points
x = [1,3,6,9]
y = [4,4,7,8]
plt.scatter(x,y)
ax = plt.gca();
ax.set_xlim([0,10])
ax.set_ylim([0,10])

# add three lines
x = np.array(np.arange(0,11,.1));
plt.plot(x,2 * x + 3, label='y=2x+3'); 
plt.plot(x,1.5 * x + 2, label='y=1.5x+2'); 
plt.plot(x,.8 * x + 2, label='y=.8x+2'); 
plt.legend()
formatgraph('Trial and Error')
savegraph('Trial and Error')
plt.show()

# start over

# points
x = [1,3,6,9]
y = [4,4,7,8]
plt.scatter(x,y)
ax = plt.gca();
ax.set_xlim([0,10])
ax.set_ylim([0,10])

# add lines
x = np.array(np.arange(0,11,.1));
plt.plot(x,.6 * x + 2.9, label='y=.6x+2.9');   # brute force
plt.plot(x,.56 * x + 3.1, label='y=.56x+3.1'); # normal equation
                                               # gradient descent
plt.legend()
formatgraph('Three Techniques')  # ? advanced techniques, mathematical techniques, least squares techniques
savegraph(  'Three Techniques')
plt.show()

