function Crop_0578( )
DEVELOPING = false;

    im = imread( 'SCAN0578.JPG' );

    zoom_figure( [ 2000 2000 ]);
    imagesc( im );
    axis image;

    if ( DEVELOPING )
    
        [xs,ys] = ginput();
    
        fprintf('  xs = [ ');
        fprintf('%6.2f, ', xs(:)' );
        fprintf(' ] \n' );
    
        fprintf('  ys = [ ');
        fprintf('%6.2f, ', ys(:)' );
        fprintf(' ] \n' );

    else
        xs = [ 188,  2353  ]; 
        ys = [ 226,  1241  ];
    
        im_cropped = im( ys(1):ys(2), xs(1):xs(2), :);
    
        imagesc( im_cropped );
        axis image;
    
        imwrite( im_cropped, 'SCAN0578__cropped.jpg', 'JPEG', 'Quality', 98 );
    end

end

