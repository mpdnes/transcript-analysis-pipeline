

import docxpy
import os
from tqdm import tqdm
from nltk import *
import re
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

massive_tokenized_list = []
docs_to_be_changed = []


# for subdir, dirs, files, in os.walk(rootdir):
#     found_doc = glob.glob('*.doc')
#     docs_to_be_changed.append(found_doc)


rootdir = '/Users/mpdnes/Documents/GitHub/TAP/TEST_SUITE/DUMP'

for subdir, dirs, files in tqdm(os.walk(rootdir)):
    for docx in files:
            if docx == '.DS_Store':
                if docx.startswith('.'):
                    continue

            if not docx.endswith("docx"):
                docs_to_be_changed.append(docx)
                continue

            if docx.endswith("docx"):
                test = len(docx)
                if len(docx) ==11:

                    key_path = subdir + "/" + docx
                    read_doc = docxpy.process(key_path)
                    resulting_dict = dict()
                    ACK_dict = dict()  # Acronym dictionary
                    all_text_in_doc_str = ''
                    words_said = ''



                     # Analyze ALL LINES IN THIS DOCUMENT:
                    separate_input_lines = read_doc.splitlines()
                    for line_idx in range(0, len(separate_input_lines)):
                        the_input_line = separate_input_lines[line_idx]
                        if (len(the_input_line) <= 1):
                            continue  # Skip this line, it only has a newline on it.

        # ########################################################
        #
        # IGNORE THE SPEAKER:
        #
        # Some transcribers only put one space after the colon.
        # So we need to carefully match the expression:
        # (one or more characters that are NOT colons)(a colon, followed by one or more whitespace chars)(spoken text)
        #
                        matched_expressions = re.match('(^[^:]+)(:\s+)(.*)', the_input_line)

                        if (matched_expressions is not None):
                            # print('There is a speaker Match Here:')
                            the_speaker = matched_expressions.group(1)
                            # print('Group 2 is: ', matched_expressions.group(2) )	# The ': *' separator.
                            words_said = matched_expressions.group(3)
                        else:
                            words_said = the_input_line

                        all_text_in_doc_str = all_text_in_doc_str + ' ' + words_said  # Append these words to a spoken stream of words:

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

                    from pluralizer import Pluralizer
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

                    list_of_str__of_sep_words = regexp_tokenize(all_text_in_doc_str, r'[-a-zA-Z0-9_]+')

                    list_of_singular_sep_words = []
                    for single_words in list_of_str__of_sep_words:
                       list_of_singular_sep_words.append(pluralizer.singular(single_words))

                    from nltk.corpus import stopwords
                    stop_words = set(stopwords.words('english'))

                    filtered_list_of_singular_sep_words = []
                    for w in list_of_singular_sep_words:
                        if w not in stop_words:
                            filtered_list_of_singular_sep_words.append(w)

                        # note to self:   print('DEVELOPMENT: regexp_tokenize returns : ', type(list_of_str__of_sep_words) )
                         # note to self:   print( list_of_str__of_sep_words )
                          # note to self:   print('DEVELOPMENT: regexp_tokenize returns : a list of separate strings')

    # for all_items_in_list_of_strings
                    from check_if_word_is_acronym import check_if_word_is_acronym
                    for idx in range(0, len(filtered_list_of_singular_sep_words)):
                        this_word = filtered_list_of_singular_sep_words[idx]

                         # uniquely add to dict of acronyms
                         # If it was already identified as an acronym,
                         # do not bother to run the acronym classifier:
                        if (this_word in ACK_dict):
                            ACK_dict[this_word] = ACK_dict[this_word] + 1
                        else:
                                # If this looks like a valid acronym
                            if check_if_word_is_acronym(this_word) == True:
                                    ACK_dict[this_word] = 1
                            else:
                                    # Convert to lower case.
                                    #   Uniquely add to dictionary.
                                lc_word = this_word.lower()
                                if (lc_word in resulting_dict):
                                    resulting_dict[lc_word] = resulting_dict[lc_word] + 1
                                else:
                                    resulting_dict[lc_word] = 1

    #   for each word in dictionary of words: # Not the acronyms
    #       classify as important or not.
    #       delete unimportant words  (pop out of the dictionary )
                    merged_dict = dict(ACK_dict)
                    for each_word, each_freq in resulting_dict.items():
                        #print('Testing : ', each_word, ' which happens ', each_freq, ' times ')
                        this_word_is_important = classify_this_unigram_word_and_count(each_word, each_freq)
                        if this_word_is_important:
                            merged_dict[each_word] = each_freq

    # print('DEBUGGING: returning a type: ', end='')
    # print( type(merged_dict) )
                        big_boi_lsit = []
                        print('DEBUGGING: Dumping the dictionary')
                        for word, freq in merged_dict.items():
                            big_boi_lsit.append(word)

                            list(big_boi_lsit)







