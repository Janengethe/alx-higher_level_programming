-- creates a table id_not_null
-- default id cannot be null so default to 1

CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
