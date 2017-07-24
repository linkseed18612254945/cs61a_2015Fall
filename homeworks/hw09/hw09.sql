create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
select name, size from dogs, sizes where height > min and height <= max;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
select child from dogs, parents where name = parent order by height desc;


-- Sentences about siblings that are the same size
create table sentences as
with
    siblings(name_a, name_b, size_a, size_b) as (
    select a.child, b.child, c.size, d.size
    from parents as a, parents as b, size_of_dogs as c, size_of_dogs as d
    where a.parent = b.parent and a.child < b.child and c.name = a.child and d.name = b.child
    )
select name_a || " and " || name_b || " are " || size_a || " siblings" as phrase
        from siblings where size_a = size_b;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
with stack_dogs(dog1, dog2, dog3, dog4, stack_height) as (
    select a.name, b.name, c.name, d.name, a.height + b.height + c.height + d.height
    from dogs as a, dogs as b, dogs as c, dogs as d where a.height < b.height and b.height < c.height and c.height < d.height
)
select dog1 || ", " || dog2 || ", " || dog3 || ", " || dog4, stack_height
from stack_dogs where stack_height > 170 order by stack_height;


create table tallest as
with height_level(dog, height, level) as (
    select name, height, height / 10
    from dogs
)
select max(height), dog
from height_level
group by level having count(*) > 1;


-- All non-parent relations ordered by height difference
--create table non_parents as
--select
--from parents as a, parents as b
--where a;


