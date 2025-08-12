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
    (id, name, email, gender, date_of_birth, salary)
VALUES
    (1, 'Clark', 'clark@mail.com', 'Male', '2000-10-10', 50000);

INSERT INTO [USER]
    (id, name, email, gender, date_of_birth, salary)
VALUES
    (2, 'Dave', 'dave@mail.com', 'Male', '2020-11-16', 60000);

INSERT INTO [USER]
    (id, name, email, gender, date_of_birth, salary)
VALUES
    (3, 'Ava', 'ava@mail.com', 'Female', '2022-07-12', 70000);

-- Add a new column
ALTER TABLE [USER] ADD department VARCHAR(50);

-- Drop a column
-- ALTER TABLE [USER] DROP COLUMN gender;

-- find users between (adjusted dates to match your data)
SELECT *
FROM [USER]
WHERE date_of_birth BETWEEN '2000-01-01' AND '2022-12-31';

-- First create the address table for the JOIN to work
CREATE TABLE [USER_ADDRESS]
(
    address_id INT PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES [USER](id),
    city VARCHAR(50),
    country VARCHAR(50)
);

-- Insert some sample address data
INSERT INTO [USER_ADDRESS]
VALUES
    (1, 1, 'New York', 'USA');
INSERT INTO [USER_ADDRESS]
VALUES
    (2, 2, 'London', 'UK');

-- LEFT JOIN (now this will work)
SELECT u.id, u.name, a.city, a.country
FROM [USER] u
    LEFT JOIN [USER_ADDRESS] a ON u.id = a.user_id;