SELECT s1.id, s1.label, s2.label, ST_Distance(s1.features, s2.features)
FROM sample_mpoints s1
LEFT JOIN sample_mpoints s2
ON ST_DWithin(s1.features, s2.features, 0.1)
WHERE s1.id != s2.id
AND s1.id <= 500
ORDER BY s1.id, ST_Distance(s1.features, s2.features);
