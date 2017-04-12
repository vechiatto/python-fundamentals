create table users (
	id serial primary key,
	usuario varchar (255),
	pass varchar(255)
);

insert into users (usuario, pass) values('joao', '123456');