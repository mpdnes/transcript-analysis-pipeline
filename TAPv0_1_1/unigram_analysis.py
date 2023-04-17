
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
#  This is our acronym identifier:
#
from check_if_word_is_acronym import check_if_word_is_acronym

# 
#  Classify the word as being important (True), or not (False).
#  Valid words must start with a letter, not a number. 
# 
def classify_this_unigram_word_and_count( candidate_word, this_word_freq ) :
    rc          	= False;		# Default return code --> NOT IMPORTANT
    this_word_length    = len(candidate_word)

    # Check for starting with a letter:
    matched_expressions = re.match( '^[a-zA-Z].*', candidate_word )
    if ( matched_expressions is None ) :
        rc = False;
    else :
        # Length must be at least 4 letters:
        if ( this_word_length >= 11 ) :
            rc = True
        elif ( this_word_length >= 9   and this_word_freq >=  1 ) :
            rc = True
        elif ( this_word_length >= 6   and this_word_freq >=  2 ) :
            rc = True
        elif ( this_word_length >= 5   and this_word_freq >=  4 ) :
            rc = True
        elif ( this_word_length >= 4   and this_word_freq >=  6 ) :
            rc = True

    return rc


# ##############################################################################
#
#  Unigram Analysis:
#
#  Separate out the individual words.
#
#  Use a classifier to identify "unusual" words:
#      A. words that are very frequent, or
#      B. words that are very unusual, or
#      C. words that are very long.
#
#  To do this:
#  1.  Put all the words into a dictionary.  
#  2.  The value in the dictionary is the number of times each word occurs.
#
#
#  Returns:
#  A DICT of WORDS and ACORNYMS considered important.
#
#  A.  Important words, ( Mahalanobis ), or
#  A Simple list of words that might be important to a captionist, or interpretor.
#
#  B.  ACRONYMS
#      (NFL, 
#       DoC, etc... )
#
#  Method:
#  
#  unigram_dict = dict();		# Empty dict.
#  
#  For each and every input line in the document:
#      Check for a speaker.
#          IGNORE THE SPEAKER for now.  Leave that to another function.
#      For all the words said:
#          Split them into separate tokens.
#          For each token:
#               if token in dict:
#                      unigram_dict(token) = unigram_dict(token) + 1
#               else:
#                      unigram_dict(token) = 1
#
#  resulting_dict = unigram_dict() :
#  For each key_word in the keys resulting_dict:
#      b_important     = run_unigram_classifier( key_word, resulting_dict(key_word) );
#      b_is_acronym    = test_for_acronym( key_word );
#      if ( (not b_important) AND (not b_is_acronym) ) :
#          resulting_dict.pop( key_word )
#
#   return resulting_dict
#
def unigram_analysis( tokenized ):
    resulting_dict  		= dict()
    ACK_dict   			= dict()			# Acronym dictionary
    all_text_in_doc_str 	= '';
    words_said          	= '';

    print( 'debugging: ' )
    print( 'DEBUGGING: input tokenized is of type: ', type( tokenized ), ' one sub-string per line' )
    print( '' )	# Debugging
    print( '' )	# Debugging

    # Analyze ALL LINES IN THIS DOCUMENT:
    separate_input_lines = tokenized.splitlines( )
    for line_idx in range(0,len(separate_input_lines)):
        the_input_line = separate_input_lines[line_idx]
        if ( len(the_input_line) <= 1 ):
            continue             # Skip this line, it only has a newline on it.

        # ########################################################
        #
        # IGNORE THE SPEAKER:
        #
        # Some transcribers only put one space after the colon.
        # So we need to carefully match the expression:
        # (one or more characters that are NOT colons)(a colon, followed by one or more whitespace chars)(spoken text)
        #
        matched_expressions = re.match( '(^[^:]+)(:\s+)(.*)', the_input_line )

        if ( matched_expressions is not None ):
            # print('There is a speaker Match Here:')
            the_speaker = matched_expressions.group(1)
            # print('Group 2 is: ', matched_expressions.group(2) )	# The ': *' separator.
            words_said  = matched_expressions.group(3)
        else:
            words_said  = the_input_line

        all_text_in_doc_str   = all_text_in_doc_str + ' ' + words_said      # Append these words to a spoken stream of words:

    # ##############################################################################
    #
    # SORT THROUGH THE TOKENIZED WORDS:
    # Roll your own frequency distribution
    #
    #
    # Go through the main text, and then decide which words are important: 
    #
    # The second parameter gives a regular expression to use to match a "word"
    # So, in this case, a word can contain a hypen, or an underscore, but NOT a period.
    #
    list_of_str__of_sep_words    = regexp_tokenize(all_text_in_doc_str, r'[-a-zA-Z0-9_]+')       # No periods.
    #note to self:   print('DEVELOPMENT: regexp_tokenize returns : ', type(list_of_str__of_sep_words) )
    #note to self:   print( list_of_str__of_sep_words )
    #note to self:   print('DEVELOPMENT: regexp_tokenize returns : a list of separate strings')

    # for all_items_in_list_of_strings 
    for idx in range(0,len(list_of_str__of_sep_words)):
        this_word = list_of_str__of_sep_words[ idx ]

        # uniquely add to dict of acronyms
        # If it was already identified as an acronym,
        # do not bother to run the acronym classifier:
        if ( this_word in ACK_dict ):
            ACK_dict[this_word] = ACK_dict[this_word] + 1
        else :
            # If this looks like a valid acronym
            if ( check_if_word_is_acronym( this_word ) == True ) :
                ACK_dict[this_word] =  1
            else :
                # Convert to lower case.
                # Uniquely add to dictionary.
                lc_word = this_word.lower()
                if ( lc_word in resulting_dict ) :
                    resulting_dict[lc_word] = resulting_dict[lc_word] + 1
                else :
                    resulting_dict[lc_word] = 1

    #   for each word in dictionary of words: # Not the acronyms
    #       classify as important or not.
    #       delete unimportant words  (pop out of the dictionary )
    merged_dict = dict( ACK_dict )
    for each_word,each_freq in resulting_dict.items() :
        print('Testing : ', each_word, ' which happens ', each_freq, ' times ')
        this_word_is_important  = classify_this_unigram_word_and_count( each_word, each_freq )
        if ( this_word_is_important ) :
            merged_dict[ each_word ] = each_freq

    # print('DEBUGGING: returning a type: ', end='')
    # print( type(merged_dict) )

    print('DEBUGGING: Dumping the dictionary')
    for word,freq in merged_dict.items() :
        print('word=', word, '  \tfreq = ', freq )

    return merged_dict

