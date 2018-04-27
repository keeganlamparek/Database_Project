IF DB_ID('ISP_Database') IS NULL CREATE DATABASE ISP_Database;
USE ISP_Database;
GO

IF OBJECT_ID('dbo.IPLeaseTable', 'U') IS NOT NULL
	DROP TABLE dbo.IPLeaseTable;

IF OBJECT_ID('dbo.IPHistoryTable', 'U') IS NOT NULL
	DROP TABLE dbo.IPHistoryTable;

IF OBJECT_ID('dbo.ModemTable', 'U') IS NOT NULL
	DROP TABLE dbo.ModemTable;

IF OBJECT_ID('dbo.IPAddressTable', 'U') IS NOT NULL
	DROP TABLE dbo.IPAddressTable;

IF OBJECT_ID('dbo.IPScopeTable', 'U') IS NOT NULL
	DROP TABLE dbo.IPScopeTable;

IF OBJECT_ID('dbo.CityTable', 'U') IS NOT NULL
	DROP TABLE dbo.CityTable;
GO

CREATE TABLE dbo.CityTable
(	CityID       INT           PRIMARY KEY,
	CityName     VARCHAR(20)   NOT NULL,
	CityPopulation INT         NOT NULL
)

CREATE TABLE dbo.IPScopeTable
(	ScopeID     INT      PRIMARY KEY,
	IPScope     VARCHAR(20)  NOT NULL,
	CityID      INT,
	FOREIGN KEY(CityID) REFERENCES dbo.CityTable(CityID) 
)

CREATE TABLE dbo.IPAddressTable
(	IPAddressID    INT     PRIMARY KEY IDENTITY,
	IPAddress      VARCHAR(20)    NOT NULL,
	ScopeID        INT            NOT NULL,
	FOREIGN KEY(ScopeID) REFERENCES dbo.IPScopeTable(ScopeID)
)

CREATE TABLE dbo.ModemTable
(	ModemID    INT    PRIMARY KEY,
	SerialName   VARCHAR(20)  NOT NULL,
	IPAddressID   INT,
	CityAddress   VARCHAR(50)     NOT NULL,
	FOREIGN KEY(IPAddressID) REFERENCES dbo.IPAddressTable(IPAddressID)
)

CREATE TABLE dbo.IPHistoryTable
(	HistoryID    INT    PRIMARY KEY,
	DateAssigned  datetime  NOT NULL,
	Expiration_Date  datetime  NOT NULL
)

CREATE TABLE dbo.IPLeaseTable
(	LeaseID    INT    PRIMARY KEY,
	AddressID   INT  NOT NULL,
	HistoryID    INT  NOT NULL,
	FOREIGN KEY(AddressID) REFERENCES dbo.IPAddressTable(IPAddressID),
	FOREIGN KEY(HistoryID) REFERENCES dbo.IPHistoryTable(HistoryID)
)

GO
INSERT INTO dbo.Citytable(CityID, CityName, CityPopulation)
VALUES(1, 'DalesBurg', 20000),
(2, 'Champville', 10000),
(3, 'Dimmavale', 9000),
(4, 'Rail Central', 17000),
(5, 'Rits Valley', 50000);
