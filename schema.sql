# Database Schema

drop table if exists users;
create table users(
	id integer primary key autoincrement,
    	latitude float not null,
    	longitude float not null
);
