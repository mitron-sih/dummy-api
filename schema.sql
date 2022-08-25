DROP TABLE IF EXISTS volunteers;

CREATE TABLE volunteers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aadhar_number TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    traffic_violation BOOL NOT NULL,
    major_crime BOOL NOT NULL
);