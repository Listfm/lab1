CREATE TABLE Computers (
    	index INT,
  	computer_id SERIAL PRIMARY KEY,
  	computer_name VARCHAR(255) NOT NULL,
  	gpu VARCHAR(255) NOT NULL,
  	operation_system VARCHAR(255) NOT NULL,
  	price VARCHAR(255) NOT NULL,
  	cpu VARCHAR(255) NOT NULL,
  	ram VARCHAR(255) NOT NULL,
	proof INT,
    	previous_hash VARCHAR(255)
);	