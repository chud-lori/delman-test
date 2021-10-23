create type gender_e as enum('female', 'male');
create table employees(id serial primary key, name varchar(255), username varchar(255), password varchar(255), gender gender_e, birthdate date);

insert into employees(name, username, password, gender, birthdate) values('lori aku', 'lori', 'llll', 'female', '1997-03-03');