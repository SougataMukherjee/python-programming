-- Create table
CREATE TABLE College (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(100),
    content TEXT,
    status VARCHAR(20) CHECK (status IN ('active', 'inactive')),
    is_active BOOLEAN,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Add email column
ALTER TABLE College ADD COLUMN email VARCHAR(64);

-- Insert sample data (corrected)
INSERT INTO College (name, content, status, is_active) VALUES
('Sam', 'First student record', 'active', TRUE),
('Rupai', 'Second student record', 'inactive', FALSE);

-- QUERY database
SELECT * FROM College;

-- Count distinct names from the table
SELECT COUNT(DISTINCT name) FROM College;

-- Regex match (case-insensitive)
SELECT * FROM College WHERE name ~* '^[a-z][a-z]+$';

-- Concatenate name + content
SELECT CONCAT(name, ' ', content) AS cont
FROM College;

-- Lowercase comparison
SELECT * FROM College WHERE LOWER(name) = 'sam';

-- Format date
SELECT TO_CHAR(created_at, 'YYYY-MM-DD') FROM College;

-- Partial index
CREATE INDEX idx_active ON College(email) WHERE is_active = TRUE;

-- Distinct values
SELECT DISTINCT name
FROM College;
