--check what tables exist
SELECT
  *
FROM
  SYSOBJECTS
WHERE
  xtype = 'U';
GO