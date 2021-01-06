#!/opt/python/gnu/2.7.9/bin/python

'''
UM debugging tool

Find the paths in a rose suite and check that the current user has permissions to access them
'''

import re, os, glob

home = os.environ['HOME']
files = glob.glob(home+'/roses/u-*/')
print(home,len(files),files)
modi = dict([[i,os.path.getmtime(i)] for i in files])
print(modi)
files = sorted(files,key=lambda x: -modi[x] )

for i,key in enumerate(files):
	try: tlog  = tuple(open(key+'/trac.log'))[3].split('||')[2]
	except IOError: tlog = '--------------------'	
	print (i,key.split('/')[-2],tlog)

selection = files[int(input('\nSelect run to transfer:\n'))]
print(selection)



#grep -inr "[\"']\s*/[^\"']*" *
