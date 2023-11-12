from app_store_scraper import AppStore
import os
import sys
import csv
import datetime


#print(minecraft.reviews)
#print(minecraft.reviews_count)


outputFolder = "outputs_Apple"


if not os.path.exists(outputFolder):
	os.mkdir(outputFolder)

if(len(sys.argv)==1):
	print("Using default")
	apps=['minecraft']
else:
	apps=sys.argv[1:]
	

for appAddr in apps:
	try:
		print("Fetching reviews for "+str(appAddr))
		lines= 0
		result = AppStore(country="us", app_name=appAddr)
		while(lines < 10):
			
			result.review(how_many=20)
			

			with open(str(outputFolder)+"/"+str(appAddr)+'.csv', 'w', newline='', encoding="utf-8") as file:
				writer = csv.writer(file)
				field = ["Score", "Date", "Content","Title"]
				
				writer.writerow(field)
				for rev in result.reviews:
					
					#Removes line breaks from title and review to avoid processing errors
					if(rev['date']<datetime.datetime(2017, 5, 18, 10, 59, 42, 518352)):
						writer.writerow([rev['rating'], rev['date'],rev['review'].replace("\n", " "),rev['title'].replace("\n", " ")])
						lines+=1
			
	except Exception as e:
		print("ERROR")
		print(e)