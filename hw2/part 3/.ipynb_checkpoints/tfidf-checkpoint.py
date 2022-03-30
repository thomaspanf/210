import re

from collections import Counter
from math import log

#to be changed after debugging
preprocessing_prefix = 'actual_preproc_'
tfidf_prefix = 'actual_tfidf_'

def load_file_names():
    return [line.strip() for line in open('tfidf_docs.txt','r')]

def preprocessing(text):
    #1. Clean
    text = re.sub(r'http[s]{0,1}://\S+', '', text.lower()) #all text to lowercase and remove all URLs
    text = re.sub(r'[^\w\s]+', '', text) #remove non-aphamueric chars
    itemized_text = re.findall(r'\w+', text) #remove whitespaces

    #2. Remove stopwords
    stopwords =  [line.strip() for line in open('stopwords.txt','r')]
    itemized_text = list(filter(lambda word: word not in stopwords, itemized_text))

    #3. Stemming and Lemmatization

    #process word by word and then join by single whitespace
    itemized_text = [re.sub(r'ing$|ly$|ment$', '', word) for word in itemized_text]
    text = ' '.join(itemized_text)

    return text, itemized_text

def main():
    doc_count = 0
    preprocessed_filenames = []
    filename_term = []

    for filename in load_file_names():
        with open(filename, 'r') as f:
            text = f.read()
        text, itemized_text = preprocessing(text)
        filename_term = filename_term + [(filename, term) for term in set(itemized_text)] #prepare for IDF calculation
        with open(preprocessing_prefix+filename, 'w') as f:
            f.write(text)
        doc_count +=1
        preprocessed_filenames.append(preprocessing_prefix+filename)

    doc_counts_of_term_appearance = Counter([element[1] for element in filename_term]) #if more than 1 then it must be from different document

    for filename in preprocessed_filenames:
        with open(filename, 'r') as f:
                text = f.read()

        term_counts = Counter(text.split(' ')).items()

        #count freq against its own total word count
        tfs = [(term_count[0], term_count[1]/len(text.split(' '))) for term_count in term_counts]

        #calculate idf by retireving doc_counts_of_term_appearance of this term
        idfs = [(term_count[0], log(doc_count/doc_counts_of_term_appearance[term_count[0]])+1) for term_count in term_counts]

        #generate product from tf and idf lists, ordered by negative tf-idfs(DESC) and ascending term
        tf_idfs = sorted([(tf[0], round(tf[1]*idf[1], 2)) for tf in tfs for idf in idfs if tf[0] == idf[0]], key=lambda pair: (pair[1]*-1, pair[0]))

        with open(filename.replace(preprocessing_prefix, tfidf_prefix), 'w') as f:
                f.write('[(')
                f.write('), ('.join(['\''+tf_idf[0]+'\', ' + str(tf_idf[1]) for tf_idf in tf_idfs[:5]]))
                f.write(')]')

main()

