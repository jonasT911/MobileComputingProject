from keywordExtraction import KeyWordExtractor

def getTopKeywords(data_set_file):
    # Main analysis run --- will use pandas in the actual analysis

    f = open(data_set_file, "r")
    raw_reviews = f.readlines()
    raw_reviews.pop(0) # remove head
    extractor = KeyWordExtractor("")

    keywords_count = {}
    for review in raw_reviews:
        review = review.strip()
        if not len(review):
            continue
        #reviewId,content,score,thumbsUpCount,reviewCreatedVersion,at,replyContent,repliedAt,predicted_category,sentiment,appVersion
        try:
            sections = review.split(",")
            review_body = sections[1]
            extractor.setText(review_body)
            keywords = extractor.yakeExtract()
        except:
            continue

        for kw, score in keywords:
            if kw in keywords_count:
                keywords_count[kw] += 1
            else:
                keywords_count[kw] = 1
    
    print("...Sorting")
    tuples = zip(keywords_count.keys(), keywords_count.values())
    sorted_by_second = sorted(tuples, reverse=True, key=lambda tup: tup[1])

    # for kw, count in keywords_count.items():
    #     if count > 20: print(kw, ":", count)
    for i in range(0, 100):
        print(sorted_by_second[i])
    
    print("... Manually checking interesting terms")
    # some manual checks
    if "privacy" in keywords_count:
        print("privacy", keywords_count["privacy"])

    if "accessibility" in keywords_count:
        print("accessibility", keywords_count["accessibility"])

    if "scam" in keywords_count:
        print("scam", keywords_count["scam"])

    if "money" in keywords_count:
        print("money", keywords_count["money"])

    if "ui" in keywords_count:
        print("ui", keywords_count["ui"])


if __name__ == "__main__":
    data_set_file = "toy_dataset.csv"
    getTopKeywords(data_set_file)