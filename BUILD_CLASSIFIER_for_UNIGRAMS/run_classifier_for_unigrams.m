
function guess_this_is_important = run_classifier_for_unigrams( n_word_length, n_occurrances_in_this_lecture )
% Given a vector of how long a word is, and how often it occurs in this corpus, decide if it is important or not.

    % Empirically determined linear regression line to the threshold.
    % Above this threshold, the word is likely to be important.
    classifier_slope        = -4.35;            
    classifier_intercept    = 30.067;


    linear_regression_predicted_threshold_of_importance     = n_word_length * classifier_slope + classifier_intercept;

    guess_this_is_important = n_occurrances_in_this_lecture > linear_regression_predicted_threshold_of_importance;

end