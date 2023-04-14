
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
def unigram_analysis( tokenized ):
    unigrams  = []
    main_text = []
    temp_dict = []
    words_said = '';

#     separate_input_lines = tokenized.splitlines( )
#     for line_idx in range(0,len(separate_input_lines)):
#         the_input_line = separate_input_lines[line_idx]
#         if ( len(the_input_line) <= 1 ):
#             continue             # Skip this line, it only has a newline on it.
# 
#         # print('\n=================  TOP OF MAIN LOOP PER LINE =================')
#         #
#         # print('Working on line ',  line_idx )
#         # print('Input = ',          the_input_line )
# 
#         # ########################################################
#         #
#         # Some transcribers only put one space after the colon.
#         # So we need to carefully match the expression:
#         # (one or more characters that are NOT colons)(a colon, followed by one or more whitespace chars)(spoken text)
#         #
#         matched_expressions = re.match( '(^[^:]+)(:\s+)(.*)', the_input_line )
# 
#         if ( matched_expressions is not None ):
#             print('There is a speaker Match Here:')
#             the_speaker = matched_expressions.group(1)
#             # print('Group 2 is: ', matched_expressions.group(2) )	# The ': *' separator.
#             words_said  = matched_expressions.group(3)
#         else:
#             words_said = the_input_line
# 
#         main_text = main_text + ' ' + words_said      # Append these words to a spoken stream of words:
# 
#     print('\n=================  BOT OF MAIN LOOP -- DONE PROCESSING THIS LINE =================')
#     print('Break here outside the loop')
#    
#     #
#     # Go through the main text, and then decide which words are important: 
#     # 
#     # The second parameter gives a regular expression to use to match
#     # a "word".  So, in this case, a word can contain a hypen, or an underscore,
#     # but NOT a period.
#     tokenized    = regexp_tokenize(main_text, r'[-a-zA-Z0-9_]+')       # No periods.
# 
#     word_counter = dict()
#     for idx in range(0,len(tokenized)):
#         one_word = tokenized[idx];
#         print( "one word = ", one_word )
# 
