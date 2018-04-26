IF DB_ID('ISP_Database') IS NULL CREATE DATABASE ISP_Database;
USE ISP_Database;
GO

IF OBJECT_ID('dbo.IPLease', 'U') IS NOT NULL
	DROP TABLE dbo.IPLease;

IF OBJECT_ID('dbo.IPHistory', 'U') IS NOT NULL
	DROP TABLE dbo.IPHistory;

IF OBJECT_ID('dbo.Modem', 'U') IS NOT NULL
	DROP TABLE dbo.Modem;

IF OBJECT_ID('dbo.IPAddress', 'U') IS NOT NULL
	DROP TABLE dbo.IPAddress;

IF OBJECT_ID('dbo.IPScope', 'U') IS NOT NULL
	DROP TABLE dbo.IPScope;

IF OBJECT_ID('dbo.City', 'U') IS NOT NULL
	DROP TABLE dbo.City;
GO

CREATE TABLE dbo.City
(	CityID       INT           PRIMARY KEY,
	CityName     VARCHAR(20)   NOT NULL,
	CityPopulation INT         NOT NULL
)

CREATE TABLE dbo.IPScope
(	ScopeID     INT      PRIMARY KEY,
	IPScope     VARCHAR(20)  NOT NULL,
	CityID      INT,
	FOREIGN KEY(CityID) REFERENCES dbo.City(CityID) 
)

CREATE TABLE dbo.IPAddress
(	IPAddressID    INT     PRIMARY KEY IDENTITY,
	IPAddress      VARCHAR(20)    NOT NULL,
	ScopeID        INT            NOT NULL,
	FOREIGN KEY(ScopeID) REFERENCES dbo.IPScope(ScopeID)
)

CREATE TABLE dbo.Modem
(	ModemID    INT    PRIMARY KEY,
	SerialName   VARCHAR(20)  NOT NULL,
	IPAddressID   INT,
	CityAddress   VARCHAR(50)     NOT NULL,
	FOREIGN KEY(IPAddressID) REFERENCES dbo.IPAddress(IPAddressID)
)

CREATE TABLE dbo.IPHistory
(	HistoryID    INT    PRIMARY KEY,
	DateAssigned  datetime  NOT NULL,
	Expiration_Date  datetime  NOT NULL
)

CREATE TABLE dbo.IPLease
(	LeaseID    INT    PRIMARY KEY,
	AddressID   INT  NOT NULL,
	HistoryID    INT  NOT NULL,
	FOREIGN KEY(AddressID) REFERENCES dbo.IPAddress(IPAddressID),
	FOREIGN KEY(HistoryID) REFERENCES dbo.IPHistory(HistoryID)
)

GO
INSERT INTO dbo.City(CityID, CityName, CityPopulation)
VALUES(1, 'DalesBurg', 20000),
(2, 'Champville', 10000),
(3, 'Dimmavale', 9000),
(4, 'Rail Central', 17000),
(5, 'Rits Valley', 50000);
