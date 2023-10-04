CREATE TABLE shifts (
  id int NOT NULL,
  cafe_id int DEFAULT NULL,
  employee_id int NOT NULL,
  shift_id varchar(45) NOT NULL,
  workday varchar(45) NOT NULL,
  PRIMARY KEY (id)
  CONSTRAINT employee_id (employee_id) REFERENCES schedules (employee_id)
);
