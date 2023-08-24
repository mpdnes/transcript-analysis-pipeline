import matplotlib.pyplot as plt
import numpy
from nltk import *
import nltk
# nltk.download('stopwords')
#nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import docxpy
import contractions
import re
from sklearn.feature_extraction.text import \
    ENGLISH_STOP_WORDS as sklearn_stop_words
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from os import system


#RegEx expression that says, give me words, but not spaces! Used to tokenize
#transcript further down


#TODO: Figure out how to separate things into a categorical dictionary.
#       Dict within a dict?
import os
import subprocess


def directctory_inspector(root_dir):
    """
    This function returns a dictionary of all words and frequencies
    :param : rootdir : is the directory to search for transcripts
    :return: a list of files to be processed somewhere else, and a list of files that need to be changed
    """
    docs_to_be_changed = []
    docx_list = []
    dir_list = []

    for subdir, dirs, files in os.walk(root_dir):

        for folders in dirs:
            dir_list.append(folders)

        for docx in files:
            if docx == '.DS_Store':
                if docx.startswith('.'):
                    continue

            if not docx.endswith("docx"):
                docs_to_be_changed.append(subdir + "/" + docx)
                continue

            if docx.endswith("docx"):
                if len(docx) == 11:
                    key_path = subdir + "/" + docx
                    docx_list.append(key_path)

    num_of_files = len(dir_list)

    return [docs_to_be_changed,docx_list,dir_list,num_of_files]



def check_csv_file(common_comparison_csv_file_name, target_csv_file_name):
    """

    :param common_comparison_csv_file_name:
    :param target_csv_file_name:
    :return: returns if these files exist
    """
    #Check to see if the common basis of comparison csv file exists
    result_comparison_csv = os.path.isfile(common_comparison_csv_file_name)

    #Check to see if the csv file for targeted words exists
    result_target_csv = os.path.isfile(target_csv_file_name)

    return result_comparison_csv,result_target_csv

#Transcript text file
def read_docx_files(docs_to_be_changed, docx_to_be_read,dirs_list):
    tokenizer_unigram = RegexpTokenizer(r'([A-Za-z]+)+\s')
    tokenizer_sent = RegexpTokenizer(r'(?<=[^A-Z].[.?!]) +(?=[A-Z])')
    list_of_words_with_pos_tags = []
    docs_read = 0
    list_of_files_processed = []
    list_of_dirs = dirs_list

    #Read document using docxpy module
    token_docx_sent = docxpy.process(docx_to_be_read)
    token_docx = docxpy.process(docx_to_be_read)
    print("Working on file: " + docx_to_be_read)
    list_of_files_processed.append(docx_to_be_read)

    #Expand contractions
    token_docx = contractions.fix(token_docx)
    print("Contractions completed...")

    SK_sw = sklearn_stop_words
    NLTK_sw = stopwords.words('English')
    stop_words = SK_sw.union(NLTK_sw)

    token_docx_unigram = re.sub(r'[A-Za-z0-9]+:+\s+\s', '' , token_docx)
    token_docx_unigram = re.sub(r'\t*', '', token_docx_unigram)
    token_docx_unigram = re.sub(r'\n*', '', token_docx_unigram)

    token_docx_sent = re.sub(r'[A-Za-z0-9]+:+\s+\s', '', token_docx)
    token_docx_sent = re.sub(r'\t*', '', token_docx_unigram)
    token_docx_sent = re.sub(r'\n*', '', token_docx_unigram)

    print("Tokenizing document...")
    tokenized_docx = tokenizer_unigram.tokenize(token_docx_unigram)
    tokenized_docx_sent = re.split(r'(?<=[^A-Z].[.?!]) +(?=[A-Z])',token_docx_sent)
    normalized_tokens = [x.lower() for x in tokenized_docx]
    normalized_tokens_sent = [y.lower() for y in tokenized_docx_sent]
    normalized_tokens_without_sw = [w for w in normalized_tokens if w not in stop_words]
    normalized_tokens_sent_without_sw = [z for z in normalized_tokens_sent if z not in stop_words]

    print("************************************************************************************************************")
    print("File " + docx_to_be_read + " has this many words, with stopwords removed:")
    print(len(normalized_tokens_without_sw))
    print("************************************************************************************************************")


    #Tag words with Part of Speech details
    normalized_tagged = nltk.pos_tag(normalized_tokens_without_sw)
    print("Assigning POS Tags...")
    docs_read += 1
    #inserting words into dictionary
    print("Inserting words into dictionary...")

    for tagged_words in normalized_tagged:
        list_of_words_with_pos_tags.append(tagged_words)
        # example_file_creation.save_dict_to_csv('DUMP.csv', dict_of_words_with_pos_tags)

    print("Total words read: ")
    print(len(list_of_words_with_pos_tags))

    return list_of_words_with_pos_tags, normalized_tokens_sent_without_sw



def lemmatizer_function(list_of_words_with_pos_tags):
    lemmatizer = WordNetLemmatizer()
    lemmatized_list = []

    #POS Tagging from NLTK does not jive well with WordNet Lemmatizer.
    #need to convert NLTK part of speech tags to pos tags the WordNet Lemmatizer recognizes

    for words,pos_tags in list_of_words_with_pos_tags:
    #TODO: Print out the actual word type so we know what it is, just in case.
        #print("Beginning lemmatization on word: " + words)
        if pos_tags.startswith('N'):
            pos_tags = 'n'
            lemmatized_word = lemmatizer.lemmatize(words, pos=pos_tags)
            lemmatized_list.append(lemmatized_word)
            # print("Lemmatized word: " + lemmatized_word)
            # print("Word type: Noun")
        elif pos_tags.startswith('J'):
            pos_tags = 'a'
            lemmatized_word = lemmatizer.lemmatize(words, pos=pos_tags)
            lemmatized_list.append(lemmatized_word)
            # print("Lemmatized word: " + lemmatized_word)
            # print("Word type: Adjective")
        elif pos_tags.startswith('R'):
            pos_tags = 'r'
            lemmatized_word = lemmatizer.lemmatize(words, pos=pos_tags)
            lemmatized_list.append(lemmatized_word)
            # print("Word type: Adverb")
            # print("Lemmatized word: " + lemmatized_word)
        elif pos_tags.startswith('V'):
             pos_tags = 'v'
             lemmatized_word = lemmatizer.lemmatize(words, pos=pos_tags)
             lemmatized_list.append(lemmatized_word)
             # print("Word type: Verb")
             # print("Lemmatized word: " + lemmatized_word)
        elif pos_tags.startswith('C'):
             pos_tags = 'n'
             lemmatized_word = lemmatizer.lemmatize(words, pos=pos_tags)
             lemmatized_list.append(lemmatized_word)
             # print("Lemmatized word: " + lemmatized_word)
             # print("Word type: Noun")

    print("Completed word gathering and lemmatization. Ready for FreqDist.")
    return lemmatized_list

from nltk.collocations import *

#Collocation, bigrams, and FreqDist
def collocation_bigram_freqdist(lemmatized_list):

    bigrams = nltk.collocations.BigramAssocMeasures()
    fdist = BigramCollocationFinder.from_words(lemmatized_list)
    fd_length = len(fdist.word_fd.items())

    return fdist,fd_length


def term_frequency_generator(fdist,fd_length):
    # Finds the term frequency by dividing word by total amount of words
    print("Attempting to calculate Term Frequency...")
    tf_list = []
    tf_dict = OrderedDict()
    for word,count in fdist.word_fd.items():
        tf_list.append((word,(count/float(fd_length))))
        tf_dict.update(({word:(count/float(fd_length))}))


    return tf_list, tf_dict

# print("Attempting to calculate IDF")
# idf_list = []
# import math
# N = fd_length
#
# for word,value in tf_list:
#     idf_list.append((word,math.log(N / float(value))))
#
# print("Attempting to calculate TF-IDF...")
# tf_list_values = []
# for word,value in tf_list:
#     tf_list_values.append(value)
# idf_list_values =[]
# for a,b in idf_list:
#     idf_list_values.append(b)
#
#
# tf_idf_list_all = {}
# tf_idf_list = numpy.multiply(tf_list_values,idf_list_values)
# print(tf_idf_list_all)
#
#
#
#
#
#
#
#
#
# print("test")
#















