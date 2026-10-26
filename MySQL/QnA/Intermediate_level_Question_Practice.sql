-- compare order volume and average order value for each city and order status combination
SELECT city, order_status, 
count(*) order_count, 
ROUND(AVG(orders.total_amount),2) average_order_value
FROM customers
JOIN orders
	ON customers.customer_id = orders.customer_id
GROUP BY city, order_status
ORDER BY city ASC;

-- product categories with at least $1,000 in delivered line revenue
SELECT category, 
SUM(line_revenue) delivered_line_revenue
FROM orders
JOIN order_items
	ON orders.order_id = order_items.order_id
    JOIN products
		on order_items.product_id = products.product_id
WHERE order_status = 'delivered'
GROUP BY category
HAVING SUM(line_revenue) >= 1000;

-- For delivered orders, compare discounted and full-price order lines
SELECT 
	SUM(
		CASE
			WHEN order_items.discount_percent > 0
            THEN order_items.line_revenue
            ELSE 0
		END) discounted_line_revenue,
	SUM(
		CASE
			WHEN order_items.discount_percent = 0
            THEN order_items.line_revenue
            ELSE 0
		END) full_price_line_revenue,
	SUM(
		CASE
			WHEN order_items.discount_percent > 0
            THEN 1
            ELSE 0
		END) discounted_line_count,
	SUM(
		CASE
			WHEN order_items.discount_percent = 0
            THEN 1
            ELSE 0
		END) full_price_line_count
FROM orders
JOIN order_items
	ON orders.order_id = order_items.order_id
WHERE orders.order_status = 'delivered';

-- delivered revenue, gross profit, and gross margin percentage for each product, 
-- sorted by gross profit from highest to lowest
SELECT products.product_name, 
SUM(order_items.line_revenue) delivered_revenue,
SUM(order_items.gross_profit) gross_profit ,
ROUND( SUM(order_items.gross_profit) 
         / NULLIF(SUM(order_items.line_revenue), 0) * 100, 1
        ) gross_margin_percent
FROM orders
JOIN order_items
	ON orders.order_id = order_items.order_id
    JOIN products
		on order_items.product_id = products.product_id
WHERE order_status = 'delivered'
GROUP BY products.product_id, products.product_name
ORDER BY gross_profit DESC;

-- List each customer with at least two delivered orders, 
-- showing their delivered order count and total delivered revenue
SELECT customers.customer_id,
customers.first_name,
customers.last_name,
count(orders.order_status) delivered_order_count,
SUM(orders.total_amount) delivered_revenue
FROM customers
JOIN orders
	ON customers.customer_id = orders.customer_id
WHERE order_status = 'delivered'
GROUP BY customers.customer_id, 
customers.first_name, 
customers.last_name
HAVING COUNT(*) >= 2;

-- report the number of delivered orders and their total revenue
-- sales_month in YYYY-MM format
-- delivered_order_count, and completed_order_revenue.
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    COUNT(*) AS delivered_order_count,
    SUM(total_amount) AS completed_order_revenue
FROM orders
WHERE order_status = 'delivered'
GROUP BY sales_month
ORDER BY sales_month; 

-- orders with a pending or failed payment, or with no payment date. 
-- Include the customer’s city and the order and payment details.
-- order_id, city, order_status, payment_status, payment_date, total_amount

SELECT payments.order_id,
customers.city,
orders.order_status,
payments.payment_status,
payments.payment_date,
orders.total_amount
FROM payments
JOIN orders
	ON payments.order_id = orders.order_id
    JOIN customers
		ON orders.customer_id = customers.customer_id
WHERE payments.payment_status IN ('pending', 'failed')
   OR payments.payment_date IS NULL; 
   
-- Find customers whose total delivered-order revenue is higher 
-- than the average customer total.
-- Return: customer_id and delivered_revenue

SELECT customer_id, delivered_revenue
From (
	SELECT customer_id,
		SUM(total_amount) delivered_revenue
	FROM orders
    WHERE order_status = 'delivered'
    GROUP BY customer_id
) customer_totals
WHERE delivered_revenue > (
	SELECT AVG(delivered_revenue)
    FROM (
		SELECT customer_id, 
			SUM(total_amount) delivered_revenue
        From orders
		WHERE order_status = 'delivered'
        group by customer_id
	) all_customer_totals
)
order by delivered_revenue Desc;

-- Find the months whose delivered-order revenue is higher 
-- than the average monthly delivered revenue 

WITH monthly_sales AS
(
	SELECT
		date_format(order_date, '%Y-%m') AS sales_month,
        sum(total_amount) as monthly_revenue
	From orders
    WHERE order_status = 'delivered' 
    AND order_date >= '2024-01-01'
	AND order_date < '2026-01-01'
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT sales_month,
monthly_revenue,
(SELECT AVG(monthly_revenue) FROM monthly_sales) avg_monthly_revenue
FROM monthly_sales
WHERE monthly_revenue > (
	SELECT AVG(monthly_revenue)
    FROM monthly_sales
    )
ORDER BY sales_month;

-- Find products whose list_price is higher than the average list price across all products. 
-- Show how much each is above the average.

select 
	product_id,
    product_name, 
    list_price,
    ROUND((SELECT AVG(list_price) FROM products), 2) AS catalog_average_price,
    ROUND(list_price - (SELECT AVG(list_price) FROM products),2) AS amount_above_average
from products
WHERE list_price > (SELECT AVG(list_price) FROM products)
ORDER BY amount_above_average DESC;





