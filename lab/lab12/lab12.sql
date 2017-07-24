.read data.sql

-- Q2
CREATE TABLE obedience as
  SELECT seven, denero FROM students;


-- Q3
CREATE TABLE blue_dog as
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";


-- Q4
CREATE TABLE smallest_int as
  SELECT time, smallest FROM students WHERE smallest > 6 ORDER BY smallest LIMIT 20;


-- Q5
CREATE TABLE sevens as
  SELECT s.seven FROM students as s, checkboxes as c WHERE s.time = c.time AND s.number = 7 AND c."7" = "True";


-- Q6
CREATE TABLE matchmaker as
  SELECT a.pet, a.song, a.color, b.color From students as a, students as b WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time;


