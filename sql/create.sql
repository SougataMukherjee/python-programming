--create db
CREATE DATABASE myDb;
USE myDb;
-- create table
CREATE TABLE EMPLOYEE (
  empId int NOT NULL PRIMARY KEY,
  name varchar(50),
  email varchar(50) UNIQUE NOT NULL,
  dept varchar(55)
);

-- insert
INSERT INTO EMPLOYEE(empId, name, email, dept) 
VALUES (1, 'Clark', 'clark@mail.com', 'Sales');

INSERT INTO EMPLOYEE(empId, name, email, dept) 
VALUES (2, 'Dave', 'dave@mail.com', 'Accounting');

INSERT INTO EMPLOYEE(empId, name, email, dept) 
VALUES (3, 'Ava', 'ava@mail.com', 'Sales');


-- -- fetch 
SELECT * FROM EMPLOYEE;

SELECT * FROM EMPLOYEE WHERE name='Dave' OR empId=2;

--column selection
SELECT name, email FROM EMPLOYEE;

--distinct values
SELECT DISTINCT name FROM EMPLOYEE;

--sorting
SELECT * FROM EMPLOYEE ORDER BY empId DESC;

--null check
SELECT name FROM EMPLOYEE WHERE email IS NULL;

-- IN clause
SELECT * FROM EMPLOYEE WHERE dept IN ('Sales');

-- Pattern matching
SELECT * FROM EMPLOYEE WHERE name LIKE 'A%' OR name LIKE 'D%';

--update record
UPDATE EMPLOYEE SET dept = 'Marketing' WHERE empId = 3;

-- UNION 
CREATE TABLE Customers (
  custId int NOT NULL PRIMARY KEY,
  name varchar(50),
  email varchar(50) UNIQUE NOT NULL,
  dept varchar(55)
);

INSERT INTO Customers(custId, name, email, dept) 
VALUES (101, 'jake', 'jake@mail.com', 'Sales');

INSERT INTO Customers(custId, name, email, dept) 
VALUES (201, 'mike', 'mike@mail.com', 'Accounting');

SELECT name, email FROM EMPLOYEE
UNION
SELECT name, email FROM Customers;

