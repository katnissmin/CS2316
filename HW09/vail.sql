DROP DATABASE IF EXISTS vail;
CREATE DATABASE IF NOT EXISTS vail;
USE vail;

DROP TABLE IF EXISTS areas;
CREATE TABLE areas (
	areaname 		VARCHAR (30) 	NOT NULL UNIQUE,
	pheight 		INTEGER (5),
    bheight			INTEGER (5),
	verticle 		INTEGER (5),
	atype			ENUM('Bowl', 'Basin', 'Peak', 'MISC') NOT NULL,
	PRIMARY KEY     (areaname)
);

DROP TABLE IF EXISTS lifts;
CREATE TABLE lifts (
	liftnumber 		INTEGER (2) NOT NULL UNIQUE,
    liftname 		VARCHAR (30) NOT NULL,
    lifttype 		ENUM('Express', 'Chair', 'Downloading', 'Gondola', 'Surface', 'Magic Carpet') NOT NULL,
    openingtime 	CHAR (5),
    closingtime 	CHAR (5),
    capacity		INTEGER (2),
    num_runs 		INTEGER (2),
    PRIMARY KEY 	(liftnumber)
);

DROP TABLE IF EXISTS runs;
CREATE TABLE runs (
	runname	  		VARCHAR (30) NOT NULL UNIQUE,
    location  		VARCHAR (30) NOT NULL,
    accessed_by 	INTEGER (2),
    level 	  		ENUM    ('Green', 'Blue', 'Black', 'Double Black', 'Terrain Park', 'Adventure Zone') NOT NULL,
    snow_status 	ENUM    ('Groomed', 'Ungroomed') NOT NULL,
    status			ENUM    ('Open', 'Closed') NOT NULL,
    run_type 	    ENUM	('Run', 'Glade', 'Chute', 'Meadow') NOT NULL,
    known_obstacle  VARCHAR (30),
    PRIMARY KEY     (runname),
    FOREIGN KEY 	(location) REFERENCES areas(areaname),
    FOREIGN KEY 	(accessed_by) REFERENCES lifts(liftnumber)
);

INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Blue Sky', 11570, null, 1900, 'Basin');
INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('China', 11375, null, 1535, 'Bowl');
INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Game Creak', null, 10981, 1900, 'Bowl');
INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Golden', 9600, null, 1400, 'Peak');
INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Mid-Vail', 11250, null, 1060, 'MISC');
INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Mongolia', 11455, null, 1615, 'Bowl');
INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Siberia', 11455, null, 1615, 'Bowl');

INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (37, 'Skyline', 'Express', '10:00', '14:30', 4, null);
INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (39, 'Petes', 'Express', '10:00', '14:15', 4, null);
INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (36, 'Tea Cup', 'Express', '09:00', '15:00', 4, null);
INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (24, 'Wapiti', 'Surface', null, null, 1, null);
INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (21, 'Orient', 'Express', '09:00', '15:00', 4, null);
INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (22, 'Mongolia', 'Surface', '09:00', '14:45', 1, null);
INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (2, 'Avanti', 'Express', '08:30', '16:00', 6, null);
INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (19, 'Eagle Bahn', 'Gondola', '08:30', '16:00', 8, null);

INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Lovers Leap', 'Blue Sky', 37, 'Black', 'Ungroomed', 'Open', 'Glade', 'Cliffs');
INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Resolution', 'Blue Sky', 39, 'Black', 'Ungroomed', 'Open', 'Glade', null);
INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('In The Wuides', 'Blue Sky', 37, 'Blue', 'Ungroomed', 'Open', 'Meadow', 'Cliffs');
INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Genghis Khan', 'China', 36, 'Black', 'Ungroomed', 'Open', 'Meadow', null);
INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Red Square', 'Siberia', 21, 'Black', 'Ungroomed', 'Open', 'Glade', 'Cliffs');
INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Bolshoi Ballroom', 'Siberia', 21, 'Black', 'Ungroomed', 'Open', 'Glade', 'Trees');
INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Inner Mongolia', 'Blue Sky', 22, 'Black', 'Ungroomed', 'Open', 'Glade', 'Ravine');
INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('O.S.', 'Blue Sky', 37, 'Black', 'Ungroomed', 'Open', 'Chute', 'Cliffs');

