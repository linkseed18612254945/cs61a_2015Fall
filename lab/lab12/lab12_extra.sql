.read lab12.sql

-- Q7
CREATE TABLE smallest_int_count as
    SELECT smallest, count(*) FROM students GROUP BY smallest HAVING smallest > 0;

