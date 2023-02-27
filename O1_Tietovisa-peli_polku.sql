# DROP DATABASE if EXISTS tietovisa;
USE flight_game;

DROP TABLE if EXISTS vastaukset;
DROP TABLE if EXISTS pisteet;
DROP TABLE if EXISTS maat;
DROP TABLE if EXISTS käyttäjä;


CREATE TABLE maat(
    ID      			INT       	 	NOT NULL,
    Nimi    			VARCHAR(64)    NOT NULL,
    vastaukset_id 	INT				,
	 Maakoodi			VARCHAR (2)		,	
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

CREATE TABLE pisteet( 
	ID				INT				NOT NULL AUTO_INCREMENT,
	pisteet_id	INT				,
	PRIMARY KEY (ID)				,
	FOREIGN KEY (pisteet_id) REFERENCES käyttäjä (ID)
);	

INSERT INTO maat (ID, Nimi, Maakoodi)
    VALUES (1, "Iso-Britannia","EN"),
	 (2, "Ranska","FR"),
	 (3, "Italia","IT"),
	 (4, "Espanja","ES"),
	 (5, "Saksa","DE"),
	 (6, "Kreikka","GR"),
	 (7, "Suomi","FI"),
	 (8, "Ruotsi","SE"),
	 (9, "Romania","RO"),
	 (10, "Puola","PL"),
	 (11, "Bulgaria","BG"),
	 (12, "Slovenia","SI"),
	 (13, "Slovakia","SK"),
	 (14, "Itävalta","AT"),
	 (15, "Norja","NO"),
	 (16, "Viro","ES"),
	 (17, "Latvia","LV"),
	 (18, "Islanti","IS"),
	 (19, "Irlanti","IE"),
	 (20, "Portugali","PT"),
	 (21, "Alankomaat","NL"),
	 (22, "Ukraina","UA"),
	 (23, "Montenegro","ME"),
	 (24, "Kypros","CY"),
	 (25, "Malta","MT"),
	 (26, "Sveitsi","CH"),
	 (27, "Tsekki","CZ"),
	 (28, "Belgia","BE"),
	 (29, "Serbia","RS"),
	 (30, "Moldova","MD");
	 
	 
INSERT INTO käyttäjä (Nimi)
	VALUES ("Petra"),
	("Mia"),
	("Wilma"),
	("Julia");
	
INSERT INTO vastaukset (paikka_id, kysymys, oikein, väärin1, väärin2)
	VALUES (1,"Mikä on Britannian kansalliseläin?","Leijona","Kotka","Karhu"),
	(1,"Mikä yhtye ei ole kotoisin Britanniasta?","Guns N' Roses","Queen","The Rolling Stones"),
	(2,"Mikä on Ranskan korkein vuori?","Mont Blanc","Mount Everest","Monte Bianco"),
	(2," "," "," "," "),
	(3," "," "," "," "),
	(3," "," "," "," "),
	(4," "," "," "," "),
	(4," "," "," "," "),
	(5," "," "," "," "),
	(5," "," "," "," "),
	(6," "," "," "," "),
	(6," "," "," "," "),
	(7," "," "," "," "),
	(7," "," "," "," "),
	(8,"Mikä on Ruotsin toiseksi suurin kaupunki?","Göteborg","Tukholma","Malmö"),
	(8," "," "," "," "),
	(9," "," "," "," "),
	(9," "," "," "," "),
	(10," "," "," "," "),
	(10," "," "," "," "),
	(11," "," "," "," "),
	(11," "," "," "," "),
	(12," "," "," "," "),
	(12," "," "," "," "),
	(13," "," "," "," "),
	(13," "," "," "," "),
	(14," "," "," "," "),
	(14," "," "," "," "),
	(15,"Keskeisimpiä elementtejä Norjan maisemassa ovat:","Vuonot ja vuoret","Joet ja järvet","Metsät ja tunturit"),
	(15,"Norjan perustaja ja ensimmäinen kuningas oli:","Harald Kaunotukka","Pyhä Olavi","Eerik Verikirves"),
	(16," "," "," "," "),
	(16," "," "," "," "),
	(17," "," "," "," "),
	(17," "," "," "," "),
	(18," "," "," "," "),
	(18," "," "," "," "),
	(19," "," "," "," "),
	(19," "," "," "," "),
	(20," "," "," "," "),
	(20," "," "," "," "),
	(21," "," "," "," "),
	(21," "," "," "," "),
	(22," "," "," "," "),
	(22," "," "," "," "),
	(23," "," "," "," "),
	(23," "," "," "," "),
	(24," "," "," "," "),
	(24," "," "," "," "),
	(25," "," "," "," "),
	(25," "," "," "," "),
	(26," "," "," "," "),
	(26," "," "," "," "),
	(27," "," "," "," "),
	(27," "," "," "," "),
	(28," "," "," "," "),
	(28," "," "," "," "),
	(29," "," "," "," "),
	(29," "," "," "," "),
	(30," "," "," "," "),
	(30," "," "," "," ");
	