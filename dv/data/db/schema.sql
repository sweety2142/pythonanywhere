DROP TABLE IF EXISTS user_list;

CREATE TABLE user_list (
	num INTEGER PRIMARY KEY AUTOINCREMENT,
	name varchar(50) not null,
	mail varchar(50) not null,
	password varchar(50) not null,
	creation_date TIMESTAMP,
  cookie_id varchar(100)
);

