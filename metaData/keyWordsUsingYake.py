import yake
from farasa.stemmer import FarasaStemmer
stemmer = FarasaStemmer()

kw_extractor = yake.KeywordExtractor()

def yakeKeyWords (text) :

    x = stemmer.stem(text)
    language = "ar"
    custom_kw_extractor = yake.KeywordExtractor(lan="ar", n=1, dedupLim=0.9)
    keywords = custom_kw_extractor.extract_keywords(x)
    for kw in keywords:
        print(kw)
    return keywords