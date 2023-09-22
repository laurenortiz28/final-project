CREATE TABLE shifts (
  id int NOT NULL,
  cafe_id int DEFAULT NULL,
  employee_number int NOT NULL,
  shift_id varchar(45) NOT NULL,
  workday varchar(45) NOT NULL,
  start_time time NOT NULL,
  end_time time NOT NULL,
  available int NOT NULL,
  PRIMARY KEY (id)
);
