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

import re 				                # Regular expression matching.
import docxpy			    		    # Handling *.docx file in python.

from wordcloud import WordCloud         # For creating the word cloud.
import matplotlib.pyplot as plt         # For creating the word cloud.
import PIL as img                       # For creating the word cloud.

import nltk			                    # Natural Language Toolkit
from nltk.corpus import stopwords		# Common stopwords.
import contractions			            # Common language contractions.
from nltk import *
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

# Thomas Module(s)
import Sort_Dict_of_Integers            # Given a dictionary of integers, sort them in order by the contents.


from nltk.corpus import stopwords
stop_words = sorted( stopwords.words('english') )       # Global variable.


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

    # Creating a list of all transcripts to analyze.
    # Return a list of *.doc's (which should be changed to *.docX es).
    # AND we get a list of directories.
    # And a number of folders in the directory.
    [doc_list, docx_list, dirs_list, num_of_folders] = preprocessing.directctory_inspector(root_dir)
    print("The list of files about to be processed are: ")
    print(docx_list)
    list_of_all_tf_dicts = []
    term_freq_list       = []

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

    #  I have gotten a list of all the docxs that I want to process.
    #  Now I need to process them one by one and insert them each into their
    #  own dictionary. To do this, I have to pass in one file at a time
    #  to be read until all the files are read and then passed into a dictionary.
    #  this is all to compute the TF-IDF

    # THIS LOOP COMPUTES the TF-IDF.
    #
    # For each transcript in the list of transcripts.
    #     Generates a DICTIONARY per transcript.
    #
    # The result is a list of dictionaries, with term frequencies.
    #
    print("DEBUGGING HERE -- USING ONLY THE FIRST THREE DOCUMENTS\n")
    for docx in docx_list[0:3]:
        # This gets us the words with the Part of Speach tagging.
        # POS is important to create an accurate lemmatized list.
        #
        list_of_words_with_pos_tags = preprocessing.read_docx_files(doc_list,docx,dirs_list)

        # Reduce a word to its root form:
        lemmatized_list             = preprocessing.lemmatizer_function(list_of_words_with_pos_tags)

        # Collocation = "Co-Location" in TBK Terms.
        # Result: A frequency distribution, and the number of unique words.
        [fdist,fd_length]           = preprocessing.collocation_bigram_freqdist(lemmatized_list)

        # This is the TERM FREQUENCY only.
        [term_freq_list, tf_dict]   = preprocessing.term_frequency_generator(fdist,fd_length)

        # Put this dictionary in the list.
        list_of_all_tf_dicts.append(tf_dict)

    # At this point we have a list of dictionaries with unique words, and term frequencies, PER TRANSCRIPT.
    #
    #   NOW CREATE THE IDF -- a measure of how "interesting" each term is.
    #
    [list_of_all_idf_dicts,total_num_docs] = postprocessing.idf_calculator(list_of_all_tf_dicts)


    #  This scales the terms according to ZIPFS Law.
    #  (This involves conversion to a logorithmic domain.)
    scaled_idf_dict = OrderedDict(postprocessing.zipfs_law_scaling(list_of_all_idf_dicts,total_num_docs))

    # This next loop examines ALL transcripts, not just one.
    # This forms a global TF-IDF list, for all terms.
    tf_idf_list = []
    for dicts in list_of_all_tf_dicts:
        dict_to_add = postprocessing.compute_tf_idf(dicts, scaled_idf_dict)
        tf_idf_list.append(dict_to_add)

    #  Sort in order of decreasing frequency:
    #  Or, perhaps, importance??
    sorted_tf_idf_list = []
    for dict_in_list in tf_idf_list:
        sorted_tf_idf = Sort_Dict_of_Integers.Sort_Dict_of_Integers(dict_in_list)
        sorted_tf_idf_list.append(sorted_tf_idf)

    #
    #  ACTUALLY CREATE THE WORD CLOUD!
    #  This creates it using imshow(), but never displays it.
    #

    counter = 0
    for dict_to_wordcloud in sorted_tf_idf_list:
        # TODO -- TBK Change options to wordcloud_generator, to change the colors.

        # TODO Figure out how to change the resulting file size:
        # TODO: This might require changing the rc.params so the backend renderer is smarter.
        # This specifies the file size in inches:
        plt.figure( figsize=(10,14), dpi=100 )

        word_cloud = postprocessing.wordcloud_generator(dict_to_wordcloud)

        # NOW -- NOW that we have created the figure that is bigger,
        # NOW put the word cloud into it.   This makes a bigger Wordcloud!
        wc_fig = plt.imshow( \
              word_cloud.recolor( color_func=postprocessing.hsl_random_color_func, random_state=3), \
              interpolation = "bilinear")


        # This gets the basename with the extension, and puts it in the title.
        plt.title( docx_list[counter][-11:] )

        plt.axis( "off" )

        plt.show()

        # TODO: change the number so that it starts with 0.
        # 01, 02 ... 09, 10, ...
        # Save to file:
        plt.savefig('Wordcloud'+ str(counter), dpi=200 )
        counter+=1

    # TODO: Check the TF-IDF Math.

    print("debug")

#
#  EPILOG -- CALL MAIN
#
#  TODO: add argument parsing.
#
if ( __name__ == "__main__" ) :
    # Make the directory for documents user independent.
    home_dir = os.environ['HOME']
    root_dir = home_dir + '/Documents/GitHub/TAP/TEST_SUITE/CSCI42001'
    print("Later on we will add argument parsing here.")
    print("This IS main.  Calling the main routine.")
    main( root_dir )
    print('done')
else:
    print("This is NOT main.  Nevermind.  Quitting.")


