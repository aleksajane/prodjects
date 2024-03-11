select min("dateId"), MAX("dateId")
FROM distributor.remains

select "branchId", "itemId",
	t."dateId" AS "dateId",
	0 AS "remains"
FROM (SELECT "dateId", "branchId", "itemId", "min_date", "max_date"
		FROM (SELECT CAST('2014-01-13' AS Date) + s.a AS "dateId" FROM GENERATE_SERIES(0,365*3,1) AS s(a))
			  CROSS JOIN (select "branchId", "itemId", MIN("dateId") AS min_date, MAX("dateId") AS max_date FROM distributor.remains
						  GROUP BY "branchId", "itemId")
	 WHERE "dateId" BETWEEN "min_date" AND "max_date") AS t
LEFT JOIN distributor.remains AS remains USING("branchId", "itemId", "dateId")
WHERE remains."dateId" IS null