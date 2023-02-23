# Write your MySQL query statement below
SELECT firstName, lastName, City, state
FROM Person P
LEFT JOIN Address A
ON P.personId = A.personId