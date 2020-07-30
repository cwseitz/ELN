Using Canvas for PDFs
=====================

Using defaults
--------------------------------------

The simplest use-case for the Canvas object involves creating a
M x N grid of subplots. This is already built into matplotlib, so we
can just pass the dimensions of the grid and we're good to go. Also, you
can choose how to position the subplots within the 8.5 x 11 page with
the appropriate parameters.

See https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html

.. code:: python

  from bamboo.objects import Canvas
  from bamboo.util import format_ax

  author = 'Author'
  title = 'Title'

  canvas = Canvas(nrows=4, ncols=4,
                  right=0.75, bottom=0.5,
                  wspace=0.75, hspace=0.75,
                  author=author, title=title)

.. plot::

  from bamboo.objects import Canvas
  from bamboo.util import format_ax

  author = 'Author'
  title = 'Title'

  canvas = Canvas(nrows=4, ncols=4,
                  right=0.75, bottom=0.5,
                  wspace=0.75, hspace=0.75,
                  author=author, title=title)

Using a built-in template
--------------------------------------

Various custom templates are also available to save time. These can be imported
from bamboo.templates

.. code:: python

  from bamboo.templates import get_template_1
  from bamboo.objects import Canvas

  author = 'Author'
  title = 'Title'
  template = get_template_1()
  canvas = Canvas(template=template, author=author, title=title)

.. plot::

  from bamboo.templates import get_template_1
  from bamboo.objects import Canvas

  author = 'Author'
  title = 'Title'
  template = get_template_1()
  canvas = Canvas(template=template, author=author, title=title)

Defining a custom template
--------------------------------------

You can even design your own template if you'd like. To do this, pass a list
of lists of the form [x0, y0, width, height]. Each sub-list represents a subplot
and contains the coordinates of the lower left hand corner and its dimensions.

See https://matplotlib.org/3.3.0/api/_as_gen/matplotlib.axes.Axes.inset_axes.html

.. code:: python

  from bamboo.objects import Canvas

  author = 'Author'
  title = 'Title'
  template = [[0.0, 0.0, 0.2, 0.2],
       [0.3, 0.0, 0.2, 0.2],
       [0.6, 0.0, 0.2, 0.2],
       [0.0, 0.25, 0.2, 0.2],
       [0.3, 0.25, 0.2, 0.2],
       [0.6, 0.25, 0.2, 0.2]]

  canvas = Canvas(template=template, author=author, title=title)

.. plot::

  from bamboo.objects import Canvas

  author = 'Author'
  title = 'Title'
  template = [[0.0, 0.0, 0.2, 0.2],
       [0.3, 0.0, 0.2, 0.2],
       [0.6, 0.0, 0.2, 0.2],
       [0.0, 0.25, 0.2, 0.2],
       [0.3, 0.25, 0.2, 0.2],
       [0.6, 0.25, 0.2, 0.2]]

  canvas = Canvas(template=template, author=author, title=title)
