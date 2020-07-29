Formatting the axis
===================

.. currentmodule:: bamboo.util

.. autofunction:: format_ax

Example
------------------

.. code:: python

  import matplotlib.pyplot as plt

  fig, ax = plt.subplots()
  plt.show()

.. plot::

 import matplotlib.pyplot as plt
 from bamboo.util import format_ax

 fig, ax = plt.subplots()
 plt.show()

.. code:: python

 import matplotlib.pyplot as plt
 from bamboo.util import format_ax

 fig, ax = plt.subplots()
 plt.show()

.. plot::

 import matplotlib.pyplot as plt
 from bamboo.util import format_ax

 fig, ax = plt.subplots()
 format_ax(ax, ax_is_box=False)
 plt.show()
