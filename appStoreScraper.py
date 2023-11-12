from app_store_scraper import AppStore
import os
import sys
import csv

minecraft = AppStore(country="nz", app_name="minecraft")
minecraft.review(how_many=20)

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
        

        result = AppStore(country="us", app_name=appAddr)
        result.review(how_many=200)
        

        with open(str(outputFolder)+"/"+str(appAddr)+'.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            field = ["Score", "Date", "Content","Title"]
            
            writer.writerow(field)
            for rev in result.reviews:
                
                writer.writerow([rev['rating'], rev['date'],rev['review'],rev['title']])
   
        
    except Exception as e:
        print("ERROR")
        print(e)