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
	 (3, "Italia"),
	 (4, "Espanja"),
	 (5, "Saksa"),
	 (6, "Kreikka"),
	 (7, "Suomi"),
	 (8, "Ruotsi"),
	 (9, "Romania"),
	 (10, "Puola"),
	 (11, "Bulgaria"),
	 (12, "Slovenia"),
	 (13, "Slovakia"),
	 (14, "Itävalta"),
	 (15, "Norja"),
	 (16, "Viro"),
	 (17, "Latvia"),
	 (18, "Islanti"),
	 (19, "Irlanti"),
	 (20, "Portugali"),
	 (21, "Alankomaat"),
	 (22, "Ukraina"),
	 (23, "Montenegro"),
	 (24, "Kypros"),
	 (25, "Malta"),
	 (26, "Sveitsi"),
	 (27, "Tsekki"),
	 (28, "Belgia"),
	 (29, "Serbia"),
	 (30, "Moldova");
	 
	 