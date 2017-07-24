create table pizzas as
  select "Pizzahhh" as name, 12 as open, 15 as close union
  select "La Val's"        , 11        , 22          union
  select "Sliver"          , 11        , 20          union
  select "Cheeseboard"     , 16        , 23          union
  select "Emilia's"        , 13        , 18;

create table meals as
  select "breakfast" as meal, 11 as time union
  select "lunch"            , 13         union
  select "dinner"           , 19         union
  select "snack"            , 22;

-- Two meals at the same place
create table double as
with more_than_six(first, first_time, second, second_time) as (
    select a.meal, a.time, b.meal, b.time
    from meals as a, meals as b
    where b.time - a.time > 6
)
select first, second, name
from more_than_six, pizzas
where first_time >= open and second_time <= close;


-- Pizza options for every meal
create table options as
with all_pizza(meal, stores) as (
    select meal, name from meals, pizzas where time >= open and time <= close
)
select *
from all_pizza;


