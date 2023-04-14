#
#  STANDARD PROLOG -- includes cruft
#

import re 				        # Regular expression matching.
import docxpy			    		# Handling *.docx file in python.

import nltk			                # Natural Language Toolkit
from nltk.corpus import stopwords		# Common stopwords.
import contractions			        # Common language contractions.

from nltk.tokenize import word_tokenize 	# Tokenizer
from nltk.tokenize import sent_tokenize		# ??? Sentence Tokenizer??

from collections import Counter			# Types of collections.

# tokenize document by sentence, under regular expression control.
from nltk import regexp_tokenize



#
# Remove the "typewell does this... " line.
# filter out  "*** TypeWell transcription provides a meaning-for-meaning" as not valid input.
#
def pre_filter_to_remove_known_phrases( tokenized ):
    developing_debugging = False	# Turn on to print feedback.

    interesting_lines    = []

    separate_input_lines = tokenized.splitlines( )
    print( "Document has: ", len(separate_input_lines), " lines" )

    for line_idx in range(0,len(separate_input_lines)):
        the_input_line = separate_input_lines[line_idx]
        if ( len(the_input_line) <= 1 ):
            continue             # Skip this line, it only has a newline on it.

        matched_expressions = re.match( '.*TypeWell transcription provides a meaning-for-meaning.*', the_input_line )
        if ( matched_expressions is not None ):
            if ( developing_debugging ) :
                print('SKIPPING ', the_input_line )
            continue             # Skip this line, we know this already
        else :
            if ( developing_debugging ) :
                print('ADDING   ', the_input_line )
            interesting_lines.append( the_input_line )
            
    return interesting_lines

