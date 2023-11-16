/*QUERY 1: Cleaning data; Replaced all the special characters from subject with spaces*/
UPDATE email_data SET subject = REGEXP_REPLACE(subject, '[^0-9A-Za-z ]+', ' ');

/*QUERY 2: Cleaning data; Replace all the special characters from body with spaces*/
UPDATE email_data SET body = REGEXP_REPLACE(body, '[^0-9A-Za-z ]+', ' ');