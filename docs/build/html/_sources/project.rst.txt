Starting a bamboo project
=========================

The first step in starting a new project in bamboo involves creation of the
*project tree*. The project tree looks like this:

::

    project
    ├── data
    ├── analysis
    ├── pub
    └── notebook.pdf

As you can see, the project tree contains four main directories each
with a specific purpose. All RAW images, spreadsheets, database dumps are housed
under *data*. All analyses and analysis parameters are in *analysis*.
Do not confuse these two directories. One is dedicated for raw data only and
the other any of its transformations or extracted data. That includes image
transformations. Any powerpoint presentations or manuscripts are under
*pub*. Lastly, the lab notebook-like object notebook.pdf will aggregate
experimental metadata, raw data, and analysis to give a track record for the
project. Due process will be given to explaining how to manage the notebook.

Let's first go over how to build a new project.

.. code:: python

  from bamboo import build_new_project

  params = {

            'dir': '/path/to/parent/directory',
            'name' : 'sample_project',
            'date' : '200810',
            'storage' : 'remote',
            'naming' : 'standard'

           }

  build_new_project(params)
