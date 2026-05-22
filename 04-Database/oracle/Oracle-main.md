# Oracle - Main

## Blocking - Transaction - Query - find

* Blocked sessions (currently waiting)

```sql
SELECT
    s.sid,
    s.serial#,
    s.username,
    s.status,
    s.event,
    s.seconds_in_wait,
    s.blocking_session,
    s.sql_id
FROM v$session s
WHERE s.blocking_session IS NOT NULL;
```

* Sessions that are blocking others

```sql
SELECT
    s.sid,
    s.serial#,
    s.username,
    s.status,
    s.sql_id
FROM v$session s
WHERE s.sid IN (
    SELECT DISTINCT blocking_session
    FROM v$session
    WHERE blocking_session IS NOT NULL
);
```

* Find the SQL Causing the Block
```sql
SELECT
    sql_id,
    sql_text
FROM v$sql
WHERE sql_id = '<SQL_ID_FROM_V$SESSION>';
```

* Kill a Hanging Session (Only If Necessary)

```sql
ALTER SYSTEM KILL SESSION '<sid>,<serial#>' IMMEDIATE;

<!-- Verify -->
SELECT status FROM v$session WHERE sid = <sid>;
```