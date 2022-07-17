'''
Draw graph for quadratic function
'''

from matplotlib import pyplot as plt
import math

# Draw the graph
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Quadratic Function Visually')
    plt.show()

def generate_x_y():
    # Generate values for r
    x_values = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50]
    # Empty list to store the calculated values of F
    y_values = []
    for x in x_values:
        # Calculate the value of the quadratic function
        y = x**2 + 2*x + 1
        y_values.append(y)

    # Call the draw_graph function
    draw_graph(x_values, y_values)

if __name__=='__main__':
    generate_x_y()



