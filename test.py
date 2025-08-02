SELECT *
FROM your_table
WHERE NOT REGEXP_LIKE(your_column, '^\s*[-+]?[0-9]*\.?[0-9]+$');
