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
ORDER BY total_amt DESC;

-- Q4) Write a query that shows: user_id, user_name (cleaned: trimmed + lowercased), city (NULLs replaced with 'Unknown')
-- The count of their successful transactions (use LOWER(TRIM(status)) = 'success' to catch all variations)

SELECT users.user_id,
	LOWER(TRIM(user_name)) AS clean_name,
	COALESCE(city, 'Unknown') AS city_clean,
	COUNT(*) AS successful_trans
FROM users
JOIN transactions
	ON users.user_id = transactions.user_id
WHERE LOWER(TRIM(status)) = 'success'
GROUP BY users.user_id, user_name, city
HAVING COUNT(*) >= 1
ORDER BY COUNT(*) DESC ;

-- Quick reference first - the three COUNT variants:
SELECT COUNT(*) FROM transactions;
SELECT COUNT(amount) FROM transactions;
SELECT COUNT(DISTINCT user_id) FROM transactions;


-- Q5) For each cleaned status (use LOWER(TRIM(status))), show:
-- The cleaned status
-- COUNT(*) — total rows for that status
-- COUNT(amount) — how many have a non-NULL amount
-- COUNT(DISTINCT user_id) — how many unique users made transactions with that status
-- Order by COUNT(*) descending. Give all columns meaningful aliases.

SELECT LOWER(TRIM(status)) AS cleaned_status,
	COUNT(*) AS total_count,
	COUNT(amount) AS no_null_amount,
	COUNT(DISTINCT user_id) AS unique_users
FROM transactions
GROUP BY cleaned_status
ORDER BY COUNT(*) DESC;

-- Q6) An interviewer asks you: "How many unique users have made at least one successful transaction?"
-- Write a single query that returns just that number. Think about which COUNT variant gives you "unique users."

SELECT COUNT(DISTINCT user_id) AS unique_success_users
FROM transactions 
WHERE LOWER(TRIM(status)) = 'success'
;


-- Q7) Write a query that shows each user_id and how many different merchants they've transacted with. 
-- Only count successful transactions (normalized status). 
-- Only show users who have transacted with more than 1 different merchant.
SELECT user_id,
	COUNT(DISTINCT merchant_id) AS unique_merchant
FROM transactions
WHERE LOWER(TRIM(status)) = 'success'
GROUP BY user_id
HAVING COUNT(DISTINCT merchant_id) > 1
ORDER BY unique_merchant DESC;

-- Q8) Write ONE query that shows, for each user who has at least 2 successful transactions:
-- user_id
-- Total number of successful transactions (COUNT(*))
-- Number of those with a non-NULL amount (COUNT(amount))
-- Number of unique merchants they've successfully transacted with (COUNT(DISTINCT merchant_id))
-- Total successful amount (SUM(amount))
-- Order by total amount descending. This combines all three COUNT variants + SUM + GROUP BY + HAVING

SELECT user_id,
	COUNT(*) AS success_trans,
	COUNT(amount) AS no_null_amt,
	COUNT(DISTINCT merchant_id) AS unique_merchants,
	SUM(amount) AS total_amt
FROM transactions
WHERE LOWER(TRIM(status)) = 'success'
GROUP BY user_id
HAVING COUNT(*) >= 2
ORDER BY total_amt DESC;

