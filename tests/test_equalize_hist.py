import numpy as np
import pytest

from process import equalize_hist as eqhist


class TestHisgramEqualisation:

    shape = (1, 258, 258)
    img = np.random.rand(*shape)
    hist_eq = eqhist.Hist_Equalisation().hist_equalisation

    def test_hist_eq(self):
        eq_img = self.hist_eq(self.img)
        assert eq_img.shape == self.shape
        if eq_img.shape == self.shape:
            pytest.fail('something goes wrong...')
