# MySQL Advanced

This repository contains SQL scripts demonstrating advanced MySQL concepts including indexes, stored procedures, triggers, views, and more. The project is part of the ALX Backend Storage curriculum.

## Project Overview

The tasks in this project explore various MySQL advanced features that help optimize database performance, enforce constraints, and abstract complex queries. Each script focuses on a specific MySQL concept and provides practical examples of its implementation.

## Technologies Used
* MySQL 5.7
* Ubuntu 18.04 LTS

## Project Structure

Each SQL script is named according to its task number and description:

### Mandatory Tasks

| Script | Description |
|--------|-------------|
| `0-uniq_users.sql` | Creates a table with a unique email attribute |
| `1-country_users.sql` | Creates a table with an enumeration of countries |
| `2-fans.sql` | Ranks country origins of bands by the number of fans |
| `3-glam_rock.sql` | Lists all bands with Glam rock as their main style, ranked by longevity |
| `4-store.sql` | Creates a trigger to decrease item quantity after adding a new order |
| `5-valid_email.sql` | Creates a trigger that resets the valid_email attribute when the email is changed |
| `6-bonus.sql` | Creates a stored procedure AddBonus to add a new correction for a student |
| `7-average_score.sql` | Creates a stored procedure to compute and store the average score for a student |
| `8-index_my_names.sql` | Creates an index on the first letter of name column |
| `9-index_name_score.sql` | Creates an index on the first letter of name and score columns |
| `10-div.sql` | Creates a function SafeDiv that safely divides numbers and handles division by zero |
| `11-need_meeting.sql` | Creates a view listing students that need a meeting based on score and last meeting date |

### Advanced Tasks

| Script | Description |
|--------|-------------|
| `100-average_weighted_score.sql` | Creates a stored procedure to compute and store weighted average score for a student |
| `101-average_weighted_score.sql` | Creates a stored procedure to compute and store weighted average score for all students |

## Usage Instructions

### Setting up the MySQL Server

1. Start the MySQL service:
```bash
$ service mysql start
```

2. Connect to the MySQL server:
```bash
$ mysql -uroot -p
```

3. Create a database (replace 'database_name' with your preferred name):
```sql
mysql> CREATE DATABASE database_name;
```

### Running the Scripts

To execute a script:

```bash
$ cat [script_name].sql | mysql -uroot -p [database_name]
```

Example:
```bash
$ cat 0-uniq_users.sql | mysql -uroot -p holberton
```

### Working with Sample Data

Some tasks require sample data. You can import a SQL dump as follows:

```bash
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p database_name
```

## Key Concepts Covered

* Table creation with constraints (UNIQUE, ENUM)
* Advanced SQL queries with aggregation
* TRIGGER creation for data integrity
* STORED PROCEDURE implementation
* INDEX creation for query optimization
* VIEW creation for query abstraction
* FUNCTION creation for reusable logic

## Author

[Your Name] - ALX Software Engineering Program

## Acknowledgements

This project is part of the curriculum of the ALX Software Engineering Program, which provides practical and project-based learning for backend development and system engineering.
