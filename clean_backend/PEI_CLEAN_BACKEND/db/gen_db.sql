CREATE DATABASE PROTECTME;
use PROTECTME;
use master;
GO

DROP TABLE dbo.ANALYSIS
DROP TABLE dbo.MEDIA
DROP TABLE dbo.RELATED
DROP TABLE dbo.RESULT
DROP TABLE dbo.TOPICS
DROP TABLE dbo.TWEETS


use PROTECTME;
CREATE TABLE TWEETS(
	id varchar(30) PRIMARY KEY,
	thread_id int,
	likes int,
	comments_num int,
	retweets int,
	related_media bit,
);

CREATE TABLE TOPICS(
	id int IDENTITY primary key,
	keyword varchar(30),
	constraint uniq_key UNIQUE(keyword)
);


Create Table RELATED(
	tweet_id varchar(30) foreign key references TWEETS(id),
	topic_id int foreign key references TOPICS(id),
);

CREATE TABLE ANALYSIS(
	id int IDENTITY primary key,
	analysis_date date,
	tweet_id varchar(30) foreign key references TWEETS(id),
);
ALTER TABLE ANALYSIS ADD CONSTRAINT
anal_today DEFAULT getdate() FOR analysis_date

CREATE TABLE MEDIA(
	id int IDENTITY primary key,
	tweet_id varchar(30) foreign key references TWEETS(id),
	media_type varchar(20),
	media_url nvarchar(2083) --nvarchar(2083) to support multilingual urls and remove the need for url encoding
	--see https://stackoverflow.com/questions/1159928/what-is-the-best-column-type-for-url
);

CREATE TABLE RESULT(
	analysis_id int foreign key references ANALYSIS(id),
	framework varchar(50),
	res nvarchar(max),
)

-- Checks if data stored in media analysis field is formatted as a json file
Alter table RESULT ADD CONSTRAINT [retrieved_data RECORD should be formatted as JSON] CHECK (ISJSON(res)=1)


CREATE LOGIN teste WITH PASSWORD = 'Testeeeeeeeee.';
GO

CREATE USER teste FROM LOGIN teste;

EXEC sp_addrolemember 'db_owner', 'teste';

SELECT * FROM dbo.TWEETS

SELECT * FROM dbo.ANALYSIS

SELECT * FROM dbo.TOPICS

SELECT * FROM dbo.RESULT WHERE framework='monkeylearn'

SELECT * FROM dbo.MEDIA
