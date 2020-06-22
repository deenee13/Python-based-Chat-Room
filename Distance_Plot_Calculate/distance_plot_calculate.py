# importing the required module
import matplotlib.pyplot as plt
from math import sqrt


def plot_points():

    # x axis values
    x1 = 10 
    x2 = 2
    # x = [1,2]
    # corresponding y axis values 
    y1 = 2
    y2 = 40
    # y = [2,4]
    distance_calculation(x1,y1,x2,y2)
    
    # plotting the points
    plt.plot(x1, x2, y1, y2, color='green', linestyle='solid', linewidth = 3, 
        marker='o', markerfacecolor='blue', markersize=12)

    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis')

    # giving a name to graph 
    plt.title('Distance Calculation')

    # Plot the graph
    plt.show()

def distance_calculation(x1,y1,x2,y2):

    x = x2 - x1
    y = y2 - y1
    distance = sqrt((x**2) + (y**2))
    print(distance)

plot_points()    
