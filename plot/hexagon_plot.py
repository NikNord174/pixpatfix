import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon


class Hexagon_Plot():

    def hex_plot(self, x: np.ndarray, y: np.ndarray, value: np.ndarray,
                 figsize: tuple = (10, 10), hex_size: float = 2) -> None:
        """Plots 2D graph of values like CI or IQ in hexagonal grid.
        Args:
            x (np.ndarray): x coordinates of points.
            y (np.ndarray): y coordinates of points.
            value (np.ndarray): The key value (CI, Iq etc).
            figsize (tuple): Size of graph. Should be (width, height). Defaults to (10, 10).
            hex_size (float): Size of hexagons in graph. Defaults to 2.
        """
        fig, ax = plt.subplots(figsize=figsize)
        value_norm = value / value.max()
        for x_val, y_val, c_val in zip(x, y, value_norm):
            hex = RegularPolygon(
                (x_val, y_val), radius=hex_size/6., numVertices=6,
                facecolor=(c_val, c_val, c_val))
            ax.add_patch(hex)
        ax.plot()
        plt.show()
