/*Q21:*/

SELECT 
TrackId
FROM Tracks
WHERE Milliseconds > 5000000;

/*Q2:*/

SELECT
*
FROM Invoices
WHERE Total BETWEEN 5 AND 15

/*Q3:*/

SELECT 
*
FROM Customers
WHERE State IN ('RJ','DF', 'AB', 'BC', 'CA', 'WA', 'NY');

/*Q4:*/

SELECT 
*
FROM Invoices
WHERE CustomerID in ('56', '58') AND Total BETWEEN 1 AND 5;

/*Q5:*/

SELECT 
*
FROM Tracks
WHERE Name Like 'All%'

/*Q6:*/

SELECT *
FROM Customers
WHERE Email Like 'J%gmail.com'

/*Q7:*/

SELECT *
FROM Invoices 
WHERE BillingCity IN ('Brasilia', 'Edmonton', 'Vancouver')
ORDER BY InvoiceId DESC

Q8:

/*Q9:*/
SELECT
AlbumId
,Count(TrackId) AS More_Tracks
FROM Tracks
Group by AlbumId
HAVING Count(TrackId) >= 12
ORDER BY More_Tracks DESC;
