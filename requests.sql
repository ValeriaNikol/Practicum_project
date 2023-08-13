SELECT с.login,
    COUNT(o.track)
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id=o."courierId"
WHERE o."inDelivery" = true
GROUP BY login; 

SELECT track,
    CASE
        WHEN finished = true THEN 2
        WHEN "canсelled" = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS "status"
FROM "Orders";