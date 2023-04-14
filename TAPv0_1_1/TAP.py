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
#  DrKinsman code to sort a dictionary from Most common to least common:
#
from Sort_Dict_of_Integers                import Sort_Dict_of_Integers
from pre_filter_to_remove_known_phrases   import *
from analyze_speaker_frequency_and_xfers  import *

from unigram_analysis                     import *
from bigram_analysis                      import *
from trigram_analysis                     import *
from quadgram_analysis                    import *

from report_these_words                   import *


# Number of unique words to get for one document, before the 180 stop words are removed.
N_SINGLE_TUPLES_TO_GET_PER_DOC = 600

# ##############################################################################
#
#  Here is the main module.
#
def main( transcript_file, comparison_file_or_stats ):
    file = transcript_file

    # Read in text from a Microsoft DOCX file.
    tokenized = docxpy.process(file)
    print( 'docxpy returns tokenized as a type :', type(tokenized) )  	# Debugging

    # Expand contractions to remove noise:
    # We do not want "don't" to matter.
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
    # bigrams 	 			= bigram_analysis( tokenized )
    # trigrams 				= trigram_analysis( tokenized )
    # quadgrams 			= quadgram_analysis( tokenized )

    #
    #  For a given python list, the '+' operator is concatenation.
    #  Here we concatenate all the words we need to report.
    #
    all_words = unitary_words_and_abbreviations
    # all_words = all_words + bigrams
    # all_words = all_words + trigrams
    # all_words = all_words + quadgrams
 
 
    #
    #  Generate a word cloud, create reports for interpretors, etc...
    # 
    report_these_words( all_words )  


# ##############################################################################
#
#  EPILOG -- CALL MAIN
#
#  TODO: add argument parsing.
#
if ( __name__ == "__main__" ) :
    transcript_file = '../TEST_SUITE/CS420_2221_10117_2022-11-16.docx'          # "Mahalanobis" happens 6 times.
    comparison_file_or_stats = '../TEST_SUITE/Baseline_Words.docx'        	# For comparison
    print("Later on we will add argument parsing here.")
    print("This IS main.  Calling the main routine.")
    main( transcript_file, comparison_file_or_stats )
else:
    print("This is NOT main.  Nevermind.  Quitting.")

