import struct
import numpy as np


class File():
    header_size = 16

    def from_file(self, file_path: str, dtype: str) -> np.ndarray:
        """
        Args:
            file_path (str): Path to the file.
            dtype (str): np.uint8 for up1: N=8 or np.uint16 for up2.

        Returns:
            np.ndarray: Extracted patterns [N, 1, m, n].
        """
        with open(file_path, 'rb') as up_file:
            header = struct.unpack('4i', up_file.read(self.header_size))
            width = header[1]  # Width of patterns in pixels
            height = header[2]  # Height of patterns in pixels
            offset = header[3]  # Offset to first pattern
            pats = np.fromfile(
                up_file,
                dtype=dtype,
                offset=offset-self.header_size)
            _offset = pats.shape[0] % (height*width)
            if _offset != 0:
                pats = pats[:-_offset]
            num_pats = int(pats.shape[0] / (width * height))
        return pats.reshape(num_pats, 1, height, width)

    def to_file(
            self,
            pat_size: int,
            file_path: str,
            write_pats: np.ndarray,
            dtype: str):
        """
        Args:
            pat_size (int): Size of patterns [N, 1, m, n].
            file_path (str): Path and name for new file.
            write_pats (np.ndarray): Patterns to write.
            dtype (str): Desired type of data in 'uint8' or 'uint16' format.
        """
        if write_pats.dtype == dtype:
            with open(file_path, 'wb') as up_file:
                header = struct.pack(
                    '4i', 1, pat_size, pat_size, self.header_size)
                up_file.write(header)
                write_pats.tofile(up_file)
        else:
            print(
                'ERROR: Type of patterns ({}) does not match \
                with desired type ({}))'.format(write_pats.dtype, type))
