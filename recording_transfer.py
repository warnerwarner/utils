import os
import datetime
import shutil
import time

camp_loc = 'Z:\\working\\warnert\\Recordings'
local_loc = 'D:\\Recordings'
log_loc = "C:\\Users\\warnert\\Documents\\GitHub\\utils\\recording_transfer_success.txt"

camp_dirs = [i for i in os.listdir(camp_loc) if str.isdigit(i)]
local_dirs = [i for i in os.listdir(local_loc) if str.isdigit(i)]
whitelist = ['180504', '180505']
moves = {}
for i in camp_dirs:
	if i not in local_dirs and i not in whitelist:
		print(i)
		st = time.time()
		shutil.copytree(os.path.join(camp_loc, i), os.path.join(local_loc, i))
		moves[i] = time.time()-st

with open(log_loc, 'a') as f:
	for direc in moves:
		log_output = str(datetime.date.today()) + ': Moved ' + direc + ' in ' + str(moves[direc]) + '\n'
		print(log_output)
		f.write(log_output)