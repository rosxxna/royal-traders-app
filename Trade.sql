Create database trading;

create table login(
userid varchar(20),
username varchar(20),
password varchar(20),
card_number int(100));

create table transaction(
userid varchar(20),
Amount decimal(20,2),
Type varchar(20),
Date date,
FOREIGN KEY (userid) REFERENCES login(userid));
