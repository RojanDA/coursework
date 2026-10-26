-- JOINS --

SELECT * 
FROM employee_demographics;

SELECT * 
FROM employee_salary;

-- INNER JOIN --

SELECT dem.employee_id,age,occupation 
FROM employee_demographics as dem
INNER JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    
-- OUTER JOIN --

SELECT * 
FROM employee_demographics as dem
LEFT JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    
SELECT *
FROM employee_demographics as dem
RIGHT JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    
-- SELF JOIN --

SELECT emp1.employee_id AS emp_santa,
emp1.first_name AS first_name_santa,
emp1.last_name AS last_name_santa,
emp2.employee_id AS emp_name,
emp2.first_name AS first_name,
emp2.last_name AS last_name
FROM employee_salary emp1
JOIN employee_salary emp2
	ON emp1.employee_id + 1 = emp2.employee_id;
    
-- unions -- 
SELECT first_name, last_name
FROM employee_demographics 
UNION 
SELECT first_name, last_name
FROM employee_salary;

SELECT first_name, last_name
FROM employee_demographics 
UNION ALL
SELECT first_name, last_name
FROM employee_salary;

SELECT first_name, last_name, 'old' AS label
FROM employee_demographics 
WHERE age > 50
UNION
SELECT first_name, last_name,'highly paid job' as label
FROM employee_salary
WHERE salary > 70000;

SELECT first_name, last_name, 'old man' AS label
FROM employee_demographics 
WHERE age > 40 and gender = 'male'
UNION 
SELECT first_name, last_name, 'old lady' AS label
FROM employee_demographics 
WHERE age > 40 and gender = 'female'
UNION
SELECT first_name, last_name,'highly paid job' as label
FROM employee_salary
WHERE salary > 70000
ORDER BY first_name,last_name;

-- STRING FUNCTION

SELECT LENGTH('skyfall');

SELECT first_name, LENGTH(first_name)
from employee_demographics
ORDER by 2;

SELECT UPPER('sky');
SELECT LOWER('SKY');

SELECT first_name, LEFT(first_name, 4), RIGHT(first_name, 4),
SUBSTRING(first_name,3,2),
birth_date,
SUBSTRING(birth_date,6, 2) as birth_month
FROM employee_demographics;

SELECT first_name, REPLACE(first_name,'a','z')
FROM employee_demographics;

SELECT LOCATE('x', 'ALEXANDER');

SELECT first_name, last_name, concat(first_name,' ',last_name) AS full_name
FROM employee_demographics;

-- CASE STATEMENT --

SELECT first_name, last_name, age,
CASE
	WHEN age <=30 THEN 'YOUNG'
    WHEN age BETWEEN 31 and 50 THEN 'old'
    WHEN age >= 50 THEN 'very old'
END AS age_bracket
FROM employee_demographics
order by age ASC;

SELECT first_name, last_name, salary,
CASE
	WHEN salary < 50000 THEN salary + (salary * 0.05)
    WHEN salary > 50000 then salary * 1.07
END AS new_salary,
CASE
	WHEN dept_id = 6 THEN salary * .10
END AS bonus
FROM employee_salary;

-- SUBQUERIES --

SELECT *
FROM employee_demographics
WHERE employee_id IN 
				(SELECT employee_id
                FROM employee_salary
                WHERE dept_id = 1)
;

SELECT first_name,salary,
(SELECT AVG(salary)
FROM employee_salary)
FROM employee_salary;

SELECT AVG(max_age)
FROM 
(SELECT gender,
AVG(age) as avg_age,
MAX(age) as max_age,
MIN(age) as min_age,
COUNT(age)
FROM employee_demographics
GROUP BY gender) as agg_table;


-- window FUnction --

SELECT dem.first_name,dem.last_name,gender,AVG(salary)
OVER(PARTITION BY gender)
FROM employee_demographics dem
JOIN employee_salary sal
		ON dem.employee_id = sal.employee_id;
        
SELECT dem.first_name,dem.last_name,gender, salary,
SUM(salary) OVER(PARTITION BY gender ORDER BY dem.employee_id) as rolling_total
FROM employee_demographics dem
JOIN employee_salary sal
		ON dem.employee_id = sal.employee_id;
        
SELECT dem.employee_id, dem.first_name, dem.last_name,gender, salary,
ROW_NUMBER() OVER(PARTITION BY gender ORDER BY salary desc),
RANK() OVER(PARTITION BY gender ORDER BY salary desc) as rank_num,
DENSE_RANK() OVER(PARTITION BY gender ORDER BY salary desc) as dens_rank_num
FROM employee_demographics dem
JOIN employee_salary sal
		ON dem.employee_id = sal.employee_id;
        








