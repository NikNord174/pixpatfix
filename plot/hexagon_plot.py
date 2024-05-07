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


if __name__ == '__main__':
    ni_pathname = '/Users/nikolai/Library/CloudStorage/OneDrive-AMOLF/Desktop/Research/Results/AI_denoising/Dataset/poly-Ni/02-11-2023/CI_QI_values_for_points/CI_poly-Ni_scan1_15kV_100pA_WD8-1_bin1_sat0110_exp140ms_gain00_gut00_step3500nm_4087points_.txt',
    mapi_pathname = '/Users/nikolai/Library/CloudStorage/OneDrive-AMOLF/Desktop/Research/Results/MAPB_V-I_var/100pA/0_Lars_MAPB_scan10_25kV_100pA_sat0350_bin4_50ms_gain400_gut0_WD13-5_mag3500_500nm_5040points_.txt'
    data = np.loadtxt(
        mapi_pathname,
        unpack=True,
        skiprows=17,
        usecols=(3, 4, 6)
    )
    x = data[0]
    y = data[1]
    value = data[2]
    plot = Hexagon_Plot()
    plot.hex_plot(x, y, value, (5, 5), )
