-- Jake
-- Research and Analysis on Yelp DataBase based on ER Diagram.
-- Some Parts of the SQL code and Analysis are Hided.

		SELECT *
		FROM  user
		WHERE 	id is null
				or name is null
				or review_count is null
				or yelping_since is null
				or useful is null
				or funny is null
				or cool is null
				or fans is null
				or average_stars is null
				or compliment_hot is null
				or compliment_more is null
				or compliment_profile is null
				or compliment_cute is null
				or compliment_list is null
				or compliment_note is null
				or compliment_plain is null
				or compliment_cool is null
				or compliment_funny is null
				or compliment_writer is null
				or compliment_photos is null

	
	SELECT City, SUM(review_count)
	FROM Business
	GROUP BY City
	ORDER BY SUM(review_count) DESC
	

-- +-----------------+-------------------+
-- | city            | SUM(review_count) |
-- +-----------------+-------------------+
-- | Las Vegas       |             82854 |
-- | Phoenix         |             34503 |
-- | Toronto         |             24113 |
-- | Scottsdale      |             20614 |
-- | Charlotte       |             12523 |
-- | Henderson       |             10871 |
-- | Tempe           |             10504 |
-- | Pittsburgh      |              9798 |
-- | Montreal        |              9448 |
-- | Chandler        |              8112 |
-- | Mesa            |              6875 |
-- | Gilbert         |              6380 |
-- | Cleveland       |              5593 |
-- | Madison         |              5265 |
-- | Glendale        |              4406 |
-- | Mississauga     |              3814 |
-- | Edinburgh       |              2792 |
-- | Peoria          |              2624 |
-- | North Las Vegas |              2438 |
-- | Markham         |              2352 |
-- | Champaign       |              2029 |
-- | Stuttgart       |              1849 |
-- | Surprise        |              1520 |
-- | Lakewood        |              1465 |
-- | Goodyear        |              1155 |
-- +-----------------+-------------------+

SELECT stars AS [star rating], 
count(stars) AS [count]
FROM Business
WHERE city = 'Avon'
GROUP BY stars


-- +-------------+-------+
-- | star rating | count |
-- +-------------+-------+
-- |         1.5 |     1 |
-- |         2.5 |     2 |
-- |         3.5 |     3 |
-- |         4.0 |     2 |
-- |         4.5 |     1 |
-- |         5.0 |     1 |
-- +-------------+-------+

		
-- +--------+--------------+
-- | name   | review_count |
-- +--------+--------------+
-- | Gerald |         2000 |
-- | Sara   |         1629 |
-- | Yuri   |         1339 |
-- +--------+--------------+	


SELECT name, review_count, fans
FROM user
ORDER BY fans DESC
LIMIT 20


-- +-----------+--------------+------+
-- | name      | review_count | fans |
-- +-----------+--------------+------+
-- | Amy       |          609 |  503 |
-- | Mimi      |          968 |  497 |
-- | Harald    |         1153 |  311 |
-- | Gerald    |         2000 |  253 |
-- | Christine |          930 |  173 |
-- | Lisa      |          813 |  159 |
-- | Cat       |          377 |  133 |
-- | William   |         1215 |  126 |
-- | Fran      |          862 |  124 |
-- | Lissa     |          834 |  120 |
-- | Mark      |          861 |  115 |
-- | Tiffany   |          408 |  111 |
-- | bernice   |          255 |  105 |
-- | Roanna    |         1039 |  104 |
-- | Angela    |          694 |  101 |
-- | .Hon      |         1246 |  101 |
-- | Ben       |          307 |   96 |
-- | Linda     |          584 |   89 |
-- | Christina |          842 |   85 |
-- | Jessica   |          220 |   84 |
-- +-----------+--------------+------+

	
SELECT name, fans 
FROM user
ORDER BY fans DESC
LIMIT 10

-- +-----------+------+
-- | name      | fans |
-- +-----------+------+
-- | Amy       |  503 |
-- | Mimi      |  497 |
-- | Harald    |  311 |
-- | Gerald    |  253 |
-- | Christine |  173 |
-- | Lisa      |  159 |
-- | Cat       |  133 |
-- | William   |  126 |
-- | Fran      |  124 |
-- | Lissa     |  120 |
-- +-----------+------+
	
         
-- +----------+-----------+---------------+-------------------+--------------+----------------------+
-- | category | city      | average_stars | number_Resturants | review_count | hours                |
-- +----------+-----------+---------------+-------------------+--------------+----------------------+
-- | Korean   | Toronto   |           4.5 |                 7 |            8 | Saturday|11:00-23:00 |
-- | Chinese  | Las Vegas | 3.76923076923 |                13 |          768 | Saturday|10:00-23:00 |
-- | French   | Las Vegas |           4.0 |                12 |          168 | Saturday|11:00-20:00 |
-- | Spanish  | Toronto   |           4.0 |                 5 |           89 | Saturday|18:00-23:00 |
-- | Indian   | Aurora    |           3.5 |                 6 |           32 | Saturday|11:30-14:00 |
-- | Japanese | Toronto   |         3.475 |                20 |            5 | Saturday|11:00-23:00 |
-- +----------+-----------+---------------+-------------------+--------------+----------------------+

SELECT 
C.category,
B.City, 
Avg(B.Stars) AS average_stars,
count(B.Name) AS number_Resturants,
B.review_count,
H.hours
FROM (business B 
INNER JOIN category C on B.id = C.business_id)
INNER JOIN hours H on H.business_id = B.id
WHERE C.category IN ('Chinese', 'Japanese', 'Korean', 'French', 
'Indian', 'Spanish')
GROUP BY C.category
ORDER BY stars DESC
		
