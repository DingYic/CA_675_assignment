/*QUERY 1: Alter the table and add a new column named LABEL to the EMAIL_DATA table*/
ALTER TABLE EMAIL_DATA ADD COLUMNS (LABEL INT);

/*Set all the entries in the database to 0 as ham entries*/
UPDATE EMAIL_DATA SET LABEL = 0;

/*QUERY 2: The below query is used to identify SPAM records and insert into SPAM database*/
UPDATE EMAIL_DATA SET LABEL = 1
WHERE LOWER(BODY) RLIKE 'call now' OR LOWER(BODY) RLIKE 'click here'
OR LOWER(BODY) RLIKE 'click' OR LOWER(BODY) RLIKE 'cash' OR LOWER(BODY) RLIKE 'bonus'
OR LOWER(BODY) RLIKE 'credit card' OR LOWER(BODY) RLIKE 'free trial' 
OR LOWER(BODY) RLIKE 'no fees' OR LOWER(BODY) RLIKE 'money back'
OR LOWER(BODY) RLIKE 'urgent' OR LOWER(BODY) RLIKE 'lottery' OR LOWER(BODY) RLIKE 'winner'
OR LOWER(BODY) RLIKE 'collect reward' OR LOWER(BODY) RLIKE 'card accepted'
OR LOWER(BODY) RLIKE 'no hidden cost' OR LOWER(BODY) RLIKE 'winner'
OR LOWER(BODY) RLIKE 'lose weight' OR LOWER(BODY) RLIKE 'apply now'
OR LOWER(BODY) RLIKE 'act now' OR LOWER(BODY) RLIKE 'action required'
OR LOWER(BODY) RLIKE 'card accepted' OR LOWER(BODY) RLIKE 'no extra cost'
OR LOWER(BODY) RLIKE 'congratulations' OR LOWER(BODY) RLIKE 'no refunds'
OR LOWER(BODY) RLIKE 'reward' OR LOWER(BODY) RLIKE 'cash prize'
OR LOWER(BODY) RLIKE 'million';

/*QUERY 3: The below query is used to insert all spam records in the email_spam database*/
INSERT OVERWRITE TABLE EMAIL_SPAM SELECT FROM_EMAIL, TO_EMAIL, SUBJECT, BODY FROM EMAIL_DATA WHERE LABEL = 1;

/*QUERY 4: The below query is used to insert all ham records in the email_ham database*/
INSERT OVERWRITE TABLE EMAIL_HAM SELECT FROM_EMAIL, TO_EMAIL, SUBJECT, BODY FROM EMAIL_DATA WHERE LABEL = 0;