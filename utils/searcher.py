import sys
import os

search_loc = list(sys.argv)[1]
search_terms = list(sys.argv)[2:]
print(search_terms)
search_type = None


if os.path.isdir(search_loc):
	print('is dir')
	search_type = 'folder'
elif os.path.isfile(search_loc):
	print('fil')
	search_type='file'
else:
	raise ValueError('Not file or folder')

if search_type == 'folder':
	for directory, subdirectories, files in os.walk(search_loc):
		for file in files:
			temp_loc = os.path.join(directory, file)
			if '/.' not in temp_loc:
				#print(temp_loc)
				try:
					with open(temp_loc) as f:
						read_file = f.read()
						if any(term in read_file for term in search_terms):
							print(temp_loc)
				except:
					None

else:
	with open(search_loc) as f:
		lines = f.readlines()
		for line in lines:
			for term in search_terms:
				if term in line:
					print(line)

# if search_type == 'folder':
# 	for foldir in os.listdir(search_loc):
# 		if foldir[0] != '.':
# 			print(foldir)
# 			if os.path.isdir(search_loc+'/'+foldir):
# 				print('more dir')
# 			else:
# 				print('fil')
