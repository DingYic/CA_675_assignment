/*QUERY 1: Create an external table in UTF-8 data format which will import the data from the CSV file imported on HDFS system*/
CREATE EXTERNAL TABLE IF NOT EXISTS EMAILS(
    FROM_EMAIL STRING, 
    TO_EMAIL STRING,
    SUBJECT STRING,
    BODY STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
location '/data'
TBLPROPERTIES('serialization.encoding'='ISO-8859-1');

/*QUERY 2: Select query to validate if the records are inserted in the EMAILS external table*/
SELECT * FROM EMAILS LIMIT 10;
/*Added limit to the query so that the output screen does not print all the records and avoids cli from crashing*/

/*QUERY 3: Create an internal ORC email_data table with transctional (ACID) properties for CRUD operations*/
CREATE TABLE IF NOT EXISTS EMAIL_DATA(
    FROM_EMAIL STRING,
    TO_EMAIL STRING,
    SUBJECT STRING,
    BODY STRING
)
STORED AS ORC
TBLPROPERTIES('transactional'='true');
/*TBLPROPERTIES('transactional'='true') means we have enabled the  transactional properties for the table created*/
/*Enabling transactional properties also enables CRUD operatios using hive queries*/

/*QUERY 4: Copy data from external emails table to the internal ORC email_data table using map reduce job*/
INSERT OVERWRITE TABLE EMAIL_DATA SELECT * FROM EMAILS;
/*This query is used in to insert all the data from the external EMAILS table to the internal ORC table EMAIL_DATA*/

/*QUERY 5: Select query to validate if the records are inserted in the EMAIL_DATA external table*/
SELECT * FROM EMAIL_DATA LIMIT 10;
/*Added limit similar to QUERY 2*/

/*QUERY 6: Creates a table to store all the spam emails present in the EMAIL_DATA database*/
CREATE TABLE IF NOT EXISTS EMAIL_SPAM(
    FROM_EMAIL STRING,
    TO_EMAIL STRING,
    SUBJECT STRING,
    BODY STRING
)
STORED AS ORC
TBLPROPERTIES('transactional'='true');
/*Transactional properties will be enabled for all the databases inorder to perform CRUD operations (if required)*/

/*QUERY 7: Creates a table to store all the non spam emails i.e. ham emails*/
CREATE TABLE IF NOT EXISTS EMAIL_HAM(
    FROM_EMAIL STRING,
    TO_EMAIL STRING,
    SUBJECT STRING,
    BODY STRING
)
STORED AS ORC
TBLPROPERTIES('transactional'='true');