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
	(2,"Kuinka korkea on Eiffel-torni?","324 metriä","264 metriä","412 metriä"),
	(3,"Missä kaupungissa siaitsee kuuluisa kalteva torni?","Pisa","Napoli","Torino"),
	(3,"Mikä on Italian suurin saari?","Sisilia","Sardinia","Elba"),
	(4,"Missä kaupungissa on suurin väkiluku?","Madrid","Barcelona","Valencia"),
	(4,"Mikä on Espanjan suurin saari?","Mallorca","Teneriffa","Gran Canaria"),
	(5,"Mikä on Saksan suurin kaupunki väkiluvultaan?","Berliini","Hampuri","München"),
	(5,"Mikä on Saksan suurin järvi?","Bodensee","Eibsee","Chiemsee"),
	(6,"Mikä on Kreikan kansallisurheilulaji?","Paini","Jalkapallo","Viesti"),
	(6,"Minkä niminen on Kreikan tunnetuin antiikin aikainen temppeli?","Parthenon"," Pantheon","Patheon"),
	(7,"Mikä on Suomen pohjoisin kunta?","Utsjoki","Inari","Enontekijö"),
	(7,"Kuka on Suomen seitsemäs presidentti?","Paasikivi","Ryti","Kekkonen"),
	(8,"Mikä on Ruotsin toiseksi suurin kaupunki?","Göteborg","Tukholma","Malmö"),
	(8,"Monta virallista vähemmistökieltä Ruotsilla on?","5 Kieltä","2 Kieltä","3 Kieltä"),
	(9,"Monta naapurimaata Romanialla on?","5","6","7"),
	(9,"Kehen Romanian hallitsijaan Dracula perustuu?","Vlad Tepes","István Báthory","János Hunyadi"),
	(10,"Mikä on Puolan suurin uskonto?","Katolinen kirkko","Ortodoksinen kirkko","Protestantinen kirkko"),
	(10,"Mikä on Puolan pisin joki?","Veiksel","Oder","Warta"),
	(11,"Mikä on Bulgarian pääkaupunki?","Sofia","Vilna","Wien"),
	(11,"Mikä on Bulgarian suurin satamakaupunki?","Varna","Burgas","Plovdiv"),
	(12,"Mikä maa tunnusti Slovenian itesenäisyyden ensin?","Kroatia","Itävalta","Serbia"),
	(12,"Mikä leivonnainen on kotoisin Slovakiasta?","Potica","Medimurska","Banket"),
	(13,"Mitkä on Slovakian lipun värit?","Valkoinen, sininen ja punainen","Keltainen, vihreä ja punainen","Oranssi, valkoinen ja vihreä"),
	(13,"Mikä on Slovakian katsotuin urheilulaji?","Jääkiekko","Jalkapallo","Tennis"),
	(14,"Mikä on Itävallan virallinen kieli?","Saksa","Kroatia","Unkari"),
	(14,"Monta osavaltiota Itävallalla on?","9","13","17"),
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
	