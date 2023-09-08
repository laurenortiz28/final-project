Create Table employee_information (

        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone_number VARCHAR(15),
        employee_id INT,
        cafe_id INT,
        shift_id INT,
        email VARCHAR(50),
        CONSTRAINT PK_employee_information PRIMARY KEY (employee_id)
);