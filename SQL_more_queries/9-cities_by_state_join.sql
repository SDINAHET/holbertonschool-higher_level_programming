-- Task 9:
-- Select cities with their states from the cities and states tables using a JOIN on state_id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
