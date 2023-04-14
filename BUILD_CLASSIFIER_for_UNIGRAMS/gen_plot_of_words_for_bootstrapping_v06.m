
function gen_plot_of_words_for_bootstrapping_v06()
FS = 24;
MS = 10;

    fn_in = "DEBUGGING_FILE_FOR_CLASSIFYING_UNIGRAMS.csv";

    dt = readtable( fn_in );

    [n_rows,n_cols] = size( dt );

    for row_index = 1 : n_rows
        this_row    = dt(row_index, :);
        n_occurrances(row_index)    = this_row.N_OCCURRANCES;
        n_word_length(row_index)    = this_row.LENGTH;
        class_id(row_index)         = this_row.CLASS;
    end

    %
    %  Plot each of the class ID's on the same plot:
    %
    zoom_figure( [1900 1100] );

    class_values = [ 0, -1, 1 ];

    class_labels = { 'NA', 'Unimportant', 'Important' };

    colors = 'wrbk';
    for idx = 1 : length(class_values)
        c_id    = class_values(idx);
        color   = colors(idx);
        b_these = class_id == c_id;
        xs      = n_word_length(b_these);
        ys      = n_occurrances(b_these);
        x_jitter = (rand(size(xs))-0.5)*0.8;
        y_jitter = (rand(size(ys))-0.5)*0.8;

        plot( xs+x_jitter, ys+y_jitter, 'ko', 'MarkerFaceColor', color, 'MarkerSize', MS);
        hold on;
        xlabel('Word Length', 'FontSize', FS );
        ylabel('Word Frequency', 'FontSize', FS );
        set(gca,'Position',[0.05 0.05 0.9 0.9] );
    end 
    
    legend( class_labels, 'Location', 'NorthWest', 'FontSize', FS  );

    classifier_slope        = -4.35;
    classifier_intercept    = 30.067;
    xs                      = [ 0, 7 ];
    ys                      = classifier_slope * xs + classifier_intercept;
    hold on;
    plot( xs, ys, 'k--', 'LineWidth', 2);
    axis([ 0 18 0 50]);

    guess_id    = run_classifier( n_word_length, n_occurrances );



end




function guess_this_is_important = run_classifier( n_word_length, n_occurrances_in_this_lecture )
    classifier_slope        = -4.35;
    classifier_intercept    = 30.067;


    linear_regression_predicted_threshold_of_importance     = n_word_length * classifier_slope + classifier_intercept)

    guess_this_is_important = n_occurrances_in_this_lecture > linear_regression_predicted_threshold_of_importance;

end

