import pymongo as pm
import uuid
from datetime import datetime

def connect(db_name, host, port):
	client = pm.MongoClient(host, port)
	db = client[db_name]
	return db

def get_exp_id():

	"""

	Generate a uuid for the experiment. All measurements will be labeled
	with this uuid for aggregation

	"""

	return uuid.uuid4()

def add_measurement(db, df,
					exp_id,
				    collection='experiments',
				    exp_date=None,
				    metadata=None,
				    summary=None):

	"""

	Parameters
	----------
	metadata : dict,
	 dictionary of experimental parameters e.g. exposure time
	db : Database,
	 MongoDB database object
	collection_name : str, optional
	 name of collection in db to insert meta_dict


	"""

	df.reset_index(inplace=True)
	data = df.to_dict('records')
	collection = db[collection]
	dict = metadata
	if not exp_date:
		now = datetime.now()
		date = now.strftime("%Y%m%d")
		date = date[2:]

	dict['exp_id'] = exp_id
	dict['date'] = exp_date
	dict['data'] = data
	dict['summary'] = summary
	collection.insert_one(dict)
