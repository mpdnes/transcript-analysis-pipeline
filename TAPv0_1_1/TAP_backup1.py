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

import nltk			                # Natural Language Toolkit
from nltk.corpus import stopwords		# Common stopwords.
import contractions			        # Common language contractions.

#import regular expression tokenizer
from nltk.tokenize import word_tokenize 	# Tokenizer
from nltk.tokenize import sent_tokenize		# ??? Sentence Tokenizer??

from collections import Counter			# Types of collections.

# tokenize document by sentence, under regular expression control.
from nltk import regexp_tokenize

# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()

# Get a list of the usual stopwords:
from nltk.corpus import stopwords
nltk.download( 'stopwords' )                            # Unknown reason why.
stop_words = sorted( stopwords.words('english') )       # Global variable.

#find collocations in text
#NOTE works better without removing stopwords first
from nltk.collocations import *			# Use everything in collocations.  Why???

# This is used to find the frequency distributions.
# The frequency distributions are how often each word is used in each corpus.
from nltk.probability import FreqDist

#
#  My own code to sort a dictionary from Most common to least common:
#
from Sort_Dict_of_Integers import Sort_Dict_of_Integers

from pre_filter_to_remove_known_phrases import *


# Number of unique words to get for one document, before the 180 stop words are removed.
# 
# Notice:
# The typical analysis only wants the "usual" words.  We don't care about them.
# We want :
#    A.  Unusually long words, OR
#    B.  Unusually words which are not frequently found.
#
N_SINGLE_TUPLES_TO_GET_PER_DOC = 500



# ##############################################################################
#
#       FUNCTION DEFINITIONS
# 
# ##############################################################################

#  #
#  # Remove the "typewell does this... " line.
#  #
#  def pre_filter_to_remove_known_phrases( tokenized ):
#      tokenized = tokenized
#      return tokenized

# ##############################################################################
#
# Find number of speaker transitions:
#
# 1.  There is a dictionary entry for each speaker, 
#     with the number of words that they speak.
#
# 2.  The number of times that the speaker changes is also returned.
def analyze_speaker_frequency_and_xfers( tokenized ):
    dict_of_speakers      = dict()
    n_transitions         = 0
    return [dict_of_speakers, n_transitions]


# ##############################################################################
#
#  Unigram Analysis:
#
def unigram_analysis( tokenized ):
    unigrams = []
    return unigrams


# ##############################################################################
#
#  bigram Analysis:
#
def bigram_analysis( tokenized ):
    bigrams = []
    return bigrams


# ##############################################################################
#
#  Trigram Analysis:
#
def trigram_analysis( tokenized ):
    trigrams = []
    return trigrams


# ##############################################################################
#
#  quadgram Analysis:
#
def quadgram_analysis( tokenized ):
    quadgrams = []
    return quadgrams



# ##############################################################################
#
#  Create a report:
#
def report_these_words( all_words ):
     print( all_words )


# ##############################################################################
#
#  Here is the main module.
#
def main( transcript_file, comparison_file_or_stats ):
    print("main() called.")
    file = transcript_file

    tokenized = []
    # read in text file for processing
    tokenized = docxpy.process(file)

    # expand contractions to remove noise:
    tokenized = contractions.fix(tokenized)

    #
    #  Remove the "typewell does this... " line.
    #
    tokenized = pre_filter_to_remove_known_phrases( tokenized )

    #  Find number of speaker transitions:
    #
    #  A.  There is a dictionary entry for each speaker, 
    #      with the number of words that they speak.
    #
    #  B.  The number of times that the speaker changes is also returned.
    [dict_of_speakers, n_transitions] = analyze_speaker_frequency_and_xfers( tokenized )


    unitary_words_and_abbreviations     = unigram_analysis( tokenized )
    bigrams 	 			= bigram_analysis( tokenized )
    trigrams 				= trigram_analysis( tokenized )
    quadgrams 				= quadgram_analysis( tokenized )

    all_words = []
    all_words.append( unitary_words_and_abbreviations )
    all_words.append( bigrams )
    all_words.append( trigrams )
    all_words.append( quadgrams )
 
 
    #
    #  Generate a word cloud, create reports for interpretors, etc...
    # 
    report_these_words( all_words )  


# ##############################################################################
#
#  EPILOG -- CALL MAIN
#
#

if ( __name__ == "__main__" ) :
    transcript_file = '../TEST_SUITE/CS420_2221_10117_2022-11-16.docx'          # "Mahalanobis" happens 6 times.
    comparison_file_or_stats = '../TEST_SUITE/Baseline_Words.docx'        	# For comparison
    print("Later on we will add argument parsing here.")
    print("This IS main.  Calling the main routine.")
    main( transcript_file, comparison_file_or_stats )
else:
    print("This is NOT main.  Nevermind.  Quitting.")




