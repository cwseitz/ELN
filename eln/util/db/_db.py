import pymongo as pm
import uuid
import rclone
import subprocess
import os
import shutil
from datetime import datetime

#Database functions

def connect(uri, database):

	"""

	Connect to a mongoDB instance

	Parameters
	----------
	uri : str,
	 uri to mongoDB instance
	database : str,
	 name of the database to connect to

	"""

	client = pm.MongoClient(uri)
	db = client[database]
	return db

def init_db(uri, project_name):

	"""

	Initialize a new project database

	Parameters
	----------
	uri : str,
	 uri to mongoDB instance
	project_name : str,
	 desired name of the project

	"""

	db = connect(uri, project_name)
	db['experiments'].insert_one({})
	db['protocols'].insert_one({})
	db['notes'].insert_one({})
	print('Successfully created database: %s' % (project_name))
	print(db.list_collection_names())

def backup_db(db, dir, dest=None, flags=[]):

	"""

	Dump a database to disk and copy to remote destination

	Parameters
	----------
	db : object,
	  pymongo mongoDB instance
	dir : str,
	 directory to output the database dump

	"""

	#dump to disk, compress
	args = ['--gzip', '-d' + db, '-o' + dir]
	cmd = ['mongodump'] + args
	code = subprocess.call(cmd)

	#change directory name
	now = datetime.now().strftime('%Y%m%d_%H:%M:%S')[2:]
	old_dir = dir + '/' + db
	dump_fldr = '/' + str(now) + '_' + db + '_dump'
	new_dir = dir + dump_fldr
	os.rename(old_dir, new_dir)

	#copy to remote
	if not dest:
		dest = 'ucbox:/dump' + dump_fldr

	print('Copying to %s' %(dest))
	rclone_copy(new_dir, dest, flags=flags)

def restore_db(db_name, path_to_dumps='ucbox:/dump'):

	"""

	Restores a database from a specified restore point. Database
	dumps are assumed to be .gz zipped files

	Parameters
	----------
	db_name : object,
	  name to give the restored database
	path_to_dumps : str,
	 directory containing database dumps

	"""

	#get restore point
	list_restore_points(dest=path_to_dumps)
	restore_point = input("Specify restore point:\n")
	source = path_to_dumps + '/' + restore_point

	cwd = os.getcwd()
	dest = cwd + '/tmp'

	if os.path.exists(dest):
		print('/tmp directory already exists!')
		return
	else:
		os.mkdir(dest)

	print('Copying restore : %s ...' % (restore_point))
	rclone_copy(source, dest)

	#restore
	print('Restoring database...')
	args = ['--gzip', '--db='+db_name, dest]
	cmd = ['mongorestore'] + args
	code = subprocess.call(cmd)

	#cleanup
	shutil.rmtree(dest)

def list_restore_points(dest='ucbox:/dump'):

	"""

	List the available database restore points

	Parameters
	----------
	dest : str,
	  remote destination

	"""

	rclone_lsd(dest=[dest])

#Collection functions

def get_uuid():

	"""

	Generate a uuid

	"""

	return uuid.uuid4()

def add_tabular_data(db, df,
					 collection='experiments',
					 date=None,
					 parameters=None,
					 summary=None):

	"""

	Parameters
	----------
	db : str,
	 Name of the mongodb Database
	df : DataFrame,
	 DataFrame containing tabular data
	collection : str, optional
	 name of collection in db to insert
	parameters : DataFrame, optional
	 DataFrame of experimental parameters
	summary : str, optional
	 summary of the tabular data

	"""

	df.reset_index(inplace=True)

	dict = {}
	if parameters is not None:
		parameters.reset_index(inplace=True)
		parameters = parameters.to_dict('records')
		dict['parameters'] = parameters

	data = df.to_dict('records')
	collection = db[collection]

	if not date:
		now = datetime.now()
		date = now.strftime("%Y%m%d")
		date = date[2:]

	dict['id'] = get_uuid()
	dict['date'] = date
	dict['data'] = data
	dict['summary'] = summary
	collection.insert_one(dict)

def add_notes(path):

	"""

	Add a .txt file containing notes to the database

	Parameters
	----------
	path : str,
	 Path to .txt file contain the notes

	"""

	file = open(path)
	text = file.read(); dict = {}
	dict['text'] = text
	collection.insert_one(dict)

#Rclone wrappers

def rclone_lsd(dest=['ucbox:/']):

	"""

	List directories at the specified remote destination

	Parameters
	----------
	dest : str,
	  remote destination


	"""

	flags = ['lsd'] + dest
	cmd = ['rclone'] + flags
	code = subprocess.call(cmd)

def rclone_copy(source, dest, flags=['--no-traverse']):

	"""

	Copy files from source to destination

	Parameters
	----------
	dest : str,
	  remote destination

	"""

	flags = ['copy'] + [source, dest]
	cmd = ['rclone'] + flags
	code = subprocess.call(cmd)
