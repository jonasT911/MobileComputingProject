import csv


def csvToDict(fileName):
    reviewList=[]
    with open(fileName, newline='') as csvfile:

        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

        skipFirst=True
        for row in spamreader:
            if(not skipFirst):
                 thisdict =    {
                      'score': row[0],
                      'at': row[1],
                      'content': row[2]
                    }
                 reviewList.append(thisdict)
            skipFirst=False
            
    return reviewList
    
    
def groupByDate(fileName,buckets):
    reviewList = csvToDict(fileName)
