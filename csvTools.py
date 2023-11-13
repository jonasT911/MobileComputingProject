import csv

def findNewestAndOldest(reviewDict):
	
	max =reviewDict[0]['Date']
	min =reviewDict[0]['Date']
	for row in reviewDict:
		
		if(row['Date']<min):
			min = row['Date']
		if(row['Date']>max):
			max = row['Date']
	print("Max = "+str(max)+" Min = "+str(min))
	return max , min

def csvToDict(fileName,apple = True):
	reviewList=[]
  
	spamreader = csv.reader(fileName, delimiter=',', quotechar='|')

	skipFirst=True
	for row in spamreader:
		if(not skipFirst):
			if(not apple):
				thisdict =	{
					'score': row[0],
					'at': row[1],
					'content': row[2]
					}
			else:
				thisdict =	{
					'Score': row[0],
					'Date': row[1],
					'Content': row[2],
					'Title': row[3]

					}
			reviewList.append(thisdict)
		skipFirst=False
			
	return reviewList
	
	
	
def groupByDate(fileName,buckets):
	reviewList = csvToDict(fileName)


outputFolder = 'outputs_Apple'
fileNameTest='cards-and-castles'
with open(str(outputFolder)+"/"+str(fileNameTest)+'.csv', 'r', newline='', encoding="utf-8") as file:
	out = csvToDict(file)
	
	findNewestAndOldest(out)