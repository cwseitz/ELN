Managing the bamboo notebook
============================

Below is an example showing how to query a mongoDB instance and build
a notebook

.. code:: python

  import os
  import pandas as pd
  import matplotlib.pyplot as plt

  from bamboo.plots import *
  from bamboo.objects import Canvas
  from bamboo.util import format_ax
  from bamboo.db import connect
  from bamboo.notebook import *

  db = connect('mongodb://127.0.0.1:27017', database='testdb')
  cwd = os.getcwd()

  def page1(dir):

    author = 'Clayton Seitz'; title = 'Data Analysis'
    template = get_template_2()
    canvas = Canvas(template=template, author=author, title=title)
    query = db.experiments.find_one()
    blobs_df = pd.DataFrame(query['data'])

    add_mean_msd(canvas.ax[0], blobs_df,
          pixel_size=1,
          frame_rate=1,
          divide_num=5,
          RGBA_alpha=0.5
          )
    canvas.ax[0].legend(loc='upper left', frameon=False, fontsize=13)

    add_D_hist(canvas.ax[1], blobs_df,
          RGBA_alpha=0.5)

    canvas.ax[1].legend(loc='upper right', frameon=False, fontsize=13)

    add_alpha_hist(canvas.ax[2], blobs_df,
             RGBA_alpha=0.5)

    canvas.ax[2].legend(loc='upper right', frameon=False, fontsize=13)

    canvas.save(cwd + '/page1.pdf')

  def page2(dir):

    author = 'Clayton Seitz'; title = 'Data Analysis'
    template = get_template_2()
    canvas = Canvas(template=template, author=author, title=title)
    query = db.experiments.find_one()
    blobs_df = pd.DataFrame(query['data'])

    add_mean_msd(canvas.ax[0], blobs_df,
          pixel_size=1,
          frame_rate=1,
          divide_num=5,
          RGBA_alpha=0.5
          )
    canvas.ax[0].legend(loc='upper left', frameon=False, fontsize=13)

    add_D_hist(canvas.ax[1], blobs_df,
          RGBA_alpha=0.5)

    canvas.ax[1].legend(loc='upper right', frameon=False, fontsize=13)

    add_alpha_hist(canvas.ax[2], blobs_df,
             RGBA_alpha=0.5)

    canvas.ax[2].legend(loc='upper right', frameon=False, fontsize=13)

    #Save as pdf
    canvas.save(cwd + '/page2.pdf')

  def page3(dir):

    author = 'Clayton Seitz'; title = 'Data Analysis'
    template = get_template_2()
    canvas = Canvas(template=template, author=author, title=title)
    query = db.experiments.find_one()
    blobs_df = pd.DataFrame(query['data'])

    add_mean_msd(canvas.ax[0], blobs_df,
          pixel_size=1,
          frame_rate=1,
          divide_num=5,
          RGBA_alpha=0.5
          )
    canvas.ax[0].legend(loc='upper left', frameon=False, fontsize=13)

    add_D_hist(canvas.ax[1], blobs_df,
          RGBA_alpha=0.5)

    canvas.ax[1].legend(loc='upper right', frameon=False, fontsize=13)

    add_alpha_hist(canvas.ax[2], blobs_df,
             RGBA_alpha=0.5)

    canvas.ax[2].legend(loc='upper right', frameon=False, fontsize=13)

    #Save as pdf
    canvas.save(cwd + '/page3.pdf')


  page1(cwd)
  page2(cwd)
  page3(cwd)

  pdfs = ['page1.pdf',
      'page2.pdf',
      'page3.pdf']

  build_notebook(cwd, pdfs)
