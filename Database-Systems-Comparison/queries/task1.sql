SELECT normalized_category AS category, SUM(review_count) AS total_reviews
FROM (SELECT ARRAY_TO_STRING(ARRAY_AGG(DISTINCT TRIM(c)), ', ') AS normalized_category, b.review_count
      FROM business b, regexp_split_to_table(b.categories, ',') AS c
      GROUP BY b.business_id, b.review_count) AS normalized
GROUP BY normalized_category
ORDER BY total_reviews DESC
LIMIT 10;