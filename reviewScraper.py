import csv
from google_play_scraper import Sort, reviews, app
import os
import sys

outputFolder = "outputs"

if not os.path.exists(outputFolder):
    os.mkdir(outputFolder)

if(len(sys.argv)==1):
    print("Using default")
    apps=['com.fantome.penguinisle','com.nianticlabs.pokemongo','com.instagram.android','com.einnovation.temu','com.zhiliaoapp.musically']
else:
    apps=sys.argv[1:]

for appAddr in apps:
    print("Fetching reviews for "+str(appAddr))
    try:
        result, continuation_token = reviews(
            appAddr,
            lang='en', # defaults to 'en'
            country='us', # defaults to 'us'
            sort=Sort.NEWEST, # defaults to Sort.NEWEST
            count=200, # defaults to 100
            filter_score_with=None # defaults to None(means all score)
        )

        # If you pass `continuation_token` as an argument to the reviews function at this point,
        # it will crawl the items after 3 review items.

    #    result, _ = reviews(
    #        appAddr,
    #        continuation_token=continuation_token # defaults to None(load from the beginning)
    #    )



        appDescription = app(
            appAddr,
            lang='en', # defaults to 'en'
            country='us' # defaults to 'us'
        )


        with open(str(outputFolder)+"/"+str(appDescription['title'])+'.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            field = ["Score", "Date", "Content"]
            
            writer.writerow(field)
            for rev in result:
                writer.writerow([rev['score'], rev['at'],rev['content']])
    except Exception as e:
        print("ERROR")
        print(e)
        
