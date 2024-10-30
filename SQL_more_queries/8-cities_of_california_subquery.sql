-- Task 8:
-- Select cities in California from the cities table based on the state_id of California from the states table
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
