CREATE TABLE schedules (
  id int NOT NULL,
  employee_id int NOT NULL,
  Cafe_id int NOT NULL,
  shift_id varchar(25) NOT NULL,
  hours_worked int NOT NULL,
  shift_availability varchar(45) NOT NULL,
  PRIMARY KEY (id),
  KEY employee_id_idx (employee_id),
  CONSTRAINT employee_id FOREIGN KEY (employee_id) REFERENCES employee_information (employee_id)
);
