SELECT *,  ST_Distance(s1.features, s2.features)
FROM sample_mpoints s1
LEFT JOIN sample_mpoints s2
ON ST_DWithin(s1.features, s2.features, 0.1)
WHERE s1.id != s2.id
AND s1.id = 1
ORDER BY ST_Distance(s1.features, s2.features);
