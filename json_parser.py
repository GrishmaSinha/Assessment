##################################
#Grishma Sinha
#Code written in Python3 
#Libraries used json and argparse
##################################

import json		#library to parse json
import argparse #library to parse cli arguments

parser = argparse.ArgumentParser()
parser.add_argument("-f", action='store',type=str,nargs=1) #adding file name through -f flag
parser.add_argument('input',action='store',nargs='*',default='null') #adding inputs for extracting attributes
args=parser.parse_args()

#handling exceptions when no argument is provided
if len(args.input)==2:
	a = args.input[0]
	b = args.input[1]
elif len(args.input)==1:
	a = args.input[0]
	b = 'null'
else:
	a='null'
	b='null'

#opening file for reading
f = open(args.f[0],'r')

#parsing the json blob into a list
data = json.load(f)

#declaring counters for total records and matched records
k=0
j=0

#iterating through the list to match the input provided
for i in range(0,len(data)):
	for key,value in data[i].items():
		if key == a:
			k=k+1
			if b=='null':					#when no value attribute is provided, all entries are returned
				print('id: '+data[i]['id'],key+': '+value)
			elif b == value[0:len(b)]:		#matching the initial charactes for user input to the value
				j=j+1
				print('id: '+data[i]['id'],key+': ' +value)


print('Total '+str(k)+' records found.')
print('Total '+str(j)+' records matched.')


