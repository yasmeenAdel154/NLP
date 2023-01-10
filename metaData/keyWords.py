import os
import re
# pip install gensim
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

np.random.seed(400)
import nltk
nltk.download('wordnet')
path = "E:\\computers\\level 4\\semester 1\\selected 3\\project\\arabiya\\Test"
print(path)
# Change the directory
os.chdir(path)
trainFolders =  os.listdir()
listOfDocs = [] # contain all docs
topicCounter = 1
for folder in os.listdir():
    path2 = path + "\\" + folder
    os.chdir(path2)
    filesOfFolder = os.listdir()
    for file in os.listdir() :
        with open(file, "r", encoding='utf-8') as data:
            fileData = data.read()
            listOfDocs.append(re.search(r'Body\n(.*?)\n', fileData ).group(1))
            #print(re.search(r'Body\n(.*?)\n', fileData ).group(1))
    print("topic num : " + str(topicCounter) + " is done ")
    topicCounter = topicCounter + 1

#pre processing

def lemmatize_stemming(text):
    from nltk.stem.isri import ISRIStemmer
    #print(ISRIStemmer().suf32(text))
    return ISRIStemmer().suf32(text)

from farasa.stemmer import FarasaStemmer
stemmer = FarasaStemmer()
# Tokenize and lemmatize
def preprocess(text):
    result = ""
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            #result.append(lemmatize_stemming(token))
            result+=lemmatize_stemming(token) + " "
    #result = stemmer.stem(result)
    return result

def preprocessing2 (text) :


    x = lemmatize_stemming(text)
    #x = stemmer.stem(x)
    #print("sssss"+x)
    return x
'''
Preview a document after preprocessing

document_num = 50
doc_sample = "ياسمين بتحب محمد عادل و باباها عادل و ابتسام و يارا و صحابها"

print("Original document: ")
words = []
for word in doc_sample.split(' '):
    words.append(word)
print(words)
print("\n\nTokenized and lemmatized document: ")
print(preprocess(doc_sample))
'''
processed_docs = [] # docs
counter = 0
for doc in listOfDocs:
    counter+=1
    if (counter%100==0) :
        print( str(counter) + " is done" )
    processed_docs.append(preprocess(doc))
#print ( processed_docs [1][0:] )
'''
docs = []
for doc in processed_docs :
    for word in doc :
        docs.append(word)
print("gg"+docs[1][0:103])
'''
#CountVectorizer to create a vocabulary and generate word counts

from sklearn.feature_extraction.text import CountVectorizer
#docs = docs.tolist()
#create a vocabulary of words,
cv=CountVectorizer(max_df=0.95,         # ignore words that appear in 95% of documents
                   max_features=10000,  # the size of the vocabulary
                   ngram_range=(1,3)    # vocabulary contains single words, bigrams, trigrams
                  )
word_count_vector=cv.fit_transform(processed_docs)

#TfidfTransformer to Compute Inverse Document Frequency (IDF)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)


def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""

    # use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    for idx, score in sorted_items:
        fname = feature_names[idx]

        # keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    # create a tuples of feature,score
    # results = zip(feature_vals,score_vals)
    results = {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]] = score_vals[idx]

    return results


# get feature names
feature_names = cv.get_feature_names()
#print(feature_names )

def get_keywords(idx, docs):
    # generate tf-idf for the given document
    tf_idf_vector = tfidf_transformer.transform(cv.transform([docs[idx]]))

    # sort the tf-idf vectors by descending order of scores
    sorted_items = sort_coo(tf_idf_vector.tocoo())

    # extract only the top n; n here is 10
    keywords = extract_topn_from_vector(feature_names, sorted_items, 10)

    return keywords

#from txt
def get_keywordsFromText(text):
    # generate tf-idf for the given document
    text = preprocess(text)
    tf_idf_vector = tfidf_transformer.transform(cv.transform([text]))

    # sort the tf-idf vectors by descending order of scores
    sorted_items = sort_coo(tf_idf_vector.tocoo())

    # extract only the top n; n here is 10
    keywords = extract_topn_from_vector(feature_names, sorted_items, 10)

    return keywords




def print_results( keywords):
    # now print the results
    #print("\n=====Title=====")
    #print(df['title'][idx])
    #print("\n=====Abstract=====")
    #print(df['abstract'][idx])
    print("\n===Keywords===")
    for k in keywords:
        print(k, keywords[k])
"""
idx=600
keywords=get_keywords(idx, processed_docs)
print_results(keywords)

"""

'''
Preview 'processed_docs'
'''


'''
Create a dictionary from 'processed_docs' containing the number of times a word appears 
in the training set using gensim.corpora.Dictionary and call it 'dictionary'
'''
'''
dictionary = gensim.corpora.Dictionary(processed_docs)


Checking dictionary created

count = 0
for k, v in dictionary.iteritems():
    print(k, v)
    count += 1
    if count > 10:
        break


OPTIONAL STEP
Remove very rare and very common words:

- words appearing less than 15 times
- words appearing in more than 10% of all documents
'''
#dictionary.filter_extremes(no_below=15, no_above=0.1, keep_n= 100000)

'''
Create the Bag-of-words model for each document i.e for each document we create a dictionary reporting how many
words and how many times those words appear. Save this to 'bow_corpus'

bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]


Preview BOW for our sample preprocessed document

document_num = 20
bow_doc_x = bow_corpus[document_num]

for i in range(len(bow_doc_x)):
    print("Word {} (\"{}\") appears {} time.".format(bow_doc_x[i][0],
                                                     dictionary[bow_doc_x[i][0]],
                                                     bow_doc_x[i][1]))
'''