
function gen_plot_of_words_for_bootstrapping_v09()
FS = 24;
MS = 10;

    fn_in   = "DEBUGGING_FILE_FOR_CLASSIFYING_UNIGRAMS.csv";

    dt      = readtable( fn_in );

    [n_rows,n_cols] = size( dt );

    for row_index = 1 : n_rows
        this_row                    = dt(row_index, :);
        n_occurrances(row_index)    = this_row.N_OCCURRANCES;
        n_word_length(row_index)    = this_row.LENGTH;
        given_class_id(row_index)   = this_row.CLASS;
    end

    % Compute jitter for the entire vectors.
    % That way, after they are classified (correctly or incorrectly)
    % we can put circles around the points.
    x_jitter = (rand(size(n_word_length))-0.5)*0.8;
    y_jitter = (rand(size(n_occurrances))-0.5)*0.8;

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
        b_these = given_class_id == c_id;
        xs      = n_word_length(b_these);
        ys      = n_occurrances(b_these);

        plot( xs+x_jitter(b_these), ys+y_jitter(b_these), 'ko', 'MarkerFaceColor', color, 'MarkerSize', MS);
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

    %
    %  Run the classifier on the unigrams.
    %
    guess_important     = run_classifier_for_unigrams( n_word_length, n_occurrances );

    b_correct_hit       = ( guess_important == true  )  & ( given_class_id ==  1 );
    b_false_alarm       = ( guess_important == true  )  & ( given_class_id == -1 );

    b_correct_reject    = ( guess_important == false )  & ( given_class_id == -1 );
    b_miss              = ( guess_important ~= true  )  & ( given_class_id ==  1 );

    % Change colors to green:
    hold on;
    xs =    n_word_length(b_correct_hit) + x_jitter(b_correct_hit);
    ys =    n_occurrances(b_correct_hit) + y_jitter(b_correct_hit);
    plot( xs, ys, 'go', 'MarkerSize', MS+2, 'LineWidth', 2 );

    xs =    n_word_length(b_correct_reject) + x_jitter(b_correct_reject);
    ys =    n_occurrances(b_correct_reject) + y_jitter(b_correct_reject);
    plot( xs, ys, 'go', 'MarkerSize', MS+2, 'LineWidth', 2 );


    fprintf('\t\tCONFUSION\n');
    fprintf('\t\t\t\t   ACTUALLY\tACTUALLY\n');
    fprintf('\t\t\t\t  IMPORTANT\tNOT IMPORTANT\n');
    fprintf('Guess Important\t\t\t  %4d\t  %4d\n',   sum(b_correct_hit), sum(b_false_alarm) );
    fprintf('Guess NOT IMPORTANT\t\t  %4d\t  %4d\n', sum(b_miss),  sum(b_correct_reject) );

end
