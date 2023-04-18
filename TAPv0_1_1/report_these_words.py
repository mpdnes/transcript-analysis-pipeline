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
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    from PIL import Image

    wc = WordCloud(background_color="white", width=1000,height=1000, max_words=len(dict_of_all_words),
                   relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(dict_of_all_words)

    for word,freq in dict_of_all_words.items():
        print( "word = ", word, '\t\t', end='' )
        print( "freq = ", freq )

        return wc