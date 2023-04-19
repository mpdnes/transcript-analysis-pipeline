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

from collections import Counter			# Types of collections.

# tokenize document by sentence, under regular expression control.
from nltk import regexp_tokenize

from nltk.corpus import stopwords
nltk.download( 'stopwords' )                            # Unknown reason why.
stop_words = sorted( stopwords.words('english') )       # Global variable.
from pluralizer import Pluralizer


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
    print( 'DEBUGGING:  docxpy returns tokenized as a type :', type(tokenized) )  	# Debugging

    # Expand contractions to remove noise:
    # We do not want "don't" to matter.
    tokenized = contractions.fix(tokenized)

    pluralizer = Pluralizer()

    assert pluralizer.pluralize('apple', 1, False) == 'apple'
    assert pluralizer.pluralize('apple', 1, True) == '1 apple'
    assert pluralizer.pluralize('apple', 2, False) == 'apples'
    assert pluralizer.pluralize('apple', 2, True) == '2 apples'

    assert pluralizer.plural('apple') == 'apples'
    assert pluralizer.singular('apples') == 'apple'

    assert pluralizer.isPlural('apples') == True
    assert pluralizer.isPlural('apple') == False
    assert pluralizer.isSingular('apples') == False
    assert pluralizer.isSingular('apple') == True



    print( 'CONTRACTIONS EXPANDED:  docxpy returns tokenized as a type :', type(tokenized) )  	# Debugging

    #
    #  Remove the "typewell does this... " line.
    #
    print('WARNING ... skipping pre_filter in file', __file__  )
    # tokenized = pre_filter_to_remove_known_phrases( tokenized )

    #  Find number of speaker transitions:
    #
    #  A.  There is a dictionary entry for each speaker, 
    #      with the number of words that they speak.
    #
    #  B.  The number of times that the speaker changes is also returned.
    [dict_of_speakers, n_transitions] = analyze_speaker_frequency_and_xfers( tokenized )


    unitary_words_and_abbreviations     = unigram_analysis( tokenized )
    print("unitary_words_and_abbreviations = ", end='');
    print( type( unitary_words_and_abbreviations ) ) 
    # bigrams 	 			= bigram_analysis( tokenized )
    # trigrams 				= trigram_analysis( tokenized )
    # quadgrams 			= quadgram_analysis( tokenized )

    #
    #  For a given python list, the '+' operator is concatenation.
    #  Here we concatenate all the words we need to report.
    #
    all_words   = unitary_words_and_abbreviations
    # all_words = all_words + bigrams
    # all_words = all_words + trigrams
    # all_words = all_words + quadgrams
 
    #
    #  Generate a word cloud, create reports for interpretors, etc...
    # 
    # print("All words = ", end='');
    # print( all_words ) 
    # for word, freq in all_words.items() :
    #    print('word=', word, ' freq=', freq )
    #
    # print('\n\n')
    # for key in dict.keys(all_words):
        # print("key = ", key )
    word_cloud = report_these_words( all_words )
    print("Printing word cloud...")
    plt.figure(figsize=(15,8))
    plt.imshow(word_cloud)
    plt.show()

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
    print('done')
else:
    print("This is NOT main.  Nevermind.  Quitting.")


