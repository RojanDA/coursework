-- Q1) For each merchant, show the merchant_id 
-- and the total amount of all their transactions. 
-- Order the results by total amount from highest to lowest.
SELECT merchant_id, SUM(amount) AS total_amount
FROM transactions
GROUP BY merchant_id
ORDER BY total_amount DESC;

-- CHECKING DISTINCT status 
SELECT DISTINCT status FROM transactions;

-- Q2) For each user, show the user_id 
-- and the number of successful transactions they have. 
-- Order by the count from highest to lowest.
SELECT user_id, COUNT(*) AS suc_trans
FROM transactions
WHERE status = 'success'
GROUP BY user_id
ORDER BY suc_trans DESC;


-- Q3) Show only the merchants whose total successful transaction amount is greater than 2000. 
-- Include merchant_id and the total amount. Order by total from highest to lowest.

SELECT merchant_id, SUM(amount) AS total_amount
FROM transactions
WHERE status = 'success'
GROUP BY merchant_id
HAVING SUM(amount) > 2000
ORDER BY total_amount DESC;

-- Q4) For each merchant AND each status combination, show the merchant_id, status, and the number of transactions.
-- Order by merchant_id ascending, then status ascending

SELECT merchant_id, 
status, 
COUNT(*) AS no_of_trans
FROM transactions
GROUP BY merchant_id, status
ORDER BY merchant_id ASC, status ASC;

-- Q5) (Verification habit)
-- (a) How many transactions have a NULL amount?
SELECT count(*)
FROM transactions
WHERE amount IS NULL;
-- (b) What are the distinct status values? 
SELECT DISTINCT status
FROM transactions;
-- (c) For each user, how many transactions do they have (all statuses combined)? Order by user_id ascending.
SELECT user_id, 
COUNT(*) AS null_amount_count
FROM transactions
GROUP BY user_id
ORDER BY user_id ASC;
-- This is the habit — you check data quality BEFORE you analyze. Show me all three!

-- Q6) For each status, show the status, the count of transactions, and the average amount. 
-- Order by average amount from highest to lowest
SELECT status, 
count(*) AS count_of_trans, 
AVG(amount) AS avg_amt
FROM transactions
GROUP BY status
ORDER BY avg_amt DESC;

-- Q7) Show the top 3 users by total successful transaction amount. 
-- Include user_id and total amount. Only include users who have at least 2 successful transactions.
SELECT user_id, 
SUM(amount) AS total_amt
FROM transactions
WHERE status = 'success'
GROUP BY user_id
HAVING count(*) >= 2
ORDER BY total_amt DESC
LIMIT 3
;














