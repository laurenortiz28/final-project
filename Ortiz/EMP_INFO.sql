Create Table employeedata (
        
        employee_id INT,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone_number VARCHAR(15),
        cafe_id INT,
        shift_id VARCHAR(30),
        email VARCHAR(50),
        job_pos VARCHAR(30),
        length_work INT,
        CONSTRAINT PK_employee_information PRIMARY KEY (employee_id)
);
