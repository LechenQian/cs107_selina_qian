#!/usr/bin/env bash
# File       : joins.sh
# Author     : Fabian Wermelinger
# Description: Examples for table joins of lecture 22
# Copyright 2021 Harvard University. All Rights Reserved.

cat <<EOF | sqlite3
.header on
.mode column
.nullvalue NULL

CREATE TABLE A (
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Name TEXT NOT NULL,
Office TEXT NOT NULL,
Salary REAL
);
INSERT INTO A (Name, Office, Salary) VALUES ('Frank', 'A12', 45000.0);
INSERT INTO A (Name, Office, Salary) VALUES ('Roberta', 'A10', 80000.0);
INSERT INTO A (Name, Office, Salary) VALUES ('Lory', 'B07', 50000.0);

CREATE TABLE B (
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Bonus REAL,
EID INTEGER NOT NULL,
FOREIGN KEY (EID) REFERENCES A(ID)
);
INSERT INTO B (Bonus, EID) VALUES (8000.0, 1);
INSERT INTO B (Bonus, EID) VALUES (10000.0, 3);
INSERT INTO B (Bonus, EID) VALUES (1000000.0, 10);

SELECT * FROM A INNER JOIN B ON B.EID = A.ID;
.print ''
SELECT * FROM A LEFT OUTER JOIN B ON B.EID = A.ID;
.print ''
SELECT * FROM B LEFT OUTER JOIN A ON B.EID = A.ID;
.print ''
-- FOLLOW UP TO IN-CLASS QUESTION: How to address columns with identical name?
-- alias two columns with identical names to distinct names in joined table
SELECT A.ID AS AID, B.ID AS BID FROM B LEFT OUTER JOIN A ON B.EID = A.ID;
.print ''
-- as opposed to this less useful variant
SELECT A.ID, B.ID FROM B LEFT OUTER JOIN A ON B.EID = A.ID;
EOF
