from app_store_scraper import AppStore
import os
import sys
import csv
import time

#minecraft = AppStore(country="nz", app_name="minecraft")
#minecraft.review(how_many=20)

#print(minecraft.reviews)
#print(minecraft.reviews_count)


outputFolder = "outputs_Final"

numReviews=2000

if not os.path.exists(outputFolder):
	os.mkdir(outputFolder)

if(len(sys.argv)==1):
	print("Using default")
	apps=['minecraft']
else:
	if(sys.argv[1].isdigit()):
		numReviews = int(sys.argv[1])
		apps=sys.argv[2:]
	else:
		apps=sys.argv[1:]
	

	
for appAddr in apps:
	try:
		print("Fetching reviews for "+str(appAddr))
		
		reviewsPulled=0
		result = AppStore(country="us", app_name=appAddr)
		with open(str(outputFolder)+"/"+str(appAddr)+'.csv', 'w', newline='', encoding="utf-8") as file:
			while(reviewsPulled<numReviews):
				result.review(how_many=100)
				time.sleep(1)
				writer = csv.writer(file)
				if(reviewsPulled==0):
					field = ["Score", "Date", "Content","Title"]
					writer.writerow(field)
				for rev in result.reviews:
					
					#Removes line breaks from title and review to avoid processing errors
					writer.writerow([rev['rating'], rev['date'],rev['review'].replace("\n", " "),rev['title'].replace("\n", " ")])
				reviewsPulled+=100
   
		
	except Exception as e:
		print("ERROR")
		print(e)