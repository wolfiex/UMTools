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
files = sorted(files,key=lambda x: -modi[x] )

for i,key in enumerate(files):
	print (i,key.split('/')[-2])

selection = files[int(input('\nSelect run to check Paths:\n'))]
print(selection)

#selection = '/home/d02/dellis/roses/u-ca218/'

# get lines from grep
lines = os.popen('grep -inr "[\\"\']\s*/[^\\"\']*\'" %s*'%selection).readlines()
# get actual links 
lines = [re.findall("[\"'](\s*/[^\"']*)",i)[0] for i in lines]
# filter out links with 
lines = set(filter(lambda x: re.match(r'/[^/]+/',x), lines))


''' 
Having obtained all our paths we check if we have permissions to read them
'''

groups = os.popen('groups').read().split()
groups.append(os.popen('echo $USER').read().strip())

print 'Number of links: ' , len(lines)

sucessful = []
failed = []

for i in lines:
    fail = True    
    if 'No such file' in os.popen('ls '+i + ' 2>&1').read():
	fail = True
    else:
	permissions = os.popen('namei -o -v '+i).readlines()#-l
	match = filter(lambda x: x[0] not in ['d','f'] ,permissions)
	if len(match) == 0: match = permissions[-1]
	print match, i
	
	
	for j in match[0].split()[1:-1]:
		# if we have user permission
		if j in groups: 
			fail = False
			break
			
			
	if fail: 
		failed.append(i)
	else:
		sucessful.append(i)
		
run = selection.split('/')[-1]
fn = '%spathtest_%s.txt'%(selection.split('roses')[0],run)
print fn
with open(fn,'w') as f:
	f.write('Path Analysis for '+run+'\n\n\n')
	f.write( 'Sucessful finds:\n\n')
	for k in sucessful:
		f.write(k+'\n')
		
		
	f.write( '\n\n-----------FAILED-----------\n\n')
	for k in failed:
		f.write(k+'\n\n')
		f.write(os.popen('grep -inr "%s" %s'%(k,selection).read()))
		f.write('\n\n')
			
			
print 'File written at ', fn
		
'''
testing 

rm pathsNpermissions.py ; wget https://raw.githubusercontent.com/wolfiex/UMTools/main/lib/pathsNpermissions.py && python pathsNpermissions.py 
'''
		
		



