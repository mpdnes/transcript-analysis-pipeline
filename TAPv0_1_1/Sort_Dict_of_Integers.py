#
#  A python function to sort a dictionary of integers.
# 
#  Often dictionaries are used to count how often various words occur.
#  This causes a dictionary that is indexed by a string, or series of letters,
#  but contains how often each string occurs.  We want to know which of these
#  strings occur most often.
#
#  This function takes in a specific types of dictionary, a dictionary that has:
#  1.  keys that are strings, or whatever.
#  2.  values that are integers
#
#  Returns:  It returns a copy of the same dictionary, but sorted by the value
#            values, most frequent to least frequent.
#

def Sort_Dict_of_Integers(dict_param,sort_order=-1):
    """
    A python function to sort a dictionary of integers.
    :param dict_param: The dictionary to be sorted.
    :param sort_order: By default, in descending order.  -1 for descending.  +1 for ascending.
    :return:           sorted_dict.
    """
    #
    #  For why this works, see https://realpython.com/sort-python-dictionary/
    #
    if ( sort_order > 0 ):
        # Sort ascending:
        sorted_tuples = sorted(dict_param.items(), key=lambda item: item[1])
    else:
        # Sort descending:
        sorted_tuples = sorted(dict_param.items(), key=lambda item: item[1], reverse=True)

    # Convert the sorted tuples back into a dictionary before return:
    sorted_dict = dict( sorted_tuples )

    return sorted_dict

def main_test() :
    print("Testing the function Soft_Dict_of_Integers.")
    Random_Dict = {}
    Random_Dict['Doughnut']    = 50
    Random_Dict['EggPlant']    = 20
    Random_Dict['Apple']       = 90
    Random_Dict['Cherry']      = 60
    Random_Dict['Banana']      = 80

    print('Original Dict = ')
    print( Random_Dict )
   
    # SORT DESCENDING: 
    srtd_dict = Sort_Dict_of_Integers( Random_Dict )
    print('\nRETURNED TYPE = ', type( srtd_dict ) )

    print('\nReturned Sorted Dict In descending order: ')
    print( srtd_dict )
    for key in srtd_dict.keys():
        print("key {:12s}".format(key), '--> ', srtd_dict[ key ] )
    
    # SORT ASSCENDING: 
    srtd_dict = Sort_Dict_of_Integers( Random_Dict, +1 )
    print('\nReturned Sorted Dict In ascending order: ')
    print( srtd_dict )
    
    for key in srtd_dict.keys():
        print("key {:12s}".format(key), '--> ', srtd_dict[ key ] )

if ( __name__ == "__main__" ) :
    print("Calling the procedure to test the local function:")
    main_test()


