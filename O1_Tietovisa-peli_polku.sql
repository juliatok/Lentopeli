DROP DATABASE if EXISTS tietovisa;
create database tietovisa;

use tietovisa;

create table maat(
    ID      INT       	 	 not null,
    Name    VARCHAR(64)     not null,
    PRIMARY KEY (ID)
);


insert into maat (ID, Name)
    VALUES (1, "Iso-Britannia"),
	 (2, "Ranska"),
	 (3, "Saksa"),
	 (4, "Italia"),
	 (5, "Espanja"),
	 (6, "Kreikka");
	 

