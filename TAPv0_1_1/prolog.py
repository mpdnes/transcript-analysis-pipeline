#
#  STANDARD PROLOG -- includes cruft
#

import re 				        # Regular expression matching.
import docxpy			    		# Handling *.docx file in python.

import nltk			                # Natural Language Toolkit
from nltk.corpus import stopwords		# Common stopwords.
import contractions			        # Common language contractions.

from nltk.tokenize import word_tokenize 	# Tokenizer
from nltk.tokenize import sent_tokenize		# ??? Sentence Tokenizer??

from collections import Counter			# Types of collections.

# tokenize document by sentence, under regular expression control.
from nltk import regexp_tokenize


