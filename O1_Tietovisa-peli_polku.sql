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
	(15," "," "," "," "),	
	(15," "," "," "," "),
	(16,"Virossa sijaitseva ylioistokaupunki on nimeltään:","Tartto","Pärnu","Narva"),
	(16,"Viron itsenäisyyspäivää juhlitaan:","24.helmikuuta","17.lokakuuta","4.kesäkuuta"),
	(17,"Latvian väkiluku on:","Noin 2 miljoonaa","Noin 3,5 miljoonaa","Noin 6 miljoonaa"),
	(17,"Latvia voitti Euroviisut vuonna:","2002","2011","2008"),
	(18,"Islannin tärkeimpiä tulonlähteitä ovat:","Kalastus ja turismi","Maatalous ja metsäteolisuus","Kaivostoiminta ja öljytuotanto"),
	(18,"Tuhmat lapset saavat lahjaksi Islannissa jouluna:","Perunan","Puun oksan","Sukan"),
	(19,"Irlannin kansalliskieli ja ensimmäinen virallinen kieli on:","Iiri","Irlanti","Gaeli"),
	(19,"Iralnnin alkoholinkulutus on maailmalla sijalla:","4","8","1"),
	(20,"Portugalin alkuperäinen nimitys Portus Cale tarkoittaa:","Kaunista satamaa","Taivaallista niemmimaata","Kultaista porttia"),
	(20,"Portugalissa sijaitsee maailman vanhin:","Kirjakauppa","Luostari","Olutpanimo"),
	(21,"Alankomaissa vallitsee:","Meri-ilmasto","Mannerilmasto","Väli-ilmasto"),
	(21,"Kuuluisa alankomainen taidemaalari:","Vincent Van Gogh","Leonardo Da Vinci","Albert Edelfelt"),
	(22,"Ukrainan jakaa läntiseen ja itäiseen osaan joki nimeltä:","Dnerp","Oder","Tonava"),
	(22,"Ukrainan pääkaupunki Kiovan väkiluku on:","Noin 2,8 miljoonaa","Noin 3,4 miljoonaa","Noin 4,6 miljonaa"),
	(23,"Mikä seuraavista maista on Montenergon rajanaapuri?","Albania","Kroatia","Bulgaria"),
	(23,"Kuinka monta kuntaa Montenegrosta on?","25","18","21"),
	(24,"Kuinka monta virallista kieltä Kyproksella on?","2","1","3"),
	(24,"Minä vuonna Kypros itsenäistyi?","1960","1965","1970"),
	(25,"Mikä on Maltan pääkaupunki?","Valletta","Tirana","Nikosia"),
	(25,"Lähin valtio Maltaa on:","Italia","Kreikka","Tunisia"),
	(26,"Mikä maa sijaitsee Sveitsin länsipuolella?","Ranska","Balgia","Saksa"),
	(26,"Mikä taidesuuntaus sai alkunsa Sveitsissä","Dadaismi","Ekspressionismi","Surrealismi"),
	(27,"Mikä on Tsekin valuutta?","Tsekin koruna","Euro","Frangi"),
	(27,"Milloin Tsekin jääkiekkomaajoukkue voitti viimeksi maailmanmestaruuden?","2010","2007","1994"),
	(28,"Mikä sarjakuva on lähtöisin Belgiasta?","Smurffit","Asterix ja Obelix","Tex Willer"),
	(28,"Kuinka monta Unescon maailmaperintökohdetta Belgiassa on?","10","4","8"),
	(29,"Mikä on Serbian väkiluku?","Noin 6,7 miljoonaa","Noin 7,4 miljoonaa","Noin 8,2 miljoonaa"),
	(29,"Kuka on Serbian nykyinen presidentti?","Alexsandar Vucic","Novak Dokovic","Ana Brnabic"),
	(30,"Kuinka korkea on Moldovan korkein kohta?","420 metriä","640 metriä","310 metriä"),
	(30,"Mikä on Moldovan virallinen kieli?","Romania","Moldova","Unkari"); 