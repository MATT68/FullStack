-- connect / as sysdba;
-- create user forma2 identified by forma2;
-- grant connect,resource to forma2;
-- connect forma2/forma2;
--
-- use para MySQL
 create database db_empl;
 use db_empl;
 DROP TABLE TEMPLA;
 CREATE TABLE TEMPLA               
         (NUEMPL  CHAR(6)        NOT NULL, 
         NOMBRE   VARCHAR(12)    NOT NULL, 
         INICIAL  CHAR(1)        NOT NULL, 
         APELLIDO VARCHAR(15)    NOT NULL, 
         DEPT     CHAR(3)        NOT NULL, 
         TLFN     CHAR(4)                , 
         FECHING  DATE                   , 
         CODTRA   DECIMAL(3)             , 
         NIVEDUC  DECIMAL(6)               , 
         SEXO     CHAR(1)                , 
         FECHNAC  DATE                   , 
         SALARIO  DECIMAL(8, 2)          );
CREATE UNIQUE INDEX X1EMPLA   
       ON TEMPLA                     
       (NUEMPL ASC);
DROP TABLE TDEPTA;
CREATE TABLE TDEPTA                    
       (NUMDEP   CHAR(3)        NOT NULL,      
        NOMDEP   VARCHAR(36)    NOT NULL,      
        NUMDIREC CHAR(6)        NOT NULL);
CREATE UNIQUE INDEX x1DEPTA     
       ON TDEPTA                       
       (NUMDEP ASC);
DROP table aumsal;
create table aumsal
       (nuempl    char(6) NOT NULL,
        fechaaum  DATE,
        AUMENTO   DECIMAL(8,2) NOT NULL);
DROP TABLE HIJOS;
CREATE TABLE HIJOS
       (NUEMPL   CHAR(6) NOT NULL,
        NOMBRE   VARCHAR(12),
        APELLIDO VARCHAR(15),
        FECHNAC  DATE);
DROP TABLE CONYUGES;
CREATE TABLE CONYUGES
        (NUEMPL   CHAR(6) NOT NULL,
        NOMBRE   VARCHAR(12),
        APELLIDO VARCHAR(15),
        FECHNAC  DATE);       
INSERT INTO AUMSAL VALUES ('000010',  '2000-12-15',9000.00);
INSERT INTO AUMSAL VALUES ('000020',  '2000-12-15',     9000.00);
INSERT INTO AUMSAL VALUES ('000030',  '2001-01-15',     3000.00);
INSERT INTO AUMSAL VALUES ('000050',  '2001-06-20',     3000.00);
INSERT INTO AUMSAL VALUES ('000060',  '1999-05-23',     2000.00);
INSERT INTO AUMSAL VALUES ('000070',  '1998-11-14',     4000.00);
INSERT INTO AUMSAL VALUES ('000090',  '2000-03-05',     6000.00);
INSERT INTO AUMSAL VALUES ('000110',  '2000-01-20',     3000.00);
INSERT INTO AUMSAL VALUES ('000120',  '2001-06-15',     2000.00);
INSERT INTO AUMSAL VALUES ('000130',  '2000-09-05',     6000.00);
INSERT INTO AUMSAL VALUES ('000140',  '2000-11-04',     7000.00);
INSERT INTO AUMSAL VALUES ('000150',  '2001-05-20',     6000.00);
INSERT INTO AUMSAL VALUES ('000160',  '2000-03-05',     6000.00);
INSERT INTO AUMSAL VALUES ('000170',  '2000-03-05',     6000.00);
INSERT INTO AUMSAL VALUES ('000180',  '2001-04-15',     6000.00);
INSERT INTO AUMSAL VALUES ('000190',  '2000-01-20',     3000.00);
INSERT INTO AUMSAL VALUES ('000200',  '2001-04-15',     3000.00);
INSERT INTO AUMSAL VALUES ('000210',  '2001-01-20',     3000.00);
INSERT INTO AUMSAL VALUES ('000220',  '1999-05-23',     2000.00);
INSERT INTO AUMSAL VALUES ('000230',  '1998-11-14',     4000.00);
INSERT INTO AUMSAL VALUES ('000240',  '2000-03-05',     6000.00);
INSERT INTO AUMSAL VALUES ('000250',  '2001-06-15',    6000.00);
INSERT INTO AUMSAL VALUES ('000260',  '2000-01-20',     3000.00);
INSERT INTO AUMSAL VALUES ('000280',  '2000-09-05',     6000.00);
INSERT INTO AUMSAL VALUES ('000300',  '2001-12-01',     3000.00);
INSERT INTO AUMSAL VALUES ('000310',  '2000-05-09',     6000.00);
INSERT INTO AUMSAL VALUES ('000320',  '2000-04-11',     7000.00);
INSERT INTO AUMSAL VALUES ('000330',  '2001-12-06',     6000.00);
INSERT INTO AUMSAL VALUES ('000340',  '2000-05-03',     6000.00);
       
INSERT INTO CONYUGES VALUES ('000010','JUAN','GARRIDO',      '1945-09-15');
INSERT INTO CONYUGES VALUES ('000050','CRISTINA','HERNANDEZ','1953-08-14');
INSERT INTO CONYUGES VALUES ('000060','CRISTINA','MARTIN',   '1968-09-14');
INSERT INTO CONYUGES VALUES ('000070','TOMAS','SOLER',       '1961-12-18');
INSERT INTO CONYUGES VALUES ('000100','EVA','PUENTE',        '1963-05-26');
INSERT INTO CONYUGES VALUES ('000120','ELISA','PINTO',       '1975-04-12');
INSERT INTO CONYUGES VALUES ('000160','SIMON','OTERO',       '1962-10-18');
INSERT INTO CONYUGES VALUES ('000190','MARTA','PASCUAL',     '1976-03-03');
INSERT INTO CONYUGES VALUES ('000210','EUGENIA','MARTINEZ',  '1978-08-29');
INSERT INTO CONYUGES VALUES ('000230','MIRIAM','SASTRE',     '1966-11-21');
INSERT INTO CONYUGES VALUES ('000310','EDUARDO','RUIZ',      '1944-09-12');
INSERT INTO CONYUGES VALUES ('000340','MARINA','SALVAT',     '1965-07-07');

INSERT INTO HIJOS VALUES ('000310','RAMON','GARCIA',   '1985-04-07');
INSERT INTO HIJOS VALUES ('000310','MARISA','GARCIA',  '1984-07-12');
INSERT INTO HIJOS VALUES ('000240','DANIEL','MARTINEZ','1999-12-05');
INSERT INTO HIJOS VALUES ('000240','JOSE','MARTINEZ',  '1999-12-05');
INSERT INTO HIJOS VALUES ('000230','MIRIAM','JIMENEZ', '1986-12-21');
INSERT INTO HIJOS VALUES ('000220','ANTONIO','MARTIN', '1998-08-29');
INSERT INTO HIJOS VALUES ('000200','FEDERICO','BONDIA','1996-04-03');
INSERT INTO HIJOS VALUES ('000180','ANA','SANCHEZ',    '1993-07-07');
INSERT INTO HIJOS VALUES ('000170','JORGE','YARZA',    '1998-09-15');
INSERT INTO HIJOS VALUES ('000120','JUAN','OTERO',     '1990-12-05');
INSERT INTO HIJOS VALUES ('000130','ELISA','QUINTAS',  '1981-07-28');
INSERT INTO HIJOS VALUES ('000100','ELENA','SOLER',    '1988-08-15');
INSERT INTO HIJOS VALUES ('000100','DOLORES','SOLER',  '1997-09-30');
INSERT INTO HIJOS VALUES ('000070','ELENA','SOLER',    '1988-08-15');
INSERT INTO HIJOS VALUES ('000070','DOLORES','SOLER',  '1997-09-30');
INSERT INTO HIJOS VALUES ('000060','ISIDRO','SUAREZ',  '1988-09-14');
INSERT INTO HIJOS VALUES ('000050','CARLOS','GARRIDO', '1980-07-01');
INSERT INTO HIJOS VALUES ('000050','EVA','GARRIDO',    '1989-08-17');
INSERT INTO HIJOS VALUES ('000010','EVA','GARRIDO',    '1989-08-17');
INSERT INTO HIJOS VALUES ('000010','CARLOS','GARRIDO', '1980-07-01');  

INSERT INTO TDEPTA VALUES ('A00','SPIFFY COMPUTER SERVICE DIV.','000010');
INSERT INTO TDEPTA VALUES ('B01','PLANNING','000020');  
INSERT INTO TDEPTA VALUES ('C01','INF.CENTER','000030');  
INSERT INTO TDEPTA VALUES ('D01','DEVELOPMENT CENTER','000260');
INSERT INTO TDEPTA VALUES ('E01','SUPPORT SERVICES','000050'); 
INSERT INTO TDEPTA VALUES ('D11','MANUFACTURING SYSTEMS','000060'); 
INSERT INTO TDEPTA VALUES ('D21','ADMINISTRATION SYSTEMS','000070');
INSERT INTO TDEPTA VALUES ('E11','OPERATIONS','000090');  
INSERT INTO TDEPTA VALUES ('E21','SOFTWARE SUPPORT','000100');

INSERT INTO TEMPLA VALUES ('000010','CRISTINA','I','HERNANDEZ','A00','3978','1985-01-01', 66.,  18,'F','1953-08-14', 52750.00);
INSERT INTO TEMPLA VALUES ('000020','MIGUEL','L','TAPIA','B01','3476',      '1993-10-10', 61.,  18,'M','1968-02-29',    41250.00);
INSERT INTO TEMPLA VALUES ('000030','SALOME','A','KEMPES','C01','4738',     '1995-04-05', 60.,  20,'F','1961-05-11',    38250.00);
INSERT INTO TEMPLA VALUES ('000050','JUAN','B','GARRIDO','E01','6789',      '1969-08-17', 58.,  16,'M','1945-09-15',    40175.00);
INSERT INTO TEMPLA VALUES ('000060','ISIDRO','F','SUAREZ','D11','6423',     '1993-09-14', 55.,  16,'M','1965-07-07',    32250.00);
INSERT INTO TEMPLA VALUES ('000070','EVA','D','PUENTE','D21','7831',        '2000-09-30', 56.,  16,'F','1963-05-26',    36170.00);
INSERT INTO TEMPLA VALUES ('000090','ELENA','W','HERRANZ','E11',NULL,       '1990-08-15', 55.,  16,'F','1961-05-15',    32725.00);
INSERT INTO TEMPLA VALUES ('000100','TOMAS','Q','SOLER','E21','0972',       '2000-06-19', 54.,  14,'M','1961-12-18',    31641.50);
INSERT INTO TEMPLA VALUES ('000110','VICENTE','G','LUENGO','A00','3490',    '1978-05-16', 58.,  19,'M','1949-11-05',    46500.00);
INSERT INTO TEMPLA VALUES ('000120','SIMON',' ','OTERO','A00','2167',       '1983-12-05', 58.,  14,'M','1962-10-18',    29250.00);
INSERT INTO TEMPLA VALUES ('000130','DOLORES','M','QUINTANA','C01','4578',  '1991-07-28', 55.,  16,'F','1945-09-15',    28798.00);
INSERT INTO TEMPLA VALUES ('000140','HELIODORA','A','NIETO','C01','1793',   '1996-12-15', 56.,  18,'F','1966-01-19',    31262.00);
INSERT INTO TEMPLA VALUES ('000150','BRUNO',' ','ALVAREZ','D11',NULL,       '1992-02-12', 55.,  16,'M','1967-05-17',    30588.80);
INSERT INTO TEMPLA VALUES ('000160','ELISA','R','PINTO','D11','3782',       '1997-10-11', 54.,  17,'F','1975-04-12',    26922.50);
INSERT INTO TEMPLA VALUES ('000170','MATEO','J','YARZA','D11','2890',       '1998-09-15', 54.,  16,'M','1971-01-05',    29862.80);
INSERT INTO TEMPLA VALUES ('000180','MARINA','S','SANDOVAL','D11','1682',   '1993-07-07', 53.,  17,'F','1969-02-21',    25821.40);
INSERT INTO TEMPLA VALUES ('000190','JAIME','H','WALKER','D11','2986',      '1994-07-26', 53.,  16,'M','1972-06-25',    24744.50);
INSERT INTO TEMPLA VALUES ('000200','DAVID',' ','BONDIA','D11','4501',      '1986-03-03', 55.,  16,'M','1961-05-29',    30514.00);
INSERT INTO TEMPLA VALUES ('000210','WENCESLAO','T','JURADO','D11','0942',  '1999-04-11', 52.,  17,'M','1973-02-23',    22106.70);
INSERT INTO TEMPLA VALUES ('000220','JIMENA','K','LUQUE','D11','0672',      '1988-08-29', 55.,  18,'F','1968-03-19',    32824.00);
INSERT INTO TEMPLA VALUES ('000230','JAIME','J','JIMENEZ','D21','2094',     '1986-11-21', 53.,  14,'M','1955-05-30',    26837.80);
INSERT INTO TEMPLA VALUES ('000240','SALVADOR','M','MARTINEZ','D21',NULL,   '1999-12-05', 55.,  17,'M','1974-03-31',    31636.00);
INSERT INTO TEMPLA VALUES ('000250','DANIEL','S','SIERRA','D21','0961',     '1989-10-30', 52.,  15,'M','1959-11-12',    23207.80);
INSERT INTO TEMPLA VALUES ('000260','SUSANA','V','JUNQUERA','D21','8953',   '1995-09-11', 52.,  16,'F','1956-10-05',    20872.50);
INSERT INTO TEMPLA VALUES ('000270','MARIA','L','PEREZ','D21','9001',       '2000-09-30', 55.,  15,'F','1973-05-26',    30118.00);
INSERT INTO TEMPLA VALUES ('000280','ENGRACIA','R','SANCHEZ','E11',NULL,    '1987-03-24', 54.,  17,'F','1956-03-28',    31762.50);
INSERT INTO TEMPLA VALUES ('000290','JUAN','R','PALACIOS','E11','4502',     '2000-05-30', 42.,  12,'M','1966-07-09',    24330.19);
INSERT INTO TEMPLA VALUES ('000300','PEDRO','X','SIERRA','E11','2095',      '1992-06-19', 48.,  14,'M','1956-10-27',    28152.59);
INSERT INTO TEMPLA VALUES ('000310','MATILDE','F','SERNA','E11','3332',     '1984-09-12', 43.,  12,'F','1951-04-21',    25218.39);
INSERT INTO TEMPLA VALUES ('000320','RAMON','V','MORAN','E21','9990',       '1985-07-07', 52.,  16,'M','1952-08-11',    24139.50);
INSERT INTO TEMPLA VALUES ('000330','WILLY',' ','LERMA','E21',NULL,         '1996-02-23', 55.,  14,'M','1961-07-18',    30697.70);
INSERT INTO TEMPLA VALUES ('000340','JAVIER','R','GIL','E21','5698',        '1967-05-05', 54.,  16,'M','1946-05-17',    28846.40);

commit;
