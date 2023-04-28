#
# Pycharm:
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#  Python program to learn how to handle the *.docx files,
#  and the Natural Language Tool Kit.
#
# Version 3:
# Wed Feb  1 10:57:03 EST 2023		Mike Donovan
# Wrote the main routines.
#
# Wed Feb  1 10:57:03 EST 2023		T.B.Kinsman,
# Converted into a standard python structure for now.
# With main( ) called from the end.
#	

#
#  PROLOG: 
#

import re 				        # Regular expression matching.
import docxpy			    		# Handling *.docx file in python.
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import PIL as img

import nltk			                # Natural Language Toolkit
from nltk.corpus import stopwords		# Common stopwords.
import contractions			        # Common language contractions.

#import regular expression tokenizer
from nltk.tokenize import word_tokenize 	# Tokenizer
from nltk.tokenize import sent_tokenize		# ??? Sentence Tokenizer??


# tokenize document by sentence, under regular expression control.
from nltk import regexp_tokenize

#Mike modules
import preprocessing
import postprocessing
import csv
import os


from nltk.corpus import stopwords                       # Unknown reason why.
stop_words = sorted( stopwords.words('english') )       # Global variable.
from pluralizer import Pluralizer


#find collocations in text
#NOTE works better without removing stopwords first
from nltk.collocations import *			# Use everything in collocations.  Why???

# This is used to find the frequency distributions.
# The frequency distributions are how often each word is used in each corpus.
from nltk.probability import FreqDist

# ##############################################################################
#
#  Here is the main module.
#
def main( root_dir):

    [doc_list, docx_list, dirs_list, num_of_folders] = preprocessing.directctory_inspector(root_dir)

    # TODO: This is an early attempt at making the process more user friendly
    # print("***********************************************************************")
    # print("There are " + str(num_of_folders) + " classes to process.")
    # print("Please choose from a list of the possible options:")
    # print("1. List classes.")
    # print("2. I know what classes I want to process and I can enter it.")
    # print("3. I want to process all transcripts in all classes.")
    # print("3. I don't want to do either of these." + "\n")
    # initial_choice = input("Input choice with number (no period) >> ")
    #
    # if initial_choice == "1":
    #     print(sorted(dirs_list))
    #     class_to_process = input("What class do you want to process? >> " + "\n")
    #     location = root_dir + "/" + class_to_process
    #     length_of_dir = len(os.listdir(location))
    #     print(str(class_to_process) + " has " + str(length_of_dir) + " transcripts." + "\n")
    #     print("Do you want to process all the transcripts or a specific number?" )
    #     print("1. All.")
    #     print("2. A specific number." + "\n")
    #     input("Input choice with number (no period) >> ")
    #
    #
    #
    # elif initial_choice == "2":
    #     specified_class = input("Enter the class you want to process >> ")
    # elif initial_choice == "2":
    #     exit("Ending TAP")




    list_of_words_with_pos_tags = preprocessing.read_docx_files(doc_list,docx_list,dirs_list)

    lemmatized_list = preprocessing.lemmatizer_function(list_of_words_with_pos_tags)

    [fdist,fd_length] = preprocessing.collocation_bigram_freqdist(lemmatized_list)

    termfreq = preprocessing.term_frequency_generator(fdist,fd_length)

    return_code= postprocessing.csv_writer(termfreq,csv_file)

    if return_code:
        print("All files processed and exported to CSV file.")
    elif return_code == 'Exit':
        print("Something else happened. Did not export to CSV.")


#
#  EPILOG -- CALL MAIN
#
#  TODO: add argument parsing.
#
if ( __name__ == "__main__" ) :
    root_dir = '../TEST_SUITE/DUMP/CSCI42001'
    csv_file = '../TEST_SUITE/DUMP/DUMP_Words_All_CSCI.csv'
    print("Later on we will add argument parsing here.")
    print("This IS main.  Calling the main routine.")
    main( root_dir )
    print('done')
else:
    print("This is NOT main.  Nevermind.  Quitting.")


