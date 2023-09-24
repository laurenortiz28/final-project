CREATE TABLE shifts (
  id int NOT NULL,
  cafe_id int DEFAULT NULL,
  employee_number int NOT NULL,
  shift_id varchar(45) NOT NULL,
  workday varchar(45) NOT NULL,
  available varchar(50) NOT NULL,
  PRIMARY KEY (id)
);
