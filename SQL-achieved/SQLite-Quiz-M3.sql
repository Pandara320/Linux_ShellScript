/*
QUIZ3

All of the questions in this
quiz pull from the open source Chinook Database. Please refer to the ER Diagram below and familiarize yourself with the table and
column names to write accurate queries and get the appropriate
answers.
*/

/*
1.How many albums does the artist Led Zeppelin
have? 
*/
SELECT count(AlbumId)
FROM (ALBUMS INNER JOIN ARTISTS ON ALBUMS.ArtistId = ARTISTS.ArtistId) 
WHERE ARTISTS.NAME == 'Led Zeppelin'  

-- 2.Create a list of album titles and the unit prices for the artist "Audioslave".

SELECT ALB.Title, TRK.UnitPrice, ART.Name
FROM ((ALBUMS ALB INNER JOIN ARTISTS ART
ON ALB.ArtistId = ART. ArtistId)
INNER JOIN TRACKS TRK ON ALB.Albumid = TRK.Albumid)
WHERE ART.Name = 'Audioslave'

-- 3.Find the first and last name of any customer who
-- does not have an invoice. Are there any customers returned from the query?  

SELECT CUST.FirstName, CUST.LastName
FROM customerS CUST LEFT JOIN invoices IVC
ON CUST.CustomerId == IVC.CustomerId
WHERE IVC.CustomerID IS NULL


-- 4.What is the total price for the album “Big Ones”?

SELECT ALB.TITLE, SUM(TRK.Unitprice)
FROM albums ALB
	INNER JOIN tracks TRK ON ALB.Albumid = TRK.Albumid
WHERE ALB.Title = 'Big Ones'
GROUP BY ALB.Title

-- 5.How many records are created when you apply a Cartesian join to the invoice and invoice items table?

SELECT COUNT(*)
FROM invoices CROSS JOIN invoice_items
