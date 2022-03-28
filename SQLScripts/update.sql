UPDATE Business 
SET numCheckins = (SELECT COUNT(business_id) from CheckIn WHERE Business.business_id=CheckIn.business_id)

UPDATE Business
SET numTips=(SELECT COUNT(business_id) FROM Tips WHERE Business.business_id=Tips.business_id)

UPDATE Users SET tipCount = Totals.counts
FROM
(
    SELECT user_id, COUNT(user_id) counts
    FROM Tips
    GROUP BY Tips.user_id
) Totals
WHERE Users.user_id = Totals.user_id;

UPDATE Users SET total_likes = Totals.total_likes
FROM
(
    SELECT Tips.user_id, SUM(likes) total_likes
    FROM Tips
    GROUP BY user_id
) Totals
WHERE Users.user_id = Totals.user_id