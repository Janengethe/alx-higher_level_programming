-- lists all cities of carifornia in hbtn_0d_usa
-- sorted results in desc
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') GROUP BY id ORDER BY id ASC;
