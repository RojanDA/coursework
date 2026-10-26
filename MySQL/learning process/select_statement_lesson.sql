SELECT * FROM parks_and_recreation.employee_demographics;

SELECT first_name,
last_name,
birth_date,
age,
age + 10 From parks_and_recreation.employee_demographics;

#pemdas 

SELECT DISTINCT gender FROM parks_and_recreation.employee_demographics; 

SELECT * FROM parks_and_recreation.employee_salary
WHERE salary > 70000;

SELECT * FROM parks_and_recreation.employee_demographics
WHERE gender != 'Female';

-- AND OR NOT -- LOGICAL OPERATOR

SELECT * FROM parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01' AND gender = 'male'; 

SELECT * FROM parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01' OR gender = 'male'; 

SELECT * FROM parks_and_recreation.employee_demographics
WHERE birth_date > '1985-01-01' OR NOT gender = 'male'; 

-- LIKE STATEMENT
SELECT * FROM parks_and_recreation.employee_demographics
WHERE first_name LIKE 'Jer%'; 

SELECT * FROM parks_and_recreation.employee_demographics
WHERE first_name LIKE 'a___'; 

-- GROUP BY --

SELECT gender FROM parks_and_recreation.employee_demographics
GROUP BY gender; 

SELECT gender, AVG(age) FROM employee_demographics
GROUP BY gender; 

SELECT occupation, salary FROM employee_salary
GROUP BY occupation, salary; 

SELECT gender, AVG(age), MAX(age), MIN(age), COUNT(age)
FROM employee_demographics
GROUP BY gender;

-- aliasing 
#Help us to provide name
SELECT gender, AVG(age) AS avg_age, MAX(age)AS max_age, MIN(age) AS min_age, COUNT(age) AS total_row
FROM employee_demographics
GROUP BY gender;

-- ORDER BY --

SELECT *
FROM employee_demographics
ORDER BY first_name DESC;

SELECT *
FROM employee_demographics
ORDER BY first_name ASC;

-- HAVING VS WHERE

SELECT gender, AVG(age) FROM employee_demographics
GROUP BY gender
HAVING AVG(age) > 40;

SELECT occupation, AVG(salary)
from employee_salary
where occupation LIKE '%manager%'
GROUP BY occupation
HAVING AVG(salary) > 75000;

-- LIMIT --

SELECT * FROM employee_demographics
ORDER BY age DESC
LIMIT 3;

SELECT * FROM employee_demographics
ORDER BY age DESC
LIMIT 2,1;







