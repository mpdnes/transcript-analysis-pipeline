import csv
import os
import sys
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt



def csv_writer(termfreq,csv_file):


    return_code = os.path.isfile(csv_file)

    if return_code:
        print("---------------------------------------------------------------------------")
        print("DUMP_words.csv already exists, do you want to overwrite?")
        print("---------------------------------------------------------------------------")

        answer = input("Y/N >>")
        if answer == 'Y':
            with open(csv_file, "w") as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                writer.writerow(["Word","Term Freq"])
                writer.writerows(termfreq)
        else:
            print("---------------------------------------------------------------------------")
            print("File not overwritten. Exiting...")
            print("---------------------------------------------------------------------------")

            return_code = False
    else:
        print("---------------------------------------------------------------------------")
        print("DUMP_words.csv not found. Create this file?")
        print("---------------------------------------------------------------------------")
        answer = input("Y/N >> ")
        if answer == 'Y':
            with open(csv_file, "w") as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                writer.writerow(["Word", "Term Freq"])
                writer.writerows(termfreq)
                return_code = True
        else:
            return_code = False


    return return_code

def idf_calculator(list_of_all_tf_dicts):
    num_docs = len(list_of_all_tf_dicts)
    list_of_words_with_idf = []
    docs_read = 0

    #Combining all dictionaries.
    #Read each dictionary document in list of all docs, individually
    for doc in list_of_all_tf_dicts:
        #This keeps track of how many total documents there are to be used for idf calculation later.
        docs_read += 1
        #Now we're looking inside individual dictionaries to analyze each word.
        for word in doc:
            #Check to see if the word is already added.
            if word in dict(list_of_words_with_idf):
                print("word " + str(word) + " already in list")
                #If word is already in there, go to the next word.
                continue
            #If the word is not in the dictionary
            else:
                ii = 0
                num_docs_containing_word = 0

                #Find how many documents the word occurs in.
                #Starting at the first document, check to see if the word appears in the list of documents.
                while ii < num_docs:
                    if word in list_of_all_tf_dicts[ii]:
                        num_docs_containing_word += 1
                        ii+=1
                    else:
                        #I didn't find the word, don't count it!!
                        ii+=1

            word_with_count = word, num_docs_containing_word
            list_of_words_with_idf.append(word_with_count)

    return list_of_words_with_idf, num_docs

def zipfs_law_scaling(list_of_words_with_idf,total_num_docs):
    import math
    scaled_list_of_words_with_idf = []
    for word,count in list_of_words_with_idf:
        #Compute the tf-idf and then scale it according to Zipf's Law.
        scaled_count = math.log(total_num_docs/count)
        list_addition = (word,scaled_count)
        scaled_list_of_words_with_idf.append(list_addition)

    return scaled_list_of_words_with_idf

def compute_tf_idf(term_freq_list,scaled_idf):
    computed_idf_dict = {}
    words_idk = []
    import math

    #Wanted to make sure that I'm multiplying the same words from different dictionaries.
    for this_word in term_freq_list:
        if this_word in scaled_idf:
            computed_idf_dict[this_word] = term_freq_list[this_word] * scaled_idf[this_word]
        else:
            words_idk.append(this_word)

    return computed_idf_dict

def wordcloud_generator(dict_to_wordcloud):

    wc = WordCloud(background_color="white", width=1000, height=1000, max_words=40, relative_scaling=0.5,
                       normalize_plurals=False).generate_from_frequencies(dict_to_wordcloud)

    return wc



