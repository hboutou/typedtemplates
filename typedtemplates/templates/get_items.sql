SELECT 
    col1,
    col2,
    SUM(c) AS col3
FROM
    {schema}.mytable
WHERE
    col1 IN ({ids})
    AND name IN ({names})
GROUP BY
    col1, col2
;

