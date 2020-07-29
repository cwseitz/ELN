import matplotlib.pyplot as plt
import numpy as np

def plt2array(fig):
    """
    Save matplotlib.pyplot figure to numpy rgbndarray.

    Parameters
    ----------
    fig : object
        matplotlib figure object.

    Returns
    -------
    rgb_array_rgb: ndarray
        3d ndarray represting the figure

    Examples
    --------

    """

    fig.canvas.draw()
    buf = fig.canvas.tostring_rgb()
    ncols, nrows = fig.canvas.get_width_height()
    rgb_array_rgb = np.frombuffer(buf, dtype=np.uint8).reshape(nrows, ncols, 3)

    return rgb_array_rgb
