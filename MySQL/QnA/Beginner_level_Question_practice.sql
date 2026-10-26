
-- 10 customers who signed up most recently
SELECT customer_id, 
first_name, 
last_name, 
city, 
signup_date 
FROM customers
ORDER BY signup_date desc
limit 10
;

-- List products with a list_price between $20 and $80
SELECT product_name, 
category, 
List_price 
FROM products
WHERE list_price BETWEEN 20 AND 80
ORDER BY list_price;

-- list of customer cities, with each city shown once and the list in alphabetical order.
SELECT distinct city 
FROM customers
ORDER BY city
;

-- orders that are still pending or processing, dated January 1, 2025 or later,
SELECT order_id, 
order_date, 
order_status, 
total_amount 
FROM orders
WHERE order_status IN ('pending', 'processing') 
AND order_date >= '2025-01-01'
ORDER BY order_date ASC;

-- products whose names contain “case” or “belt”
SELECT product_id,
product_name, 
category
FROM products
WHERE product_name LIKE '%case%'
   OR product_name LIKE '%belt%'
ORDER BY list_price;

-- Total number of customer records and Number of customers with a recorded gender
SELECT COUNT(*) total_customers, 
COUNT(gender) customers_with_gender
FROM customers;

-- number of orders in each order status.
SELECT order_status, 
count(order_id) order_count
FROM orders
Group BY order_status;

-- Label each delivered order based on total_amount
-- Small: under $100, Standard: $100 up to, but not including, $300, Large: $300 or more

SELECT order_id,
total_amount,
CASE
	WHEN total_amount < 100 THEN 'Small'
    WHEN total_amount < 300 THEN 'Standard'
    WHEN total_amount >= 300 THEN 'Large'
END AS order_value_band
FROM orders
WHERE order_status = 'delivered';

-- the number of delivered orders and their total revenue for each calendar year
SELECT year(order_date) order_year, 
COUNT(*) delivered_orders, 
sum(total_amount) delivered_order_revenue
FROM orders
WHERE order_status = 'delivered'
GROUP BY YEAR(order_date);

-- order with a positive subtotal, calculate the discount as a percentage of the subtotal

SELECT order_id,subtotal,discount_amount,
CASE
	WHEN subtotal > 0 THEN discount_amount / subtotal * 100
END AS discount_percent_of_subtotal
FROM orders
WHERE subtotal > 0;




