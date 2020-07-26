
=====

.. currentmodule:: bamboo.util

Formatting a matplotlib axis
----------------

.. autofunction:: format_ax

.. plot::

 import matplotlib.pyplot as plt
 import numpy as np
 from bamboo.util import format_ax

 fig, ax = plt.subplots()
 plt.show()


.. plot::

 import matplotlib.pyplot as plt
 import numpy as np
 from bamboo.util import format_ax

 fig, ax = plt.subplots()
 format_ax(ax, ax_is_box=False)
 plt.show()
