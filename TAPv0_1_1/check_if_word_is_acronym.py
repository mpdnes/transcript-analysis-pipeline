
import re 				# regular expressions

#
#  Return true if this word is an acronym
#
#  Acronyms must be three to seven characters.
#
def check_if_word_is_acronym( only_one_string ) :
    rc = False		# Default return code
    # Check for names: Mahalanobis:
    if ( re.match( '^[A-Z][a-z][a-z]+', only_one_string ) ) :
        rc = False				# Is a name
    elif ( len( only_one_string ) <= 6 ) and re.match( '^[A-Z]([a-zA-Z]{2,5})', only_one_string ) :
        rc = True
 
    return rc


#
#  Code to do unit testing on this:
#
def main() :

   test_lst = [ 'ABC', 'FLD', 'DoC', 'Tom', 'not', 'nul', 'of', 'two', 'three', 'PSF', 'Covariance' ]

   for idx in range( 0, len(test_lst) ):
       b_temp = check_if_word_is_acronym( test_lst[idx] )
       print(test_lst[idx], '\treturns ', b_temp )

if ( __name__ == "__main__" ) :
    print("Running unit text for acronym finder")
    main()
else: 
    print("this is NOT main")


