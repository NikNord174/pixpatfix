import numpy as np
import cv2 as cv
from skimage.morphology import disk
from skimage.filters import rank


class Hist_Equalisation():
    """Increases the global contrast of images:
    https://en.wikipedia.org/wiki/Histogram_equalization"""

    def hist_equalisation(self, img: np.ndarray) -> np.ndarray:
        """Regular histagram normalisation.

        Args:
            img (np.ndarray): Image to normalise. Shape (1, m, n).

        Returns:
            np.ndarray: Normalised image with shape (1, m, n)
        """
        return cv.equalizeHist(img[0]).reshape(*img.shape)

    def ahe(self, img: np.ndarray, radius: int = 10) -> np.ndarray:
        """Adaptive histogram normalisation.

        Args:
            img (np.ndarray): Image to normalise. Shape (1, m, n).
            radius (int, optional): The range of neighbouring pixels taking as
                a kernel. Defaults to 10.

        Returns:
            np.ndarray: Normalised image with shape (1, m, n)
        """
        footprint = disk(radius)
        return rank.equalize(img[0], footprint).reshape(*img.shape)

    def clahe(
            self, img: np.ndarray, clipLimit: int = 2,
            tileGridSize: tuple = (8, 8)) -> np.ndarray:
        """Contrast Limited Adaptive Histogram Normalisation.

        Args:
            img (np.ndarray): Image to normalise. Shape (1, m, n).
            clipLimit (int, optional): Sets the threshold for contrast
                limiting. Defaults to 2.
            tileGridSize (tuple, optional): Sets the size of grid for histogram
                equalization. Input image will be divided into equally sized
                rectangular tiles. Defaults to (8, 8).

        Returns:
            np.ndarray: Normalised image with shape (1, m, n)
        """
        clahe = cv.createCLAHE(clipLimit, tileGridSize)
        return clahe.apply(img[0]).reshape(*img.shape)
