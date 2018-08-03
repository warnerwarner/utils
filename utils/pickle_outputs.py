'''
Holds utility functions for general usage. So far only have test functions and a function to pickle outputs so I don't forget
'''


import pickle
import os
import datetime

def time_test():
	'''
	Tests to make sure that the time output is one I was looking for
	'''
	st = datetime.datetime.now()
	print(st)
	for i in range(100090000):
		None

	print((datetime.datetime.now()-st).total_seconds())

def folder_test():
	'''
	Checks if the os.getcwd() returns the working directory of the utils folder, of the folder it was called from
	seems to return the one it was called from which is very useful
	'''
	print(os.getcwd())

def pickle_output(obj, name, folder_loc=os.getcwd()):
	'''
	Pickles an object passed to it, requires the object and a name to call it, can pass a different folder to it, but can also use the current directory as an output

	-------------------
	Arguments:
	obj: object
		The object to be pickled
	name: str
		Name of the object
	folder_loc: string
		Location of the folder for the pickled object to be saved. If none is passed, then uses the current working directory
	'''
	st = datetime.datetime.now()
	current_time = '-' + str(datetime.datetime.now())[:-7].replace(' ', '_').replace(':', '-')
	pickle.dump(obj, open(folder_loc + '\\'+name + current_time+'.pkg', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
	print('Pickled object called', name, 'took', (datetime.datetime.now()-st).total_seconds(), 'seconds to pickle. Saved in', folder_loc)