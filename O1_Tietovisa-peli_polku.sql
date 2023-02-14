DROP DATABASE if EXISTS tietovisa;
CREATE DATABASE tietovisa;

USE tietovisa;

CREATE TABLE maat(
    ID      			INT       	 	NOT NULL,
    Nimi    			VARCHAR(64)    NOT NULL,
    vastaukset_id 	INT				,
	 lentokenttä		VARCHAR (64)	,	
    PRIMARY KEY (ID)
);

CREATE TABLE vastaukset(
	ID 			INT				NOT NULL AUTO_INCREMENT,
	paikka_id 	INT				,
	kysymys 		VARCHAR (200)	,
	oikein		VARCHAR (100)	,
	väärin1 		VARCHAR (100)	,
	väärin2 		VARCHAR (100)	,
	PRIMARY KEY	(ID),
	FOREIGN KEY (paikka_id) REFERENCES maat (ID)
);

CREATE TABLE käyttäjä(
	ID				INT 				NOT NULL auto_increment,
	Nimi			VARCHAR(60)		NOT NULL,
	paikka		INT 				,				
	PRIMARY KEY (ID)
);

INSERT INTO maat (ID, Nimi)
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
	 
	 
INSERT INTO käyttäjä (Nimi)
	VALUES ("Petra"),
	("Mia"),
	("Wilma"),
	("Julia");
	
INSERT INTO vastaukset (paikka_id, kysymys, oikein, väärin1, väärin2)
	VALUES (8,"Mikä on Ruotsin toiseksi suurin kaupunki?","Göteborg","Tukholma","Malmö"),
	(15,"Keskeisimpiä elementtejä Norjan maisemassa ovat:","Vuonot ja vuoret","Joet ja järvet","Metsät ja tunturit"),
	(15,"Norjan perustaja ja ensimmäinen kuningas oli:","Harald Kaunotukka","Pyhä Olavi","Eerik Verikirves");
	