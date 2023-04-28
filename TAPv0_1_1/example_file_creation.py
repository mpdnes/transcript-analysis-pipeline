#
#
#  QUICK PYTHON PROGRAM TO:
#
#

#import SYS

def read_in_files():
    # A routine to create a dictionary:
    my_local_dict = { 'Adam':1, \
                      'Bruce':2 , \
                      'Charlie':3, \
                      'David':4, \
                      'Edward':5 }
    my_local_dict.update( {'Frank':6} )

    return my_local_dict

def save_dict_to_csv(fn_out, my_dict):
    print("printing file out ", type(fn_out), " ", fn_out)
    print("second paramter is of type", type(my_dict))

    fp = open(fn_out, "w");
    for key, item in my_dict.items():
        string_to_print = key + "," + str(item) + "\n"
        fp.write(string_to_print)
    fp.close();


def main( fn_out ) :
    print("in main , doing the real work here.")

    my_dictionary = read_in_files( );
    
    fp = open( fn_out, "w" );
    for key,item in my_dictionary.items() :
        string_to_print = key+","+str(item)+"\n"
        fp.write( string_to_print )
    fp.close();
    

#
#  Standard boilerplate for Python:
#
if ( __name__ == "__main__" ) :
    print("calling main...")
    main( 'MY_NEW_FILENAME.csv' )
    print("done... ")
else: 
    print("this is NOT main")


