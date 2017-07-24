.read data.sql

-- Q1
CREATE TABLE flight_costs as
    with day_prices(day, price, yesterday_price) as (
    select 3, 40, 30 union
    select day + 1, (price + yesterday_price) / 2 + ((day + 1) % 7 * 5), price
    from day_prices
    where day < 25
    )
  select 1 as Day, 20 as Price union
  select 2, 30 union
  select day, price
  from day_prices;

-- Q2
CREATE TABLE schedule as
  select "SFO, PDX" as path, price from flights where departure = "SFO" and arrival = "PDX" union
  select "SFO, " || a.arrival || ", PDX" as path, a.price + b.price as price
  from flights as a, flights as b
  where a.departure = "SFO" and b.arrival = "PDX" and a.arrival = b.departure
  order by price;


-- Q3 -------------------------------------------------
CREATE TABLE shopping_cart as
  with cart(list, last, budget) as (
    SELECT item, price, 60 - price FROM supermarket WHERE price <= 60 UNION
    SELECT list || ", " || item, price, budget - price FROM cart, supermarket
      WHERE price <= budget AND price >= last
  )
  SELECT list, budget FROM cart ORDER BY budget, list;


-- Q4
CREATE TABLE number_of_options as
  SELECT count(distinct meat)
  from main_course;


-- Q5
CREATE TABLE calories as
  SELECT count(meat)
  from main_course, pies
  where main_course.calories + pies.calories < 2500;


-- Q6
CREATE TABLE healthiest_meats as
  with meat_full(meat, fullcal) as (
  SELECT meat, main_course.calories + pies.calories as full
  from main_course, pies
  )
  select meat, min(fullcal)
  from meat_full
  group by meat
  having max(fullcal) < 3000;




-- Q7
CREATE TABLE average_prices as
  SELECT category, avg(MSRP)
  from products
  group by category;



-- Q8
CREATE TABLE lowest_prices as
  SELECT item, store, min(price)
  from inventory
  group by item;


-- Q9
CREATE TABLE shopping_list as
  with price_item(category, name) as (
  select category, name
  from products
  group by category
  having min(MSRP / rating)
  )
  select name, store
  from price_item, lowest_prices
  where name = item;


-- Q10
CREATE TABLE total_bandwidth as
  SELECT sum(MIBs)
  from shopping_list, stores
  where shopping_list.store = stores.store;

