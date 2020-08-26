.. bamboo documentation master file, created by
   sphinx-quickstart on Fri Jul 24 19:08:25 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

bamboo
==================================

Below is a diagram depicting a tech setup that I have found to be incredibly
useful for rapid and organized biophysics research in python. Frequently I have found
myself reconfiguring operating systems, rewriting code, and fussing with package
management. With this setup, everything is a portable environment, there is
redundancy, software development is a breeze, and you can take advantage of a
host of fancy applications on non-linux operating systems.

.. image:: 200824_Tech-Stack.jpg

The bamboo package makes this setup possible with all the necessary APIs to
tools like rclone and mongoDB. In addition to this, it facilitates data analysis
with common biophysical metrics and an electronic lab notebook. Stay organized
my friends!

Contents
--------

.. toctree::
   :maxdepth: 1

   install
   notebook
   modules
   format_ax
   canvas
