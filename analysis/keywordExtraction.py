# https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c
import yake
from rake_nltk import Rake
import nltk

class KeyWordExtractor:
    
    def __init__(self, text):
        self.text = text

    def setText(self, text):
        self.text = text
    
    def yakeExtract(self, max_ngram =3, max_keywords=20, dedup_thresh = 0.9):
        language = "en"
        max_ngram_size = max_ngram
        deduplication_threshold = dedup_thresh
        numOfKeywords = max_keywords
        custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
        keywords = custom_kw_extractor.extract_keywords(self.text)

        return keywords


    def rakeExtract(self):
        nltk.download('stopwords')
        nltk.download('punkt')

        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(text)
        keywords = rake_nltk_var.get_ranked_phrases()

        return keywords
    

if __name__ == "__main__":

    # testing
    text = """spaCy is an open-source software library for advanced natural language processing, 
            written in the programming languages Python and Cython. The library is published under the MIT license
            and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
    extractor = KeyWordExtractor(text)

    #! YAKE
    print("-------- YAKE --------")
    keywords = extractor.yakeExtract();
    for kw in keywords:
        print(kw)

    #! RAKE
    print("-------- RAKE --------")
    keywords = extractor.rakeExtract();
    for kw in keywords:
        print(kw)
