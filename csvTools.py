import csv


def csvToDict(name):
	reviewList=[]
	with open(name, newline='') as csvfile:

	    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

	    skipFirst=True
	    for row in spamreader:
	        if(not skipFirst):
	             thisdict =	{
					  'score': row[0],
					  'at': row[1],
					  'content': row[2]
					}
	             reviewList.append(thisdict)
	        skipFirst=False
	        
	return reviewList
	
	

