в первом задании все поднимается командой:
docker-compose up -d

во втором задании sql запрос ниже запускал в pgadmin но перед этим создал таблицы модуль
create_tables.py и заполнил таблицы данными insert_data.py

WITH cte AS (
    SELECT
        TRIM(SUBSTRING(name, 1, POSITION('.' IN name) - 1)) AS short_name,
        name AS full_name,
        status
    FROM full_names
)
UPDATE full_names f
SET status = c.status
FROM cte c, short_names shr
WHERE c.short_name = shr.name;