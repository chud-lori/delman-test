create type gender_e as enum('female', 'male');
create type status_e as enum('IN_QUEUE', 'DONE', 'CANCELLED');
create table employees(id serial primary key, name varchar(255), username varchar(255), password varchar(255), gender gender_e, birthdate date);

create table doctors(id serial primary key, name varchar(255), username varchar(255), password varchar(255), gender gender_e, birthdate date, work_start_time time, work_end_time time);

create table patients(id serial primary key, name varchar(255), gender gender_e, birthdate date, no_ktp varchar(255), address varchar(255), vaccine_type varchar(255) default null, vaccine_count int default 0);

create table appointments(id serial primary key, doctor_id integer not null, patient_id integer not null, datetime timestamp, status status_e, diagnose text default null, notes text default null);

insert into employees(name, username, password, gender, birthdate) values('lori aku', 'lori', 'llll', 'female', '1997-03-03');
insert into doctors(name, username, password, gender, birthdate, work_start_time, work_end_time) values('lia cantik', 'lia', 'pasws', 'male', '1980-09-03', '07:00:00', '19:00:00');
insert into patients(name, gender, birthdate, no_ktp, address, vaccine_type, vaccine_count) values('pitik', 'male', '1940-11-21', '930182302180312', 'kandang', 'sinovac', 1);
insert into appointments(doctor_id, patient_id, datetime, status) values(1, 1, '2021-11-12 08:00:00', 'IN_QUEUE');