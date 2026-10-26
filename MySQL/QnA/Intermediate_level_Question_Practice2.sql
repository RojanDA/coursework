-- Return the 10 most recently registered customers, showing their ID, name, city, and signup date. 
-- Sort newest first
SELECT customer_id, first_name, last_name as full_name, city, signup_date
FROM customers
ORDER BY signup_date DESC, customer_id DESC
LIMIT 10;


-- Find products priced between $20 and $80 inclusive whose names contain “belt” or “mug.” 
-- Sort by price from lowest to highest.
-- Return: product_name, category, list_price
-- tables: Products
SELECT product_name, 
category, 
list_price
FROM products
WHERE (product_name LIKE '%belt%' OR product_name LIKE '%mug%') 
	AND list_price BETWEEN 20 AND 80
ORDER BY list_price;


-- Tables: customers
-- A. List each customer city once, alphabetically.
SELECT DISTINCT city
FROM customers
ORDER BY city ASC;

-- B. Report the total number of customers and how many have a recorded gender.
SELECT COUNT(*) AS total_customers,
       COUNT(gender) AS customers_with_gender
FROM customers;


-- Tables: orders
-- A. List pending or processing orders dated January 1, 2025 or later, oldest first.
SELECT order_status, 
order_date
FROM orders
WHERE order_status	IN ('pending','processing')
	AND order_date >= '2025-01-01'
ORDER BY order_date ASC; 

-- B. Count orders in each status.
SELECT order_status, 
COUNT(order_status) AS order_count
FROM orders
GROUP BY order_status;


-- 5. Delivered sales by year and order size
-- For delivered orders, label each order Small (under $100), 
-- Standard ($100 to under $300), or Large ($300 or more). 
-- Then report order count and revenue by year and size band.
-- Return: order_year, order_value_band, order_count, revenue
-- Tables: orders
SELECT YEAR(order_date) as order_year,
CASE
	WHEN total_amount < 100 THEN 'Small'
    WHEN total_amount < 300 THEN 'Standard'
    ELSE 'Large'
END AS order_value_band, 
count(*) order_count,
sum(total_amount) as revenue
FROM orders 
WHERE order_status = 'delivered'
GROUP BY YEAR(order_date), order_value_band;

-- Tables: orders, order_item
-- For delivered orders, report discounted and full-price line revenue and line counts. 
SELECT
    CASE
        WHEN order_items.discount_percent > 0 THEN 'Discounted'
        ELSE 'Full price'
    END AS price_type,
    SUM(order_items.line_revenue) AS total_line_revenue,
    COUNT(*) AS line_count
FROM orders
	JOIN order_items
		ON orders.order_id = order_items.order_id
WHERE orders.order_status = 'delivered'
GROUP BY price_type;
-- Also calculate the discount percentage for each order with a positive subtotal.
SELECT order_id,
       subtotal,
       discount_amount,
       ROUND(discount_amount / NULLIF(subtotal, 0) * 100, 2)
           AS discount_rate_percent
FROM orders
WHERE subtotal > 0;


-- Tables: customers, orders, order_items, products
-- A. Report order count and average order value by city and order status.
SELECT city, 
	orders.order_status,
	COUNT(*) AS order_count,
	ROUND(AVG(orders.total_amount), 2) AS average_order_value
FROM customers
JOIN orders
	ON customers.customer_id = orders.customer_id
GROUP BY customers.city, orders.order_status
ORDER BY customers.city, orders.order_status DESC;
-- B. Find product categories with at least $1,000 in delivered line revenue.
SELECT  category,
SUM(line_revenue) AS delivered_line_revenue
FROM products
JOIN order_items
	ON products.product_id = order_items.product_id
JOIN orders
	ON orders.order_id = order_items.order_id
WHERE orders.order_status = 'delivered'
GROUP BY category
HAVING SUM(line_revenue) >= 1000;





-- For delivered sales, report revenue, gross profit, and gross margin percentage by product,
--  sorted by gross profit highest first. 
--  Also list products priced above the average catalog price and 
--  show how far above average each is.
-- Tables: products, orders, order_items



-- A. Find customers with at least two delivered orders and report their delivered revenue.
-- B. Find orders with pending or failed payments, or a missing payment date; include the customer’s city and order total.
-- C. From the customers in part A, identify those whose delivered revenue is above the average customer total.
-- Tables: customers, orders, payments



-- Report delivered order count and revenue by month. 
-- Then return only months whose revenue is above the average monthly revenue.
-- Return: sales_month, delivered_order_count, monthly_revenue, average_monthly_revenue
-- Tables: orders