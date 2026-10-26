SELECT DISTINCT status FROM transactions;

-- Q1)Write a query that counts the total amount of ALL successful transactions 
-- - including 'Success', 'SUCCESS', ' success ', ' Success', and 'success'.

SELECT SUM(amount) AS total_success_amount
FROM transactions
WHERE LOWER(TRIM(status)) = 'success';

-- Q2) The users table now has messy names — extra spaces, 
-- mixed casing, and even an empty string ' ' as a name. 
-- Write a query that shows all user_name values

SELECT TRIM(LOWER(user_name)) AS clean_name,
	COALESCE(city, 'Unknown') AS city_clean
FROM users
ORDER BY user_id;

-- Q3let's combine everything. Write a query that shows:
-- For each cleaned status (use LOWER(TRIM(status)) to group all variations together)
-- The count of transactions for that status
-- The total amount for that status
-- Group by the cleaned status. Order by total amount descending.

SELECT LOWER(TRIM(status)) AS clean_status,
	COUNT(*), SUM(amount) AS total_amt
FROM transactions
GROUP BY LOWER(TRIM(status))
ORDER;
