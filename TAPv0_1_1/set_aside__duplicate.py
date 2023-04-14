# 
# 
#         # ########################################################
#         #
#         # Some transcribers only put one space after the colon.
#         # So we need to carefully match the expression:
#         # (one or more characters that are NOT colons)(a colon, followed by one or more whitespace chars)(spoken text)
#         #
#         b_is_speaker = re.search(':\s+', the_input_line )
#         matched_expressions = re.match( '(^[^:]+)(:\s+)(.*)', the_input_line )
# 
#         if ( matched_expressions is not None ):
#             print('There is a speaker Match Here:')
#             # print('Group 0 is: ', mmm.group(0) )	# This is the entire line.
#             # print('Group 1 is: ', matched_expressions.group(1) )	# The first group matched.
#             # print('Group 2 is: ', matched_expressions.group(2) )	# The ': *' separator.
#             # print('Group 3 is: ', matched_expressions.group(3) )	# The rest of the line.
#             # print(' ')
#             the_speaker = matched_expressions.group(1)
#             words_said  = matched_expressions.group(3)
#             print('speaker: ', the_speaker, ' says ', len(words_said), ' characters')
#         else:
#             # print('(The Speaker)(:  )(Text) pattern did not match.' )
#             words_said = the_input_line
# 
#         if ( len(main_speaker) == 0 ) and ( len(the_speaker) > 0 ):
#             # THIS ONLY HAPPENS ONCE.
#             # The first time this happens,
#             # record the first speaker as the name of the main speaker.
#             # This only happens once.
#             #
#             # TODO:
#             # We assume that the instructor is the the main speaker.
#             # Later on, expand to a sub-set of legal names for the main speaker.
#             # The set: instructor, speaker, professor
#             main_speaker = the_speaker +'' # Force a deep copy  TODO check later if we can ignore this.
# 
#         # If the speaker is the main speaker, record the words said:
#         if ( the_speaker is not None ) and ( len( the_speaker ) > 0 ) and (len(main_speaker) > 0) and ( the_speaker == main_speaker ):
#             main_text = main_text + ' ' + words_said      # Append these words to a spoken stream of words:
#         #         if ( b_is_speaker ):
#         #             print('Span of the match is: ', b_is_speaker.span())
#         #             the_speaker   = the_input_line[ 0 : b_is_speaker.span(0)[0] ] # Get a slice:
#         #             words_said    = the_input_line[ b_is_speaker.span(0)[1] : -1 ]
#         #         else:
#         #             # This text goes with the last speaker:
#         #             print('no speaker set on line: ', line_idx )
#         #             print('==>', the_input_line, '<==')
# 
#         # print("break here at the bottom of the loop")
#     print('\n=================  BOT OF MAIN LOOP -- DONE PROCESSING THIS LINE =================')
#     print('Break here outside the loop')
# 
#     # TODO -- filter out  "*** TypeWell transcription provides a meaning-for-meaning" as not valid input.
# 
#     #
#     #  Now process the "main_text" and tokenize it...
#     #
#     # remove stopwords from predefined stopwords list
#     # stopwords = set(stop_words.words('english'))
#     #
#     # #Clean up data
#     # tokenized = re.sub("\t", "" , tokenized)
#     # tokenized = re.sub("\n\n\n", "\n\n", tokenized)
# 
#     # Tokenize document by sentence and delete header
#     #
#     # The second parameter gives a regular expression to use to match
#     # a "word".  So, in this case, a word can contain a hypen, or an underscore,
#     # but NOT a period.
#     tokenized = regexp_tokenize(main_text, r'[-a-zA-Z0-9_]+')       # No periods.
#     # Debug:
#     print( 'Number of tokens = ', end='')
#     print( len( tokenized  ))
#     # print("DELETING:", end='')
#     # print( tokenized[0] )       # Debugging code
#     # del tokenized[0]
#     # del tokenized[0]
#     # TODO: Add back the idea of deleting the header lines.
#     #
# 
#     #convert document to lowercase
#     #tokenized = [w.lower() for w in tokenized]
#     # tagged = []
# 
#     # Label each word with the parts of speech (POS):
#     tagged 	= nltk.pos_tag(tokenized)
#     print( tagged )
#     #
#     # #
#     # counts 	= Counter(tag for word, tag in tagged)
#     # print(counts)
#     # print(tagged)
# 
# 
