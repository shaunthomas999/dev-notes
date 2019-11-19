# Oracle SQL sample commands

```sql
-- Create --

CREATE TABLE Student(ID NUMBER(*,0), 
  FIRSTNAME NVARCHAR2(50),
  LASTNAME NVARCHAR2(50),
  ADDRESS NVARCHAR2(500),
  AGE NUMBER(3),
  SALARY NUMBER(6,4)
  GENDER NCHAR(1)
);
```

```sql
-- Insert --

INSERT INTO Student(ID, FIRSTNAME, LASTNAME, ADDRESS, AGE, GENDER) VALUES(1, 'Mahindra Singh', 'Dhoni', 'Jharkand', 33, 'M');
INSERT INTO Student(ID, FIRSTNAME, LASTNAME, ADDRESS, AGE, GENDER) VALUES(2, 'Sachin', 'Tendulkar', 'Mumbai', 36, 'M');
INSERT INTO Student(ID, FIRSTNAME, LASTNAME, ADDRESS, AGE, GENDER) VALUES(3, 'Juila', 'Roberts', 'California', 40, 'F');
```

```sql
-- Alter Table/Column --

ALTER TABLE MY_SCHEMA.STUDENT
  ADD (INSURANCE NVARCHAR2(2),
       CLUB_PASS NUMBER(5,0));
```

```sql
-- Constraint --

ALTER TABLE MY_SCHEMA.STUDENT
  ADD CONSTRAINT CLUB_PASS_CONSTRAINT
    CHECK (CLUB_PASS IN ('AA', 'BB'));
```
