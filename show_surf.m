img1 = '/home/tommy/Desktop/db_project/lfw/Alan_Greenspan/Alan_Greenspan_0002.jpg';
img2 = '/home/tommy/Desktop/db_project/lfw/Alan_Greenspan/Alan_Greenspan_0005.jpg';

img = imread( img2 );
img = rgb2gray( img );

points = detectSURFFeatures( img );

[descriptors , coords] = extractFeatures( img, points, 'SURFSize', 64 );

imshow(img2); hold on;
strongestPoints = coords.selectStrongest(5);
strongestPoints.plot('showOrientation',true);
