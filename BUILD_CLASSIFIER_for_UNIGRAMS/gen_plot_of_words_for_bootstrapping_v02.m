
function gen_plot_of_words_for_bootstrapping_v02()
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

    class_values = [ 1, 0, -1 ];

    class_labels = { 'Important', 'Meh', 'Unimportant'};

    colors = 'bwrm';
    for idx = 1 : length(class_values)
        c_id    = class_values(idx);
        color   = colors(idx);
        b_these = class_id == c_id;
        xs      = n_word_length(b_these);
        ys      = n_occurrances(b_these);
        x_jitter = (rand(size(xs))-0.5)*0.66;
        y_jitter = (rand(size(ys))-0.5)*0.66;

        plot( xs+x_jitter, ys+y_jitter, 'ko', 'MarkerFaceColor', color, 'MarkerSize', MS);
        hold on;
        xlabel('Word Length', 'FontSize', FS );
        ylabel('Word Frequency', 'FontSize', FS );

    end 
    
    legend( class_labels, 'Location', 'NorthWest', 'FontSize', FS  );

end
