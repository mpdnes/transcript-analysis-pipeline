# ##############################################################################
#
#  Create a report:
#
def report_these_words( dict_of_all_words ):
    print( 'function ', __file__ , ' not fully written yet.' )
    # print('CALLED: report_these_words ')
    # print( 'Called with parameter of type: ', dict_of_all_words )
    # print('REPORT OF IMPORTANT WORDS: ')
    #
    # Python 3 has a new method.
    # AND, when working with keys, you must use both the key and the value in a for loop.
    # print( dict_of_all_words )
    for word,freq in dict_of_all_words.items():
        print( "word = ", word, '\t\t', end='' )
        print( "freq = ", freq )

    from wordcloud import WordCloud #package necessary to generate word cloud

    #these parameters can be modified to design the word cloud in whatever way we want.
    #there is a built in argument for stopwords, but STOPWORDS list is IGNORED when using generate_from_frequencies
    wc = WordCloud(background_color="white",            #white background color
    width = 1000,
    height = 1000,                                      #dimensions in pixels
    max_words = len( dict_of_all_words ),               #This probably needs to be modified.
    relative_scaling = 0.5 ).generate_from_frequencies( dict_of_all_words )
        #From Documentation: Importance of relative word-ranks are considered
        #With relative_scaling = 0, only word ranks are considered.
        #With relative_scaling=1, a word that is twice as frequent will
        #have twice the size.

    return wc
