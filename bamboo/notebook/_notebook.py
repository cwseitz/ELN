from ..db import connect
from ..objects import Canvas
from ..plots import *
import os; import pandas as pd

def build_notebook(uri, database, output_dir=None):

	"""

	Pulls from MongoDB and builds the electronic lab notebook

	Parameters
	----------

	"""


	db = connect(uri, database)

	if not output_dir:
		dir = os.getcwd()

	exp_ids = db.experiments.distinct('exp_id')
	for exp_id in exp_ids:
		docs = db.experiments.find({'exp_id':exp_id})
		metadata = db.experiments.find_one({'exp_id':exp_id})['metadata']
		metadata = pd.DataFrame(metadata)

		#Create a lab notebook pages
		canvas = Canvas(); canvas.add_header()
		add_table(canvas.ax, metadata)
		canvas.save(os.getcwd())
