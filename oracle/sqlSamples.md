# Oracle SQL sample commands

```sql
-- Create --
CREATE TABLE Student(ID NUMBER(*,0), 
  FIRSTNAME NVARCHAR2(50),
  LASTNAME NVARCHAR2(50),
  ADDRESS NVARCHAR2(500),
  AGE NUMBER(2,0),
  GENDER NCHAR(1)
);

-- Insert --
INSERT INTO Student(ID, FIRSTNAME, LASTNAME, ADDRESS, AGE, GENDER) VALUES(1, 'Mahindra Singh', 'Dhoni', 'Jharkand', 33, 'M');
INSERT INTO Student(ID, FIRSTNAME, LASTNAME, ADDRESS, AGE, GENDER) VALUES(2, 'Sachin', 'Tendulkar', 'Mumbai', 36, 'M');
INSERT INTO Student(ID, FIRSTNAME, LASTNAME, ADDRESS, AGE, GENDER) VALUES(3, 'Juila', 'Roberts', 'California', 40, 'F');
```
