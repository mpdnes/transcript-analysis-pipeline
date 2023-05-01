import csv
import os
import sys

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

    for doc in list_of_all_tf_dicts:
        docs_read += 1
        for word in doc:

            if word in dict(list_of_words_with_idf):
                print("word " + str(word) + " already in list")
                continue
            else:
                i = 0
                num_docs_containing_word = 0
                while i < num_docs:
                    if word in list_of_all_tf_dicts[i]:
                        num_docs_containing_word += 1
                        i+=1
                    else:
                        i+=1

            word_with_count = word, num_docs_containing_word
            list_of_words_with_idf.append(word_with_count)

    return list_of_words_with_idf, num_docs

def zipfs_law_scaling(list_of_words_with_idf,total_num_docs):
    import math
    scaled_list_of_words_with_idf = []
    for word,count in list_of_words_with_idf:
        scaled_count = math.log(total_num_docs/count)
        list_addition = (word,scaled_count)
        scaled_list_of_words_with_idf.append(list_addition)

    return scaled_list_of_words_with_idf

def compute_tf_idf(term_freq_list,scaled_idf):
    computed_idf_dict = {}
    words_idk = []
    import math
    for key in term_freq_list:
        if key in scaled_idf:
            computed_idf_dict[key] = term_freq_list[key] * scaled_idf[key]
        else:
            words_idk.append(key)

    print("test")

    return computed_idf_dict



