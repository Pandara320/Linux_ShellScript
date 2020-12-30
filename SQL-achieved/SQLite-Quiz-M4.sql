-- Quiz4
-- All of the questions in this quiz refer to the open source Chinook Database. 
-- Please familiarize yourself with the ER diagram in order to familiarize yourself 
-- with the table and column names in order to write accurate queries and get the appropriate answers.

-- Question 1
-- Pull a list of customer ids with the customer’s full name, and address, 
-- along with combining their city and country together.
-- Be sure to make a space in between these two and make it UPPER CASE. (e.g. LOS ANGELES USA)

SELECT 
C.CustomerId, C.FirstName || ' ' || C.LastName AS FullName, c.Address,
UPPER(C.City || ' ' || C.Country) AS FullAddress 
FROM Customers C

-- Question 2
-- Create a new employee user id by combining the first 4 letters of the employee’s first name 
-- with the first 2 letters of the employee’s last name. 
-- Make the new field lower case and pull each individual step to show your work.
-- What is the final result for Robert King?

SELECT C.FirstName, C.LastName,
SUBSTR(C.FirstName, 1, 4) as FirstNameFragment,
SUBSTR(C.LastName, 1, 2) as LastNameFragment,
LOWER(SUBSTR(C.FirstName, 1, 4) || SUBSTR(C.LastName, 1, 2)) AS New_ID
FROM Customers C
ORDER BY C.LastName

-- Question 3
-- Show a list of employees who have worked for 
-- the company for 15 or more years using the current date function. Sort by lastname ascending.
-- What is the lastname of the last person on the list returned?
SELECT E.LastName, E.FirstName, E.BirthDate, E.HireDate, DATE('now'), 
DATE('now')- DATE(E.HireDate) AS Term
FROM Employees E
WHERE Term >= 15
ORDER BY E.LastName ASC

-- Question 4
-- Profiling the Customers table, answer the following question.
-- Are there any columns with null values? Indicate any below. Select all that apply.

SELECT *
FROM Customers C
-- WHERE C.Company is NULL
-- WHERE C.Address is NULL
-- WHERE C.FirstName is NULL
WHERE C.Phone is NULL

-- Question 5
-- Find the cities with the most customers and rank in descending order.
-- Which of the following cities indicate having 2 customers?

SELECT C.City, COUNT(C.CustomerId)
FROM Customers C
GROUP BY C.City
ORDER BY COUNT(C.CustomerId) DESC


-- Question 6
-- Create a new customer invoice id by combining a customer’s 
-- invoice id with their first and last name while ordering your query in the following order: 
-- firstname, lastname, and invoiceID.
-- Select all of the correct "AstridGruber" entries
-- that are returned in your results below. Select all that apply.

SELECT C.FirstName || C.LastName || I.InvoiceId as NewInvoiceID
FROM Customers C JOIN Invoices I
on C.CustomerId = I.CustomerId
WHERE NewInvoiceID like 'AstridGruber%'
ORDER BY C.FirstName, C.LastName, I.InvoiceId ASC

