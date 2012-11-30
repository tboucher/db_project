% extract features from all photos of people with exactly 5 photos

function [feature_matrix] = extract_surf_feat ( )
    
    img_dir       = '/home/tommy/Desktop/db_project/lfw/';
    stat_file     = 'lfw-names.txt';

    [names, count] = textread(strcat( img_dir, stat_file ), '%s %d');
    
    feature_matrix = [];

    for i = 1:size(count,1)
        if count(i) == 5
            tmp_dir = dir( strcat( img_dir, names{i}, '/*.jpg' ) );
            for j = 1:length(tmp_dir)                
                tmp_img_path = strcat( img_dir, names{i}, '/', tmp_dir(j).name );
                tmp_img = imread( tmp_img_path );
                tmp_img = rgb2gray( tmp_img );
                tmp_points = detectSURFFeatures( tmp_img );
                [tmp_descriptors , tmp_coords] = extractFeatures( tmp_img, tmp_points, 'SURFSize', 128 );
                person_num = ones(size(tmp_descriptors,1),1)*i;
                img_num = ones(size(tmp_descriptors,1),1)*j;
                feature_matrix = [feature_matrix;person_num, img_num, tmp_descriptors];
            end
        end
    end

    dlmwrite(strcat( img_dir, '../', 'feature_matrix.csv' ), feature_matrix)
end