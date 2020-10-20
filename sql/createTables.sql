CREATE TABLE IF NOT EXISTS stations (
    RLOIid INTEGER,
    catchmentName VARCHAR(100),
    dateOpened DATE,
    easting INTEGER,
    label VARCHAR(100),
    lat REAL,
    long REAL,
    northing INTEGER,
    notation VARCHAR(20) PRIMARY KEY,
    riverName VARCHAR(100),
    stationReference VARCHAR(50),
    town VARCHAR(100),
    wiskiID VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS measurements (
    datetime TIMESTAMP,
    date DATE,
    label VARCHAR(100),
    stationreference VARCHAR(50),
    parameter VARCHAR(50),
    qualifier VARCHAR(50),
    period INTEGER,
    unitname VARCHAR(10),
    valuetype VARCHAR(20),
    value REAL/*,
    PRIMARY KEY (datetime,stationReference),
    CONSTRAINT fk_stations 
        FOREIGN KEY(stationReference)
            REFERENCES stations(notation)*/
);