## 0x0D. SQL - Introduction
> Structures Query Language.
> It helps in executing commands that let you create, manipulate and control a relational database.
> SQL is a declarative language that focuses on the "what" results you desire, but not how to get them. It is non-procedural.
> Main components of SQL Syntax:
* Data Definition Language (DDL)
* Data Manipulation Language (DML)
* Data Control Language (DCL)
* Transaction Control Language (TCL)


### Resources
* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
* [Basic SQL statements: DDL and DML (no need to read the )](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
* [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
*[SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
* [MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/creating-tables.html)

### Requirements
* Files executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
* All SQL queries should a comment just before
* Files start by a comment describing the task
* All SQL keywords are in uppercase 

#### Comments Example:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 5.7 on Ubuntu 14.04 LTS
```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```

#### Connecting to Server
```
$ mysql -hlocalhost -uroot -p
Password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 5.7.8-rc MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
mysql> quit
Bye
$
```
If you have some issues to upgrade to 5.7, t hesitate to cleanup your server of any MySQL packages: `sudo apt-get remove --purge mysql-server mysql-client mysql-commond` 

#### Use "container-on-demand" to run MYSQL 
```
$ service mysql start
 * MySQL Community Server 5.7.8-rc is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
```
 
### Files Descriptions
* `0-list_databases.sql` - a script that lists all databases of your MySQL server.
* `1-create_database_if_missing.sql` - a script that creates the database hbtn_0c_0 in your MySQL server.
* `2-remove_database.sql` - a script that deletes the database hbtn_0c_0 in your MySQL server.
* `3-list_tables.sql` - a script that lists all the tables of a database in your MySQL server.
* `4-first_table.sql` - a script that creates a table called first_table in the current database in your MySQL server.
* `5-full_table.sql` - a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server
* `6-list_values.sql` - a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.