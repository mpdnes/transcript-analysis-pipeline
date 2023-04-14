# ##############################################################################
#
# Find number of speaker transitions:
#
# 1.  There is a dictionary entry for each speaker, 
#     with the number of words that they speak.
#
# 2.  The number of times that the speaker changes is also returned.
def analyze_speaker_frequency_and_xfers( tokenized ):
    dict_of_speakers      = dict()
    n_transitions         = 0
    return [dict_of_speakers, n_transitions]
