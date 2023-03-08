# DROP DATABASE if EXISTS tietovisa;
#USE flight_game;

DROP TABLE if EXISTS pisteet;

DROP table if EXISTS vastaukset;
DROP table if EXISTS maat;
DROP table if EXISTS käyttäjä;


CREATE TABLE maat(
    ID      			INT       	 	NOT NULL,
    Nimi    			VARCHAR(64)    NOT NULL,
	 iso_country		VARCHAR (64)	,	
    PRIMARY KEY (ID),
    FOREIGN KEY (iso_country) REFERENCES country (iso_country)
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
	pisteet 		INT 				,				
	PRIMARY KEY (ID)				
);

INSERT INTO käyttäjä (Nimi, pisteet)
	VALUES ("Petra", 0),
	("Mia", 0),
	("Wilma", 0),
	("Julia", 0);

	INSERT INTO maat (ID, Nimi, iso_country)
    VALUES (1, "Iso-Britannia", "GB"),
	 (2, "Ranska","FR"),
	 (3, "Italia","IT"),
	 (4, "Espanja","ES"),
	 (5, "Saksa","DE"),
	 (6, "Kreikka", "GR"),
	 (7, "Suomi", "FI"),
	 (8, "Ruotsi", "SE"),
	 (9, "Romania", "RO"),
	 (10, "Puola", "PL"),
	 (11, "Bulgaria", "BG"),
	 (12, "Slovenia", "SI"),
	 (13, "Slovakia", "SK"),
	 (14, "Itävalta","AT"),
	 (15, "Norja","NO"),
	 (16, "Viro","EE"),
	 (17, "Latvia", "LV"),
	 (18, "Islanti", "IS"),
	 (19, "Irlanti", "IE"),
	 (20, "Portugali", "PT"),
	 (21, "Alankomaat", "NL"),
	 (22, "Ukraina", "UA"),
	 (23, "Montenegro", "ME"),
	 (24, "Kypros", "CY"),
	 (25, "Malta","MT"),
	 (26, "Sveitsi", "CH"),
	 (27, "Tsekki", "CZ"),
	 (28, "Belgia","BE"),
	 (29, "Serbia","RS"),
	 (30, "Moldova","MD");
	 
	 
	
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
	(15,"Norjan perustaja ja ensimmäinen kuningas oli:","Harald Kaunotukka","Pyhä Olavi","Eerik Verikirves"),(16,"Virossa sijaitseva ylioistokaupunki on nimeltään:","Tartto","Pärnu","Narva"),
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
	(26,"Mikä maa sijaitsee Sveitsin länsipuolella?","Ranska","Belgia","Saksa"),
	(26,"Mikä taidesuuntaus sai alkunsa Sveitsissä","Dadaismi","Ekspressionismi","Surrealismi"),
	(27,"Mikä on Tsekin valuutta?","Tsekin koruna","Euro","Frangi"),
	(27,"Milloin Tsekin jääkiekkomaajoukkue voitti viimeksi maailmanmestaruuden?","2010","2007","1994"),
	(28,"Mikä sarjakuva on lähtöisin Belgiasta?","Smurffit","Asterix ja Obelix","Tex Willer"),
	(28,"Kuinka monta Unescon maailmaperintökohdetta Belgiassa on?","10","4","8"),
	(29,"Mikä on Serbian väkiluku?","Noin 6,7 miljoonaa","Noin 7,4 miljoonaa","Noin 8,2 miljoonaa"),
	(29,"Kuka on Serbian nykyinen presidentti?","Alexsandar Vucic","Novak Dokovic","Ana Brnabic"),
	(30,"Kuinka korkea on Moldovan korkein kohta?","420 metriä","640 metriä","310 metriä"),
	(30,"Mikä on Moldovan virallinen kieli?","Romanian kieli","Moldovan kieli","Unkarin kieli"); 
	

	