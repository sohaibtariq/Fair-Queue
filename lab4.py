import csv
import json

data = []

with open('Academic _Schedule.csv', 'rb') as f:
	reader = csv.reader(f)
	count = 0
	
	for row in reader:
		if count < 1:
			count += 1
			continue

		startDate, endDate, activity = row
		data.append(row)


#print json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))


#priorities={}
#for activity in data:
#    priorities[activity]=0


#priorities[priorities.items()[0][0]]=12 
#priorities[priorities.items()[1][0]]=15
#priorities[priorities.items()[2][0]]=19
#priorities[priorities.items()[3][0]]=16
#priorities[priorities.items()[4][0]]=15
#priorities[priorities.items()[5][0]]=5
#priorities[priorities.items()[6][0]]=10
#priorities[priorities.items()[7][0]]=15
#priorities[priorities.items()[8][0]]=18
#priorities[priorities.items()[9][0]]=5
#priorities[priorities.items()[10][0]]=18
#priorities[priorities.items()[11][0]]=19
#priorities[priorities.items()[12][0]]=10
#priorities[priorities.items()[13][0]]=10
#priorities[priorities.items()[14][0]]=19
#priorities[priorities.items()[15][0]]=15
#priorities[priorities.items()[16][0]]=10
#priorities[priorities.items()[17][0]]=17
#priorities[priorities.items()[18][0]]=15
#priorities[priorities.items()[19][0]]=19          
          
#""""
#- add all priorities for a slot
#- divide individual priority by total  
#- assign percentage bandwidth equal to the percentage priority

#"""
           