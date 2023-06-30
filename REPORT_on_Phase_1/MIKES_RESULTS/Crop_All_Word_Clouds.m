function Crop_All_Word_Clouds()

    % Files are in the current working directory:
    file_names = dir('Word_Cloud_*.png');

    % Crop all files:
    for file_idx = 1 : length( file_names )
        fn = file_names(file_idx).name;

        [~,bn,ext] = fileparts( fn );

        new_name = [ 'Cropped', bn, ext ];

        im_orig     = imread( fn );
        zoom_figure([2000 2000]);
        imagesc( im_orig ); 
        axis image;
        set(gcf,'Position', [10 10 1700 1110]);

        [xs, ys ] = ginput();

        % We are using image coordinates:
        ulh_xy  = [ floor(min(xs)), floor(min(ys)) ];
        lrh_xy  = [ ceil(max(xs)),  ceil(max(ys))  ];

        % Draw a box for visual feedback:
        boundary_xs     = [ ulh_xy(1), ulh_xy(1), lrh_xy(1), lrh_xy(1), ulh_xy(1) ];
        boundary_ys     = [ ulh_xy(2), lrh_xy(2), lrh_xy(2), ulh_xy(2), ulh_xy(2) ];

        hold on;
        plot( boundary_xs, boundary_ys, 'r-', 'LineWidth', 2 );

        pause(2);

        im_cropped  = im_orig( ulh_xy(2):lrh_xy(2), ulh_xy(1):lrh_xy(1), : );



        imwrite( im_cropped, new_name, 'PNG');


    end

end
