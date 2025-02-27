SELECT b.name AS business_name, 
    ARRAY_TO_STRING(ARRAY_AGG(DISTINCT TRIM(c)), ', ') AS normalized_category,
    b.stars AS highest_rating,
    b.review_count
FROM business b, regexp_split_to_table(b.categories, ',') AS c
GROUP BY  b.business_id
ORDER BY b.stars DESC, b.review_count DESC
LIMIT 10;
