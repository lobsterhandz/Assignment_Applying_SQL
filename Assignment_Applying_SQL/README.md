# Gym Database Management with Python and SQL

This repository contains Python scripts for managing a gym's database. The tasks include adding, retrieving, updating, and deleting records in the 'Members' and 'WorkoutSessions' tables, ensuring data integrity and efficient data handling.

## Table Structures

### Members Table

The `Members` table holds the information about the gym members.

```sql
CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);
CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);
