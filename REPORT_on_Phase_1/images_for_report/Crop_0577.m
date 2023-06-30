function Crop_0577( )


    im = imread( 'SCAN0577.JPG' );

    zoom_figure( [ 2000 2000 ]);
    imagesc( im );
    axis image;

% 
%     [xs,ys] = ginput();
% 
%     fprintf('  xs = [ ');
%     fprintf('%6.2f, ', xs(:)' );
%     fprintf(' ] \n' );
% 
%     fprintf('  ys = [ ');
%     fprintf('%6.2f, ', ys(:)' );
%     fprintf(' ] \n' );

    xs = [   175,  2404  ];
    ys = [   190,  1434  ]; 

    im_cropped = im( ys(1):ys(2), xs(1):xs(2), :);

    imagesc( im_cropped );
    axis image;

    imwrite( im_cropped, 'SCAN0577__cropped.jpg', 'JPEG', 'Quality', 98 );



end

