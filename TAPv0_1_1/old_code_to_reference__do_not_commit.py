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

import re 					        # Regular expression matching.
import docxpy			    		# Handling *.docx file in python.

import nltk				            # Natural Language Toolkit
from nltk.corpus import stopwords	# Common stopwords.
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
# Remove the "typewell does this... " line.
#
tokenized = pre_filter_to_remove_known_phrases( tokenized )
    tokenized = tokenized


# Find number of speaker transitions:
#
# 1.  There is a dictionary entry for each speaker, 
#     with the number of words that they speak.
#
# 2.  The number of times that the speaker changes is also returned.
[dict_of_speakers, n_transitions] = analyze_speaker_frequency_and_xfers( tokenized )

    #
    # This is a loop inserted before the rest of the processing.
    # The goal here is to work on the raw text:
    # 1.  Identify speaker changes.
    # 2.  Associate the spoken text of the main speaker with the 'Instructor'
    # 3.  Ignore student utterances as noise.
    #
    print( "Before we do anything else, or tokenize the strings, analyze the file as a string of known characters.")
    print( "Find the first line, and process that. ")
    separate_input_lines = tokenized.splitlines( )
    print( "Document has: ", len(separate_input_lines), " lines" )

    main_speaker = ""
    main_text    = ""
    the_speaker  = ""

    for line_idx in range(0,len(separate_input_lines)):
        the_input_line = separate_input_lines[line_idx]
        if ( len(the_input_line) <= 1 ):
            continue             # Skip this line, it only has a newline on it.

        print('\n=================  TOP OF MAIN LOOP PER LINE =================')
        #
        print('Working on line ',  line_idx )
        print('Input = ',          the_input_line )

        if re.search('mahalanobis', the_input_line, re.IGNORECASE ):
            print('this line contains the word mahalanobis')
        if re.search('regularization', the_input_line, re.IGNORECASE ):
            print('this line contains the word regularization')

        # ########################################################
        #
        #
        # Some transcribers only put one space after the colon.
        # So we need to carefully match the expression:
        # (one or more characters that are NOT colons)(a colon, followed by one or more whitespace chars)(spoken text)
        #
        b_is_speaker = re.search(':\s+', the_input_line )
        matched_expressions = re.match( '(^[^:]+)(:\s+)(.*)', the_input_line )

        if ( matched_expressions is not None ):
            print('There is a speaker Match Here:')
            # print('Group 0 is: ', mmm.group(0) )	# This is the entire line.
            # print('Group 1 is: ', matched_expressions.group(1) )	# The first group matched.
            # print('Group 2 is: ', matched_expressions.group(2) )	# The ': *' separator.
            # print('Group 3 is: ', matched_expressions.group(3) )	# The rest of the line.
            # print(' ')
            the_speaker = matched_expressions.group(1)
            words_said  = matched_expressions.group(3)
            print('speaker: ', the_speaker, ' says ', len(words_said), ' characters')
        else:
            # print('(The Speaker)(:  )(Text) pattern did not match.' )
            words_said = the_input_line

        if ( len(main_speaker) == 0 ) and ( len(the_speaker) > 0 ):
            # THIS ONLY HAPPENS ONCE.
            # The first time this happens,
            # record the first speaker as the name of the main speaker.
            # This only happens once.
            #
            # TODO:
            # We assume that the instructor is the the main speaker.
            # Later on, expand to a sub-set of legal names for the main speaker.
            # The set: instructor, speaker, professor
            main_speaker = the_speaker +'' # Force a deep copy  TODO check later if we can ignore this.

        # If the speaker is the main speaker, record the words said:
        if ( the_speaker is not None ) and ( len( the_speaker ) > 0 ) and (len(main_speaker) > 0) and ( the_speaker == main_speaker ):
            main_text = main_text + ' ' + words_said      # Append these words to a spoken stream of words:
        #         if ( b_is_speaker ):
        #             print('Span of the match is: ', b_is_speaker.span())
        #             the_speaker   = the_input_line[ 0 : b_is_speaker.span(0)[0] ] # Get a slice:
        #             words_said    = the_input_line[ b_is_speaker.span(0)[1] : -1 ]
        #         else:
        #             # This text goes with the last speaker:
        #             print('no speaker set on line: ', line_idx )
        #             print('==>', the_input_line, '<==')

        # print("break here at the bottom of the loop")
    print('\n=================  BOT OF MAIN LOOP -- DONE PROCESSING THIS LINE =================')
    print('Break here outside the loop')

    # TODO -- filter out  "*** TypeWell transcription provides a meaning-for-meaning" as not valid input.

    #
    #  Now process the "main_text" and tokenize it...
    #
    # remove stopwords from predefined stopwords list
    # stopwords = set(stop_words.words('english'))
    #
    # #Clean up data
    # tokenized = re.sub("\t", "" , tokenized)
    # tokenized = re.sub("\n\n\n", "\n\n", tokenized)

    # Tokenize document by sentence and delete header
    #
    # The second parameter gives a regular expression to use to match
    # a "word".  So, in this case, a word can contain a hypen, or an underscore,
    # but NOT a period.
    tokenized = regexp_tokenize(main_text, r'[-a-zA-Z0-9_]+')       # No periods.
    # Debug:
    print( 'Number of tokens = ', end='')
    print( len( tokenized  ))
    # print("DELETING:", end='')
    # print( tokenized[0] )       # Debugging code
    # del tokenized[0]
    # del tokenized[0]
    # TODO: Add back the idea of deleting the header lines.
    #

    #convert document to lowercase
    #tokenized = [w.lower() for w in tokenized]
    # tagged = []

    # Label each word with the parts of speech (POS):
    tagged 	= nltk.pos_tag(tokenized)
    print( tagged )
    #
    # #
    # counts 	= Counter(tag for word, tag in tagged)
    # print(counts)
    # print(tagged)





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
    quadgrams 				= bigram_analysis( tokenized )



            continue             # Skip this line, it only has a newline on it.

        print('\n=================  TOP OF MAIN LOOP PER LINE =================')
        #
        print('Working on line ',  line_idx )
        print('Input = ',          the_input_line )

        if re.search('mahalanobis', the_input_line, re.IGNORECASE ):
            print('this line contains the word mahalanobis')
        if re.search('regularization', the_input_line, re.IGNORECASE ):
            print('this line contains the word regularization')

        # ########################################################
        #
        #
        # Some transcribers only put one space after the colon.
        # So we need to carefully match the expression:
        # (one or more characters that are NOT colons)(a colon, followed by one or more whitespace chars)(spoken text)
        #
        b_is_speaker = re.search(':\s+', the_input_line )
        matched_expressions = re.match( '(^[^:]+)(:\s+)(.*)', the_input_line )

        if ( matched_expressions is not None ):
            print('There is a speaker Match Here:')
            # print('Group 0 is: ', mmm.group(0) )	# This is the entire line.
            # print('Group 1 is: ', matched_expressions.group(1) )	# The first group matched.
            # print('Group 2 is: ', matched_expressions.group(2) )	# The ': *' separator.
            # print('Group 3 is: ', matched_expressions.group(3) )	# The rest of the line.
            # print(' ')
            the_speaker = matched_expressions.group(1)
            words_said  = matched_expressions.group(3)
            print('speaker: ', the_speaker, ' says ', len(words_said), ' characters')
        else:
            # print('(The Speaker)(:  )(Text) pattern did not match.' )
            words_said = the_input_line

        if ( len(main_speaker) == 0 ) and ( len(the_speaker) > 0 ):
            # THIS ONLY HAPPENS ONCE.
            # The first time this happens,
            # record the first speaker as the name of the main speaker.
            # This only happens once.
            #
            # TODO:
            # We assume that the instructor is the the main speaker.
            # Later on, expand to a sub-set of legal names for the main speaker.
            # The set: instructor, speaker, professor
            main_speaker = the_speaker +'' # Force a deep copy  TODO check later if we can ignore this.

        # If the speaker is the main speaker, record the words said:
        if ( the_speaker is not None ) and ( len( the_speaker ) > 0 ) and (len(main_speaker) > 0) and ( the_speaker == main_speaker ):
            main_text = main_text + ' ' + words_said      # Append these words to a spoken stream of words:
        #         if ( b_is_speaker ):
        #             print('Span of the match is: ', b_is_speaker.span())
        #             the_speaker   = the_input_line[ 0 : b_is_speaker.span(0)[0] ] # Get a slice:
        #             words_said    = the_input_line[ b_is_speaker.span(0)[1] : -1 ]
        #         else:
        #             # This text goes with the last speaker:
        #             print('no speaker set on line: ', line_idx )
        #             print('==>', the_input_line, '<==')

        # print("break here at the bottom of the loop")
    print('\n=================  BOT OF MAIN LOOP -- DONE PROCESSING THIS LINE =================')
    print('Break here outside the loop')

    # TODO -- filter out  "*** TypeWell transcription provides a meaning-for-meaning" as not valid input.

    #
    #  Now process the "main_text" and tokenize it...
    #
    # remove stopwords from predefined stopwords list
    # stopwords = set(stop_words.words('english'))
    #
    # #Clean up data
    # tokenized = re.sub("\t", "" , tokenized)
    # tokenized = re.sub("\n\n\n", "\n\n", tokenized)

    # Tokenize document by sentence and delete header
    #
    # The second parameter gives a regular expression to use to match
    # a "word".  So, in this case, a word can contain a hypen, or an underscore,
    # but NOT a period.
    tokenized = regexp_tokenize(main_text, r'[-a-zA-Z0-9_]+')       # No periods.
    # Debug:
    print( 'Number of tokens = ', end='')
    print( len( tokenized  ))
    # print("DELETING:", end='')
    # print( tokenized[0] )       # Debugging code
    # del tokenized[0]
    # del tokenized[0]
    # TODO: Add back the idea of deleting the header lines.
    #

    #convert document to lowercase
    #tokenized = [w.lower() for w in tokenized]
    # tagged = []

    # Label each word with the parts of speech (POS):
    tagged 	= nltk.pos_tag(tokenized)
    print( tagged )
    #
    # #
    # counts 	= Counter(tag for word, tag in tagged)
    # print(counts)
    # print(tagged)

    # Initialize empty BiGrams, TriGrams, and QuadGrams:
    # Create instances of these objects:
    bigram_measures   = nltk.collocations.BigramAssocMeasures()
    trigram_measures  = nltk.collocations.TrigramAssocMeasures()
    fourgram_measures = nltk.collocations.QuadgramAssocMeasures()

    # Find the BiGrams, TriGrams, and Quadgrams:
    # Find a series of words that occur much more often than by chance:
    # This is comparing, based on Point-Wise-Mutual-Information.
    # This explains why words like "Obi-Wan", which is not frequent at any level, pops to the top.
    # This compares the probabilitiy of two events occurring together,
    # compared to chance.
    finder2 = BigramCollocationFinder.from_words(tokenized)
    finder3 = TrigramCollocationFinder.from_words(tokenized)
    finder4 = QuadgramCollocationFinder.from_words(tokenized)

    #measured using Pointwise Mutual Information ()
    #
    #  For other possible measures: https://www.nltk.org/howto/collocations.html
    #
    finder2 = finder2.nbest(  bigram_measures.pmi,   20)
    finder3 = finder3.nbest(  trigram_measures.pmi,  20)
    found_4 = finder4.nbest(  fourgram_measures.pmi, 20)

    print("Printing the BiGrams:")
    print(finder2)

    print("Printing the Trigrams:")
    print(finder3)

    #
    # TODO -- try different measures of .... compared to PMI.
    #
    for measure_idx in range(1, 5) :
        if ( measure_idx == 1 ) :
            print('trying method 1 - PMI:')
            found_4 = finder4.nbest(  fourgram_measures.pmi, 20)
        elif ( measure_idx == 2 ) :
            print('trying method 2 - Likelihood ratio')
            found_4 = finder4.nbest(  fourgram_measures.likelihood_ratio, 20)
        elif ( measure_idx == 3 ) :
            print('trying method 3 - Raw Frequency')
            found_4 = finder4.nbest(  fourgram_measures.raw_freq, 20)
        elif ( measure_idx == 4 ) :
            print('trying method 4 - Chi-Squared')
            found_4 = finder4.nbest(  fourgram_measures.chi_sq, 20)
        else :
            print('none of the above')
        print("Printing the QuadGrams:")
        for idx in range(0, len(found_4)):
            print('idx = ', idx, ' | == ', found_4[idx] )

    # print(finder4)
    print("Done testing different methods....")

    # converts the words in word_tokens to lower case
    filtered_doc = [x.lower() for x in tokenized]

    # create a frequency distribution to get top words:
    fdist = FreqDist(filtered_doc)


    print( 'CLEARING THE OUTPUT LINE ----------------------------------------------------' )
    # Get me a list of the most common 20 words:
    # The method most_common( ) returns the N numbers.
    # But NOT the strings themselves.
    #
    # Now we could use a list comprehension...
    # tokens_without_sw = [ word for word in text_tokens if not word in all stopwords]
    #
    common_tuples               = fdist.most_common(N_SINGLE_TUPLES_TO_GET_PER_DOC)

    sorted_dict = Sort_Dict_of_Integers( dict(common_tuples) )

    # There are only about 180 stop words.
    # So, for each stop word, delete it from the dictionary:
    for sw in stop_words:
        if ( sw in sorted_dict.keys()):
            del sorted_dict[ sw ]

    for key_in_dictionary in sorted_dict.keys():
        numeric_value = sorted_dict[ key_in_dictionary ]
        print("key_in_dict={:15s}".format( key_in_dictionary ), 'value=', numeric_value)

    # Print the tabulated list
    # print(fdist.tabulate(20))
    print('=== DEBUGGING:')
    if ( 'mahalanobis' in sorted_dict.keys() ):
        print('mahalanobis occurs: {:3d} times'.format(sorted_dict['mahalanobis']) )
    else:
        print('mahalanobis does not occur in this set of words.')
    if ( 'regularization' in sorted_dict.keys() ):
        print('regularization occurs: {:3d} times'.format(sorted_dict['regularization']) )
    else:
        print('regularization does not occur in this set of words.')

    print('=== DEBUGGING:')

    print("break here")


if ( __name__ == "__main__" ) :
    transcript_file = '../TEST_SUITE/CS420_2221_10117_2022-11-16.docx'          # "Mahalanobis" happens 6 times.
    comparison_file_or_stats = '../TEST_SUITE/Baseline_Words.docx'        	# For comparison
    print("Later on we will add argument parsing here.")
    print("This IS main.  Calling the main routine.")
    main( transcript_file, comparison_file_or_stats )
else:
    print("This is NOT main.  Nevermind.  Quitting.")




