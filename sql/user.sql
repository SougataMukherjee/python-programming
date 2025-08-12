
-- create
CREATE TABLE [USER]
(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('Male','Female','Other')),
    date_of_birth DATE,
    salary DECIMAL(10,2)
);

-- insert
INSERT INTO [USER]
    (id, name, email, gender, date_of_birth,salary)
VALUES
    (1, 'Clark', 'clark@mail.com', 'Male', '2000-10-10', 50000);

INSERT INTO [USER]
    (id, name, email, gender, date_of_birth,salary)
VALUES
    (2, 'Dave', 'dave@mail.com', 'Male', '2020-11-16', 60000);

INSERT INTO [USER]
    (id, name, email, gender, date_of_birth,salary)
VALUES
    (3, 'Ava', 'ava@mail.com', 'Female', '2022-07-12', 70000);

-- fetch 
SELECT *
FROM [USER];


SELECT *
FROM [USER]
WHERE name='Dave' OR id=2;
SELECT *
FROM [USER]
WHERE salary IN (50000,60000)

--column update
UPDATE [USER] SET salary=salary+10000 WHERE salary<=60000;
SELECT *
FROM [USER]

--count
SELECT COUNT(*)
FROM [USER]
WHERE gender='Female'

--group
SELECT gender, AVG(salary) AS avg_salary
FROM [USER]
GROUP BY gender

--average
SELECT AVG(salary)
FROM [USER];

--sub query
SELECT *
FROM [USER]
WHERE salary < (SELECT AVG(salary)
FROM [USER])

