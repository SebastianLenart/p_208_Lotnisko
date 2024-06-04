import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits import mplot3d
import matplotlib.animation as animation


class Space3D:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        self.infiwhile()
        planes = animation.FuncAnimation(self.fig, self.update_data)

        plt.show()

    def update_data(self):
        self.create_lines()
        self.settings()

    def settings(self):
        self.ax.set_xlim(0, 10000)
        self.ax.set_ylim(0, 10000)
        self.ax.set_zlim(0, 10000)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        self.ax.set_title("Airport")

    def create_lines(self):
        self.ax.plot([6000, 8000], [4000, 4000], [0])
        self.ax.plot([6000, 8000], [6000, 6000], [0])

    def add_points(self, x, y, z):
        print("XYZ", x, y, z)
        self.ax.scatter(int(x), int(y), int(z))
        plt.show()

    def infiwhile(self):
        while True:
            plt.show()



if __name__ == '__main__':
    fig = Space3D()
