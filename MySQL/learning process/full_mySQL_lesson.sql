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
        

-- CTES-- comment table expressions

WITH CTE_Example AS
(
SELECT gender, AVG(salary) avg_sal, MAX(salary) max_sal, MIN(salary) min_sal, COUNT(salary) count_sal
from employee_demographics dem
join employee_salary sal
	on dem.employee_id = sal.employee_id
group by gender
)
SELECT *
FROM CTE_Example
;

WITH CTE_Example AS
(
SELECT employee_id, gender, birth_date
from employee_demographics
WHERE birth_date >'1985-01-01'

),
CTE_Example2 AS
(
SELECT employee_id, salary
from employee_salary
WHERE salary > 50000
)
SELECT *
FROM CTE_Example
JOIN CTE_Example2
	ON CTE_Example.employee_id = CTE_Example2.employee_id
;

-- Temporary Tables

CREATE TEMPORARY TABLE Temp_table
(
first_name VARCHAR(50),
last_name VARCHAR(50),
favorite_movie VARCHAR(50)
);

INSERT INTO Temp_table
VALUES('ROJAN CHANDRA','POUDEL','SILENT VOICE');

SELECT * FROM Temp_table;

SELECT *
FROM employee_salary;

CREATE TEMPORARY TABLE salary_over_50k
SELECT *
FROM employee_salary
WHERE salary >= 50000;

SELECT * 
FROM salary_over_50k;


-- Stored Procedures

CREATE procedure large_salaries()
SELECT * 
FROM employee_salary
WHERE salary >= 50000;

CALL large_salaries();

DELIMITER $$
CREATE procedure large_salaries2()
BEGIN
	SELECT * 
	FROM employee_salary
	WHERE salary >= 50000;
	SELECT * 
	FROM employee_salary
	WHERE salary >= 10000;
END $$

DELIMITER ;

CALL large_salaries2();

DELIMITER $$
CREATE procedure large_salaries3(emp_id INT)
BEGIN
	SELECT salary
	FROM employee_salary
    WHERE employee_id = emp_id
	;
END $$
DELIMITER ;

CALL large_salaries3(1);

-- TRIGGERS AND EVENTS



DELIMITER $$
CREATE TRIGGER employee_insert
	AFTER INSERT ON employee_salary
    FOR EACH ROW 
BEGIN
	INSERT INTO employee_demographics (employee_id, first_name, last_name)
    VALUES(NEW.employee_id, NEW.first_name, NEW.last_name);
END $$
DELIMITER ;

INSERT INTO employee_salary (employee_id, first_name, last_name, occupation, salary, dept_id)
VALUES (13, 'Rojan Chandra','Poudel','Entertainment 720 CEO', 10000000, NULL);


-- Events --

SELECT *
FROM employee_demographics;

DELIMITER $$
CREATE EVENT delete_retirees
ON SCHEDULE EVERY 1 MONTH
DO
BEGIN
	DELETE
    FROM employee_demographics
    WHERE age >= 60;
END $$
DELIMITER ;

SHOW VARIABLES LIKE 'event%';

-- Data Cleaning --

SELECT *
FROM layoffs;


-- 1. Remove Duplicates
-- 2. Standardize the Data
-- 3. Null Values or Blank Values
-- 4. Remove Any Columns


-- copy data from raw data to staging database

CREATE TABLE layoff_staging
LIKE layoffs;

SELECT *
FROM layoff_staging;

INSERT layoff_staging
SELECT *
FROM layoffs;

-- 1. Remove Duplicates from data

SELECT *,
ROW_NUMBER() OVER(PARTITION BY 
company, industry, total_laid_off, percentage_laid_off, `date`) AS row_num
FROM layoff_staging;

WITH duplicate_cte AS
(
SELECT *,
ROW_NUMBER() OVER(PARTITION BY 
company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) AS row_num
FROM layoff_staging
)
SELECT *
FROM duplicate_cte
WHERE row_num > 1;

CREATE TABLE `layoff_staging2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO layoff_staging2
SELECT *,
ROW_NUMBER() OVER(PARTITION BY 
company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) AS row_num
FROM layoff_staging;

SELECT * 
FROM layoff_staging2
WHERE row_num>1;

DELETE
FROM layoff_staging2
WHERE row_num>1;

SELECT * 
FROM layoff_staging2;

-- 2. Standardize the Data

UPDATE layoff_staging
SET company = TRIM(company);

SELECT DISTINCT industry 
FROM layoff_staging2
ORDER BY 1;

SELECT *
FROM layoff_staging2
WHERE industry LIKE 'crypto%';

UPDATE layoff_staging2
SET industry = 'Crypto'
WHERE industry LIKE 'crypto%';

SELECT DISTINCT location 
FROM layoff_staging2
ORDER BY 1;

SELECT DISTINCT country
FROM layoff_staging2
ORDER BY 1;

SELECT *
FROM layoff_staging2
WHERE country LIKE 'United States%';

UPDATE layoff_staging2
SET country = TRIM(TRAILING '.' FROM country)
WHERE country LIKE 'United States%';

SELECT `date`,
STR_TO_DATE(`date`, '%m/%d/%Y')
FROM layoff_staging2;

UPDATE layoff_staging2
SET `date` = STR_TO_DATE(`date`, '%m/%d/%Y');

SELECT *
FROM layoff_staging2;

ALTER TABLE layoff_staging2
MODIFY COLUMN `date` DATE;

-- 3. Null Values or Blank Values


SELECT *
FROM layoff_staging2
WHERE industry IS NULL
OR industry = '';

SELECT *
FROM layoff_staging2
WHERE company = 'Airbnb';

SELECT *
FROM layoff_staging2;

UPDATE layoff_staging2
SET industry = NULL
WHERE industry = '';

SELECT t1.industry, t2.industry
FROM layoff_staging2 t1
JOIN layoff_staging2 t2
	ON t1.company = t2.company
WHERE t1.industry IS NULL
AND t2.industry IS NOT NULL;


UPDATE layoff_staging2 t1
JOIN layoff_staging2 t2
	ON t1.company = t2.company
SET t1.industry = t2.industry
WHERE (t1.industry IS NULL OR t1.industry = '')
AND t2.industry IS NOT NULL;


SELECT *
FROM layoff_staging2
WHERE total_laid_off IS NULL
AND percentage_laid_off IS NULL;

DELETE
FROM layoff_staging2
WHERE total_laid_off IS NULL
AND percentage_laid_off IS NULL;

ALTER TABLE layoff_staging2
DROP COLUMN row_num;

SELECT *
FROM layoff_staging2;

-- Exploratory Data Analysis

SELECT *
FROM layoff_staging2;

SELECT MAX(total_laid_off), MAX(percentage_laid_off)
FROM layoff_staging2;

SELECT *
FROM layoff_staging2
WHERE percentage_laid_off = 1
ORDER BY funds_raised_millions DESC;

SELECT company, SUM(total_laid_off)
FROM layoff_staging2
GROUP BY company
ORDER BY 2 DESC;

SELECT MIN(`date`), MAX(`date`)
FROM layoff_staging2;

SELECT industry, SUM(total_laid_off)
FROM layoff_staging2
GROUP BY industry
ORDER BY 2 DESC;

SELECT country, SUM(total_laid_off)
FROM layoff_staging2
GROUP BY country
ORDER BY 2 DESC;

SELECT YEAR(`date`), SUM(total_laid_off)
FROM layoff_staging2
GROUP BY YEAR(`date`)
ORDER BY 1 DESC;

SELECT stage, SUM(total_laid_off)
FROM layoff_staging2
GROUP BY stage
ORDER BY 1 DESC;

SELECT SUBSTRING(`date`,6,2) AS `month`, SUM(total_laid_off)
FROM layoff_staging2
WHERE SUBSTRING(`date`,6,2) IS NOT NULL
GROUP BY `month`
ORDER BY 1 ASC;

WITH Rolling_Total AS
(
SELECT SUBSTRING(`date`,1,7) AS `month`, SUM(total_laid_off) AS total_off
FROM layoff_staging2
WHERE SUBSTRING(`date`,1,7) IS NOT NULL
GROUP BY `month`
ORDER BY 1 ASC
)
SELECT `month`, total_off,
SUM(total_off) OVER(ORDER BY `month`) AS rolling_total
FROM Rolling_Total;


SELECT company, SUM(total_laid_off)
FROM layoff_staging2
GROUP BY company
ORDER BY 2 DESC;

SELECT company, YEAR(`date`),
SUM(total_laid_off)
FROM layoff_staging2
GROUP BY company, YEAR(`date`)
ORDER BY 3 desc;

WITH Company_Year(company, years, total_laid_off) AS
(
SELECT company, YEAR(`date`),
SUM(total_laid_off)
FROM layoff_staging2
GROUP BY company, YEAR(`date`)
), Company_years_rank AS
(
SELECT *, DENSE_RANK() OVER(PARTITION BY years ORDER BY total_laid_off DESC) AS ranking
FROM Company_Year
WHERE years IS NOT NULL
)
SELECT *
FROM Company_years_rank
WHERE ranking <= 5;









