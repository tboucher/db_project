function [feature_matrix] = load_files ( )
    
    stat_file = '/home/tommy/Desktop/db_project/lfw-names.txt';
    img_dir = '/home/tommy/Desktop/db_project/lfw/';

    [names, count] = textread(stat_file, '%s %d');
    
    feature_matrix = [];

    for i = 1:size(count,1)
        if count(i) == 5
            tmp_dir = dir( strcat( img_dir, names{i}, '/*.jpg' ) );
            for j = 1:length(tmp_dir)                
                tmp_img_path = strcat( img_dir, names{i}, '/', tmp_dir(j).name );
                tmp_img = imreadbw( tmp_img_path );
                tmp_points = detectSURFFeatures( tmp_img );
                [tmp_descriptors , tmp_coords] = extractFeatures( tmp_img, tmp_points, 'SURFSize', 128 );
                person_num = ones(size(tmp_descriptors,1),1)*i;
                img_num = ones(size(tmp_descriptors,1),1)*j;
                feature_matrix = [feature_matrix;person_num, img_num, tmp_descriptors];
            end
        end
    end

    %dlmwrite(strcat( img_dir, 'feature_matrix.csv' ), feature_matrix)

end