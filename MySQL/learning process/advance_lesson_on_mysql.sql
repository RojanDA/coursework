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


