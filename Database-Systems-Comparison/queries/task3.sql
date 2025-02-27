SELECT u.name AS user_name,
    COUNT(r.review_id) AS total_reviews,
    AVG(b.stars) AS avg_business_rating
FROM users u
INNER JOIN review r ON u.user_id = r.user_id
INNER JOIN business b ON r.business_id = b.business_id
WHERE b.stars >= 4.5
GROUP BY u.user_id, u.name
ORDER BY total_reviews DESC
LIMIT 10;
