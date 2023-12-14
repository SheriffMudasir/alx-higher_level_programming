-- This script lists all cities contained in the database hbtn_0d_usa.

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Select cities with state names using a JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;

