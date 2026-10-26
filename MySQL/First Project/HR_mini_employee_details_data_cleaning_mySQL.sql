-- DATA CLEANING AND EXPOLARATION USING CSV FILE 

SELECT * FROM employee_demographics_raw ;
SELECT * FROM employee_salary_raw;

-- dublicating the raw table demigraphics because using raw data is not good way to practice, and we need the raw data if we do some mistake
CREATE TABLE employee_demographics
LIKE employee_demographics_raw;


-- dublicating the raw table salary
CREATE TABLE employee_salary
LIKE employee_salary_raw;


-- inserting the value from raw data
INSERT employee_demographics
SELECT * 
FROM employee_demographics_raw;

INSERT employee_salary
SELECT * 
FROM employee_salary_raw;

-- checking data,inserted in the new table 
SELECT * FROM employee_demographics;
SELECT * FROM employee_salary;

SELECT *,
ROW_NUMBER() OVER(PARTITION BY first_name, last_name, gender, birth_date, age, country) AS row_num
FROM employee_demographics;

UPDATE employee_demographics
SET first_name = TRIM(first_name),
last_name = TRIM(last_name),
country = TRIM(country),
gender = LOWER(TRIM(gender));

UPDATE employee_demographics
SET country = 
	CASE 
		WHEN UPPER(country) IN ('USA', 'U.S.A.','US','UNITED STATES') THEN 'United States'
        WHEN UPPER(country) IN ('NEPAL') THEN 'Nepal'
        ELSE country
	END;


UPDATE employee_demographics
SET gender = 
	CASE 
		WHEN LOWER(TRIM(gender)) IN ('f', 'female') THEN 'Female'
        WHEN LOWER(TRIM(gender)) IN ('m','male') THEN 'Male'
        ELSE NULL
	END;

UPDATE employee_demographics AS ed
JOIN employee_demographics_raw AS edr
USING(employee_id)
SET ed.gender = edr.gender;

SELECT * FROM employee_demographics;
SELECT * FROM employee_salary;

ALTER TABLE employee_demographics
ADD COLUMN birth_date_parsed DATE NULL;

UPDATE employee_demographics
SET birth_date_parsed = COALESCE(
STR_TO_DATE(birth_date, '%Y-%m-%d'),
STR_TO_DATE(birth_date, '%m/%d/%Y'),
STR_TO_DATE(birth_date, '%d-%m-%Y'),
STR_TO_DATE(birth_date, '%Y/%m/%d')
);

SELECT birth_date,
  CASE
    WHEN birth_date REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
      THEN STR_TO_DATE(birth_date, '%Y-%m-%d')
    WHEN birth_date REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$'
      THEN STR_TO_DATE(birth_date, '%m/%d/%Y')
    WHEN birth_date REGEXP '^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$'
      THEN STR_TO_DATE(birth_date, '%d-%m-%Y')
    WHEN birth_date REGEXP '^[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}$'
      THEN STR_TO_DATE(birth_date, '%Y/%m/%d')
    ELSE NULL
  END AS parsed_date
FROM employee_demographics
LIMIT 30;

UPDATE employee_demographics
SET birth_date_parsed =
  CASE
    WHEN birth_date REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
      THEN STR_TO_DATE(birth_date, '%Y-%m-%d')
    WHEN birth_date REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$'
      THEN STR_TO_DATE(birth_date, '%m/%d/%Y')
    WHEN birth_date REGEXP '^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$'
      THEN STR_TO_DATE(birth_date, '%d-%m-%Y')
    WHEN birth_date REGEXP '^[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}$'
      THEN STR_TO_DATE(birth_date, '%Y/%m/%d')
    ELSE NULL
  END;
  
  ALTER TABLE employee_demographics
  DROP COLUMN birth_date;

SELECT * FROM employee_demographics;

 ALTER TABLE employee_demographics
 CHANGE birth_date_parsed birth_date DATE;
SELECT * FROM employee_salary;


UPDATE employee_demographics
SET age = NULL
WHERE age IS NOT NULL AND TRIM(age) = '';

UPDATE employee_demographics
SET age = TIMESTAMPDIFF(YEAR, birth_date, CURDATE())
WHERE birth_date IS NOT NULL;


SELECT * FROM employee_salary;

update employee_salary
SET dept_id = TRIM(dept_id),
salary = TRIM(salary);

SELECT pay_date,
  CASE
    WHEN pay_date REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
      THEN STR_TO_DATE(pay_date, '%Y-%m-%d')
    WHEN pay_date REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$'
      THEN STR_TO_DATE(pay_date, '%m/%d/%Y')
    WHEN pay_date REGEXP '^[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}$'
      THEN STR_TO_DATE(pay_date, '%Y/%m/%d')
    ELSE NULL
  END AS parsed_date
FROM employee_salary
LIMIT 30;



UPDATE employee_salary
SET pay_date =
  CASE
    WHEN pay_date REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
      THEN STR_TO_DATE(pay_date, '%Y-%m-%d')
    WHEN pay_date REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$'
      THEN STR_TO_DATE(pay_date, '%m/%d/%Y')
    WHEN pay_date REGEXP '^[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}$'
      THEN STR_TO_DATE(pay_date, '%Y/%m/%d')
    ELSE NULL
  END;

ALTER TABLE employee_salary
MODIFY COLUMN `pay_date` DATE;

SELECT * FROM employee_salary;

ALTER TABLE employee_salary
MODIFY COLUMN salary DECIMAL(10,2);

SELECT COUNT(*) FROM employee_salary WHERE dept_id = '';
SELECT COUNT(*) FROM employee_salary WHERE dept_id IS NULL;

UPDATE employee_salary
SET dept_id = NULL
WHERE TRIM(dept_id) = '';

SELECT *
FROM employee_demographics ed
INNER JOIN employee_salary es ON ed.employee_id = es.employee_id;



