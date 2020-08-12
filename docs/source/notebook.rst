Managing the bamboo notebook
============================

The bamboo notebook is basically a much better looking and smarter version of
a paper lab notebook. It is in chronological order and is more aware of the
rest of the project than pen and paper so you don't have to be.

When you do an experiment, you generate some data, hopefully, and you want
to log how you generated it and later how you analyzed it. For the former,
we take a batch of files stored at dir, provide some experimental metadata
and where to store it and call add_data()

.. code:: python

  from bamboo.notebook import add_data

  params = {

            'project_path': '/path/to/project',
            'dir': '/path/to/files/'
            'param_file': '/path/to/param_file.txt'
            'exp_name' : 'sample_exp',
            'date' : '200810',
            'storage' : 'both',
            'rename': True,

           }

  add_data(params)

This operation will log an entry in the notebook and move data stored
at /path/to/files into /path/to/project/data and (optionally) rename all files
according to the convention specified in the project metadata.
Moving on, for the analysis portion, we provide a path to a CSV file containing
a key-value pair for each analysis parameter and the parent experiment name:

.. code:: python

  from bamboo.notebook import add_analysis

  params = {

            'project_path': '/path/to/project',
            'param_file': '/path/to/param_file.txt'
            'exp_name' : 'sample_exp',
            'date' : '200810'
            'storage' : 'both'

           }

  add_analysis(params)

This operation will also add an entry in the notebook.
By providing the experiment name for this analysis, we link these in
bamboo's backend representation of the project. Note that it is possible to
pass an array of experiment names (provided they exist) in the case that
we decided to merge some data from several experiments for a single analysis.

Next, we will try out a more advanced usage of add_analysis() that utilizes
the Canvas object to take the data we generated in our analysis, plot it, and
add those plots to a custom or default template.

.. code:: python

  from bamboo.notebook import add_analysis
  from bamboo.objects import Canvas

  author = 'Author'; exp_name = 'Experiment'
  template = [[0.0, 0.0, 0.2, 0.2],
              [0.3, 0.0, 0.2, 0.2],
              [0.6, 0.0, 0.2, 0.2],
              [0.0, 0.25, 0.2, 0.2],
              [0.3, 0.25, 0.2, 0.2],
              [0.6, 0.25, 0.2, 0.2]]

  canvas = Canvas(template=template, author=author, title=exp_name)
  canvas.set_plots([plot1, plot2, ...])

  params = {

            'project_path': '/path/to/project',
            'param_file': '/path/to/param_file.txt'
            'exp_name' : 'sample_exp',
            'date' : '200810'
            'storage' : 'both'
            'canvas' : canvas,

           }

  add_analysis(params)
