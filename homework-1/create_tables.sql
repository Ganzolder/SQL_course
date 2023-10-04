-- SQL-команды для создания таблиц
CREATE TABLE employee
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(200) NOT NULL,
	birth_date date NOT NULL,
	notes text
);


CREATE TABLE customer
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);


CREATE TABLE customer_order
(
	order_id int PRIMARY KEY,
	customer_id varchar(100) REFERENCES customer(customer_id) NOT NULL,
	employee_id int REFERENCES employee(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(100) NOT NULL
);
