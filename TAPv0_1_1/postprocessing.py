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
